import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('./libsvm-3.22/python')
from irusUtil import IrusDataReader
plt.rcParams.update({'font.size': 24})
import os

def createPlot(Xpositive, Xnegative, namePositive, nameNegative, i, j):
    f, axis = plt.subplots(1, sharex=True,figsize=(15,8))
    axis.set_xlabel(r"$x_"+str(i+1)+"$")
    axis.set_ylabel(r"$x_"+str(j+1)+"$")
    axis.set_title("Plot of "+namePositive+" vs "+nameNegative)
    plt.scatter(Xpositive[:,i], Xpositive[:,j], c='b', label=namePositive)
    plt.scatter(Xnegative[:,i], Xnegative[:,j], c='r', label=nameNegative)
    plt.legend()
    plt.savefig("Output/"+namePositive+nameNegative+str(i)+"_"+str(j)+".pdf", format='pdf', dpi=500,bbox_inches="tight")
    plt.show()
def createPlots(Xpositive, Xnegative, namePositive, nameNegative):
    createPlot(Xpositive, Xnegative, namePositive, nameNegative, 0, 1)
    createPlot(Xpositive, Xnegative, namePositive, nameNegative, 0, 2)
    createPlot(Xpositive, Xnegative, namePositive, nameNegative, 0, 3)
    createPlot(Xpositive, Xnegative, namePositive, nameNegative, 1, 2)
    createPlot(Xpositive, Xnegative, namePositive, nameNegative, 1, 3)
    createPlot(Xpositive, Xnegative, namePositive, nameNegative, 2, 3)


if not os.path.exists("Output"):
    os.makedirs("Output")
IR=IrusDataReader()

i,j=0,1
createPlots(IR.XValues[i], IR.XValues[j], IR.uniqueLabels[i], IR.uniqueLabels[j])
i,j=0,2
createPlots(IR.XValues[i], IR.XValues[j], IR.uniqueLabels[i], IR.uniqueLabels[j])
i,j=1,2
createPlots(IR.XValues[i], IR.XValues[j], IR.uniqueLabels[i], IR.uniqueLabels[j])

