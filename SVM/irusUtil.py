import numpy as np
import csv
import math
import svmutil

class IrusDataReader:
    def __init__(self, datafile='iris.data'):
        self.uniqueLabels=['Iris-versicolor', 'Iris-virginica', 'Iris-setosa']
        self.XValues = [[],[],[]]
        
        with open(datafile) as f:
            for line in csv.reader(f):
                if len(line) == 0:
                    continue
                self.XValues[self.uniqueLabels.index(line[-1])].append([float(x) for x in line[:-1]])
        self.XValues = np.array(self.XValues);
        self.minX = None
        self.maxX = None
        
    def GetDataInPositiveNegativeFormat(self, positiveLabel, negativeLabel, splitRatio=0.6):
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
    
    def ShuffelAndSplit(X, y, randomizeIndicies, splitRatio=0.6):

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

def getVfoldCrossValidation(param, XTrain, yTrain, n, splitRatio=0.7, prewnPercentage = 85):
    errorAccumulator = 0
    ri=np.arange(len(yTrain))
    
    for i in range(1,n+1):
        trainx, trainy, testx, testy = IrusDataReader.ShuffelAndSplit(XTrain,yTrain,ri,splitRatio)
        prob = svmutil.svm_problem(trainy,trainx.tolist())
        m = svmutil.svm_train(prob, param, '-q')
        p_label, p_acc, p_val = svmutil.svm_predict(testy,testx.tolist(), m, '-q')
        errorAccumulator +=p_acc[0]
        if i > 3 and errorAccumulator < prewnPercentage*i:
            return n*errorAccumulator/i
    return errorAccumulator