import numpy as np
from PcUtils import calcHalfDelta, calcHalfDelta2, calcHalfDelta3,calcHalfDeltaKernel
from PSO2 import PSO
import matplotlib.pyplot as plt

N=30
maxIt1= 100
maxit2= 10

#p=2
#deltafn = calcHalfDelta

#p=2
#deltafn = calcHalfDelta2

#p=2
#deltafn = lambda i,j,x,y,h,eta,B: calcHalfDelta3(i,j,x,y,h,eta,B,0.75)

#p=3
#deltafn = calcHalfDelta3

#p=2
#kernel = np.array([[1,4,6,4,1],
#                   [4,16,24,16,4],
#                   [6,24,0,24,6],
#                   [4,16,24,16,4],
#                   [1,4,6,4,1]])/220.0
#kernel = kernel.reshape(kernel.shape+(1,))
#deltafn = lambda i,j,x,y,h,eta,B: calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel)

#p=2
#kernel = np.ones((5,5,1))
#kernel[2,2,0] = 0
#deltafn = lambda i,j,x,y,h,eta,B: calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel)

#p=2
#kernel = np.array([[0,0,1,0,0],
#                   [0,1,1,1,0],
#                   [1,1,0,1,1],
#                   [0,1,1,1,0],
#                   [0,0,1,0,0]]).reshape(5,5,1)
#deltafn = lambda i,j,x,y,h,eta,B: calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel)

p=10
deltafn = lambda i,j,x,y,h,eta,B, p1,p2,p3,p4,p5,p6,p7,p8: calcHalfDeltaKernel(i,j,x,y,h,eta,B,
         np.array([[p1,p2,p3,p2,p1],
                   [p4,p5,p6,p5,p4],
                   [p7,p8,[0]*N,p8,p7],
                   [p4,p5,p6,p5,p4],
                   [p1,p2,p3,p2,p1]]))

y = np.loadtxt('C/y.txt', dtype=None, delimiter='\t')
x_gt = np.loadtxt('C/x_gt.txt', dtype=None, delimiter='\t')
y=np.concatenate((np.zeros((len(y),1)),y,np.zeros((len(y),1))),axis=1)
y=np.concatenate((np.zeros((1,len(y[0]))),y,np.zeros((1,len(y[0])))),axis=0)
x_gt=np.concatenate((np.zeros((len(x_gt),1)),x_gt,np.zeros((len(x_gt),1))),axis=1)
x_gt=np.concatenate((np.zeros((1,len(x_gt[0]))),x_gt,np.zeros((1,len(x_gt[0])))),axis=0)

weights = np.random.uniform(0,1,(N,p))
eta = 1.0

def calcerror(y,x_gt):
    h = weights.T[0]*0.2-0.1
    B = np.abs(weights.T)[1]
    other = np.abs((weights.T)[2:])
    dfn = lambda i,j,x,y: deltafn(i,j,x,y,h,eta,B,*other)
    
    x = y.copy()
    x = np.repeat(x.reshape(x.shape+(1,)),N,axis=2)
    flipped=True
    counter=0
    while flipped and counter < maxit2:
        flipped=False
        counter=counter+1
        for i in range(1,len(x)-1):
            for j in range(1,len(x[0])-1):
                flipIndicies = np.where(dfn(i,j,x,y) < 0)[0]
                if len(flipIndicies) > 0:
                    x[i,j,flipIndicies] = -x[i,j,flipIndicies]
                    flipped = True
    
    #plt.imshow(x.reshape(y.shape[0],-1))
    #plt.show()
    return np.count_nonzero(x_gt.reshape(x_gt.shape+(1,))-x,axis=(0,1))/y[1:-1,1:-1].size

pso=PSO(1.49618,1.49618,0.7298,weights,calcerror,np.random.uniform(-0.5,0.7,weights.shape))
#pso=PSO(0.001,1.49618,0.999,weights,calcerror,np.random.uniform(-0.01,0.01,weights.shape))
#pso=PSO(0.2,0.3,0.999,weights,calcerror,np.random.uniform(-0.1,0.1,weights.shape))

error = 1
for i in range(maxIt1):
    weightsbefore = weights.copy()
    error=pso.iterate(y,x_gt,weights)
    print(error)
    print(weights)

err,weights=pso.getBestWeightsAndError()
h = weights.T[0]*0.2-0.1
B = np.abs(weights.T)[1]
other = np.abs((weights.T)[2:])
print(np.append([eta,B,h],other))

