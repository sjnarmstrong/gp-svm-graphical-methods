import numpy as np
from scipy.io import loadmat

a=loadmat("matlab.mat")
ScoreList=a["ScoreList"][0]
hypList=a["hypList"]
initialParams=a["initialParams"]


ip=np.exp([initialParams[0,i][1][0].tolist() + initialParams[0,i][2][0].tolist()
    for i in range(10)])

hp=np.exp([hypList[0,i][1][0].tolist() + hypList[0,i][2][0].tolist()
    for i in range(10)])

cp = np.concatenate((ip,hp,ScoreList.reshape(10,1)),axis=1)


formatstring="%.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f & %.2e, %.2e, %.2e, %.2f, %.2f, %.2e, %.2e & %.3e\\\\\\hline"
formatstring="%.2f, %.2f, %.2f, %.2f, %.2e & %.2e, %.2e, %.2f, %.2e, %.2e & %.3e\\\\\\hline"

for i in range(10):
    print(formatstring% tuple(cp[i].tolist()) )