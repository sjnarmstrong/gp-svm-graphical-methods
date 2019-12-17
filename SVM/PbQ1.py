import svmutil
import svm
import numpy as np
import csv
import math

class IrusDataReader:
    def __init__(self, datafile='B/iris.data'):
        self.uniqueLabels=['Iris-versicolor', 'Iris-virginica', 'Iris-setosa']
        self.XValues = [[],[],[]]
        
        with open('B/iris.data') as f:
            for line in csv.reader(f):
                if len(line) == 0:
                    continue
                self.XValues[self.uniqueLabels.index(line[-1])].append([float(x) for x in line[:-1]])
        self.XValues = np.array(self.XValues);
        self.minX = None
        self.maxX = None
        
    def GetDataInPositiveNegativeFormat(self, positiveLabel, negativeLabel, splitRatio=0.4):
        indexPositive=self.uniqueLabels.index(positiveLabel)
        indexNegative=self.uniqueLabels.index(negativeLabel)
        
        y = np.array([1]*len(self.XValues[indexPositive]) + [-1]*len(self.XValues[indexNegative]))
        X = np.append(self.XValues[indexPositive],self.XValues[indexNegative],axis=0)
        
        return IrusDataReader.ShuffelAndSplit(X, y, np.arange(len(y)), splitRatio)
    
    def GetNormalisedData(self, XTest, XTrain=None):
        assert XTrain is not None or self.minX is not None, (
            "Please ensure that this functiomn is called at least once with the training dataset")
        if XTrain is not None:
            self.minX=np.min(XTrain,axis=0)
            self.maxX=np.max(XTrain,axis=0)
            return (XTest-self.minX)/(self.maxX-self.minX), (XTrain-self.minX)/(self.maxX-self.minX)
        return (XTest-self.minX)/(self.maxX-self.minX)
    
    def ShuffelAndSplit(X, y, randomizeIndicies, splitRatio=0.4):

        np.random.shuffle(randomizeIndicies)
        X=X[randomizeIndicies]
        y=y[randomizeIndicies]
        endTr=math.floor(splitRatio*len(y))
        
        return X[:endTr], y[:endTr], X[endTr:], y[endTr:]

def getVfoldCrossValidationold(param, XTrain, yTrain, v):
    errorAccumulator = 0
    xtrainlist=np.split(XTrain,v)
    ytrainlist=np.split(yTrain,v)
    
    trainx=np.empty((int(len(XTrain)*(v-1)/v),)+XTrain.shape[1:])
    trainy=np.empty(int(len(yTrain)*(v-1)/v))

    for i in range(len(xtrainlist)):
        testx=xtrainlist.pop(0)
        testy=ytrainlist.pop(0)
        np.concatenate(xtrainlist,out=trainx)
        np.concatenate(ytrainlist,out=trainy)
        
        prob = svmutil.svm_problem(trainy,trainx.tolist())
        m = svmutil.svm_train(prob, param)
        p_label, p_acc, p_val = svmutil.svm_predict(testy,testx.tolist(), m, '-b 1 -q')
        
        xtrainlist.append(testx)
        ytrainlist.append(testy)
        errorAccumulator +=100 - p_acc[0]
    return errorAccumulator/v
def getVfoldCrossValidation(param, XTrain, yTrain, n, splitRatio=0.4):
    errorAccumulator = 0
    ri=np.arange(len(yTrain))
    
    for i in range(n):
        trainx, trainy, testx, testy = IrusDataReader.ShuffelAndSplit(XTrain,yTrain,ri,splitRatio)
        prob = svmutil.svm_problem(trainy,trainx.tolist())
        m = svmutil.svm_train(prob, param)
        p_label, p_acc, p_val = svmutil.svm_predict(testy,testx.tolist(), m, '-b 1 -q')
        errorAccumulator +=100 - p_acc[0]
    return errorAccumulator
       

#XTrain, yTrain, XTest, yTest = IR.GetDataInPositiveNegativeFormat('Iris-versicolor', 'Iris-virginica')
#XTest, XTrain = IR.GetNormalisedData(XTest, XTrain) 
#
#
#prob = svmutil.svm_problem(yTrain,XTrain.tolist())
#param = svmutil.svm_parameter('-t 1 -c 4 -b 1 -r 5')
#m = svmutil.svm_train(prob, param)
#p_label, p_acc, p_val = svmutil.svm_predict(yTest,XTest.tolist(), m, '-b 1')

