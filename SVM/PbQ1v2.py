import sys
sys.path.append('./libsvm-3.22/python')

from itertools import product
import numpy as np
import svmutil
from irusUtil import IrusDataReader, getVfoldCrossValidation
from multiprocessing import Pool
from functools import partial
import warnings
warnings.filterwarnings("ignore")

templateParameter = "-t {0} -d {1} -g {2} -r {3} -c {4} -q"
def getscore(XTrain, yTrain, n, vals):
    pstring = templateParameter.format(*[vals[0],vals[1],2**vals[2],2**vals[3],vals[4]])
    param = svmutil.svm_parameter(pstring)
    return getVfoldCrossValidation(param,XTrain,yTrain,n, splitRatio=0.6, prewnPercentage = 85), vals

#CostValues=[0.1,0.6,1,100]
CostValues=2.0**np.arange(-6,7)
numberOfTrials=50
problems=[('Iris-versicolor', 'Iris-virginica'),('Iris-versicolor','Iris-setosa'),('Iris-virginica', 'Iris-setosa')]
nvalues = [40,5,5]
pcounter=0
total=numberOfTrials*len(problems)
nextsteps1 = [1,1,1,0.25]
nextsteps2 = [1,1,1,0.25]



if __name__ == '__main__':
    IR=IrusDataReader()
    _pool = Pool(40)
    
    errors=np.empty((3,4,len(CostValues),numberOfTrials))
    Verrors=np.empty((3,4,len(CostValues),numberOfTrials))
    Allpstrings=[[[[None for i in range(50)] 
                    for j in range(len(CostValues))]
                    for k in range(4)]
                    for l in range(3)]
    
    for trial in range(numberOfTrials):
        for probnr, problem in enumerate(problems):
            print(100*pcounter/total)
            pcounter+=1
            XTrain, yTrain, XTest, yTest = IR.GetDataInPositiveNegativeFormat(*problem)
            XTest, XTrain = IR.GetNormalisedData(XTest, XTrain) 
            getscorepartial = partial(getscore, XTrain, yTrain, nvalues[probnr])
            
            for funcnr,costnr in product(range(4),range(len(CostValues))):
                nextstep1 = nextsteps1[funcnr]
                nextstep2 = nextsteps2[funcnr]
                ranges=[[[0],[0],[0]],
                    [np.arange(2,5),np.arange(0,5.0,nextstep1),np.arange(-4.0,10.0,nextstep2)],
                    [[0],np.arange(0,5.0,nextstep1),[0]],
                    [[0],np.arange(-3,3,nextstep1),np.arange(-3,3,nextstep2)]]
                params=[[funcnr]]+ranges[funcnr]+[[CostValues[costnr]]]
                
                for stepPow in range(12):
                    
                    scores,values = zip(*_pool.map(getscorepartial,product(*params)))
                        
                    bvi=np.argmax(scores)
                    besterrparams=values[bvi]
                    #print(scores[bvi],besterrparams)
                    
                    step1 = nextstep1       
                    nextstep1 = step1/2
                    step2 = nextstep2       
                    nextstep2 = step2/2
                    params[1]=[besterrparams[1]]
                    params[2]=np.arange(besterrparams[2]-step1,besterrparams[2]+step1+nextstep1,nextstep1)
                    params[3]=np.arange(besterrparams[3]-step2,besterrparams[3]+step2+nextstep2,nextstep2)
                    
                
                prob = svmutil.svm_problem(yTrain,XTrain.tolist())
                pstring = templateParameter.format(*[besterrparams[0],besterrparams[1],
                                                     2**besterrparams[2],2**besterrparams[3],besterrparams[4]])
                bestparams = svmutil.svm_parameter(pstring)
                
                m = svmutil.svm_train(prob, bestparams)
                p_label, p_acc, p_val = svmutil.svm_predict(yTest,XTest.tolist(), m, '-q')
                errors[probnr][funcnr][costnr][trial]=p_acc[0]
                Verrors[probnr][funcnr][costnr][trial]=scores[bvi]
                Allpstrings[probnr][funcnr][costnr][trial]=[besterrparams[0],besterrparams[1],
                                                     2**besterrparams[2],2**besterrparams[3],besterrparams[4]]
                

    medians=np.percentile(errors,50,axis=3)
    UQ=np.percentile(errors,75,axis=3)
    LQ=np.percentile(errors,25,axis=3)
    mean=np.mean(errors,axis=3)
    
    print("medians", medians)
    print("medians", UQ)
    print("medians", LQ)
    print("medians", mean)
    
    np.savez_compressed("OutputStats", medians, UQ, LQ, mean, errors, Verrors, Allpstrings)