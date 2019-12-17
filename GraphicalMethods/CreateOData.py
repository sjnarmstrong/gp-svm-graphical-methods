import numpy as np
import matplotlib.pyplot as plt
from PcUtils import calcHalfDelta, calcHalfDelta2, calcHalfDelta3, calcHalfDeltaKernel
import os
from scipy.stats import multivariate_normal

def showImage(x,i,baseExperement):
    f, axis = plt.subplots(1, sharex=True,figsize=(15,8))
    axis.imshow(x)
    plt.xticks([])
    plt.yticks([])
    plt.savefig("Outputs/{0}/{1}.pdf".format(*(baseExperement,i)), format='pdf', dpi=500,bbox_inches="tight")
    plt.show()
    
y = np.loadtxt('y.txt', dtype=None, delimiter='\t')
x_gt = np.loadtxt('x_gt.txt', dtype=None, delimiter='\t')

baseExperement="OrigionalData"

if not os.path.exists("Outputs/{0}".format(*(baseExperement,))):
    os.makedirs("Outputs/{0}".format(*(baseExperement,)))   

showImage(y,"Noise","OrigionalData")
showImage(x_gt,"NoNoise","OrigionalData")