#param = svmutil.svm_parameter('-t 0 -c 4 -b 1')
#err = getVfoldCrossValidation(param,XTrain,yTrain,4)

"""
-s svm_type : set type of SVM (default 0)
	0 -- C-SVC
	1 -- nu-SVC
	2 -- one-class SVM
	3 -- epsilon-SVR
	4 -- nu-SVR
-t kernel_type : set type of kernel function (default 2)
	0 -- linear: u'*v
	1 -- polynomial: (gamma*u'*v + coef0)^degree
	2 -- radial basis function: exp(-gamma*|u-v|^2)
	3 -- sigmoid: tanh(gamma*u'*v + coef0)
-d degree : set degree in kernel function (default 3)
-g gamma : set gamma in kernel function (default 1/num_features)
-r coef0 : set coef0 in kernel function (default 0)
-c cost : set the parameter C of C-SVC, epsilon-SVR, and nu-SVR (default 1)
-n nu : set the parameter nu of nu-SVC, one-class SVM, and nu-SVR (default 0.5)
-p epsilon : set the epsilon in loss function of epsilon-SVR (default 0.1)
-m cachesize : set cache memory size in MB (default 100)
-e epsilon : set tolerance of termination criterion (default 0.001)
-h shrinking: whether to use the shrinking heuristics, 0 or 1 (default 1)
-b probability_estimates: whether to train a SVC or SVR model for probability estimates, 0 or 1 (default 0)
-wi weight: set the parameter C of class i to weight*C, for C-SVC (default 1)

The k in the -g option means the number of attributes in the input data.
"""
#[degree gamma coef0]
ranges=[[[0],[0],[0]],
        [np.arange(2,5),np.arange(-5.0,5.0),np.arange(-5.0,5.0)],
        [[0],np.arange(-5.0,5.0),[0]],
        [[0],np.arange(-4.0,2.0),np.arange(-5.0,3)]]

templateParameter = "-t {funcnr} -d {degree} -g {gamma} -r {coef0} -c {cost} -e 0.000001  -b 1"
reverseGridSearch=True
numberOfIterations = 1;
CostValues=[0.1,0.6,1,5,100]

total = len(np.arange(0,10)) * len(np.arange(-5,10,1))
count = -1
IR=IrusDataReader()

errors=np.empty((3,4,len(CostValues),numberOfIterations))

for iteration in range(numberOfIterations):
    print(100*iteration/numberOfIterations)
    for probnr, problem in enumerate([('Iris-versicolor', 'Iris-virginica'),('Iris-versicolor','Iris-setosa'),('Iris-virginica', 'Iris-setosa')]):
        XTrain, yTrain, XTest, yTest = IR.GetDataInPositiveNegativeFormat(problem[0],problem[1])
        XTest, XTrain = IR.GetNormalisedData(XTest, XTrain) 
        prob = svmutil.svm_problem(yTrain,XTrain.tolist())
        for funcnr in range(4):
            for costnr,cost in enumerate(CostValues):#[0.1,0.6,1,5,100]):
                besterr = float('inf')
                bestparams = None
                for degree in reversed(ranges[funcnr][0]) if reverseGridSearch else ranges[funcnr][0]:
                    for gammapow in reversed(ranges[funcnr][1]) if reverseGridSearch else ranges[funcnr][1]:
                        count+=1
                        #print(str(count/total)+"% complete best error is: "+str(besterr))
                        for coef0pow in reversed(ranges[funcnr][2]) if reverseGridSearch else ranges[funcnr][2]:
                            param = svmutil.svm_parameter(templateParameter.format(**{"degree":degree,
                                                                                      "gamma":2**gammapow,
                                                                                      "coef0": 2**coef0pow,
                                                                                      "cost": cost,
                                                                                      "funcnr":funcnr}))
                            err = getVfoldCrossValidation(param,XTrain,yTrain,100)
                            print(err)
                            if err < besterr:
                                besterr = err;
                                bestparams = param
                    if besterr == 0:
                        break
                m = svmutil.svm_train(prob, bestparams)
                p_label, p_acc, p_val = svmutil.svm_predict(yTest,XTest.tolist(), m, '-b 1 -q')
                errors[probnr][funcnr][costnr][iteration]=p_acc[0]
                #print(errors[probnr][funcnr][costnr][iteration],probnr,funcnr,costnr,iteration)

medians=np.percentile(errors,50,axis=3)
UQ=np.percentile(errors,75,axis=3)
LQ=np.percentile(errors,25,axis=3)
mean=np.mean(errors,axis=3)