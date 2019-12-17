import numpy as np

def calcHalfDelta(i,j,x,y,h,eta,B):
    return (-h*x[i,j]
            +B*x[i,j]*(x[i-1,j]+x[i+1,j]+x[i,j-1]+x[i,j+1])
            +eta*x[i,j]*y[i,j])
    
def calcHalfDelta2(i,j,x,y,h,eta,B):
    return (-h*x[i,j]
            +B*x[i,j]*(x[i-1,j-1]+x[i  ,j-1]+x[i+1,j-1]+
                       x[i-1,j  ]           +x[i+1,j  ]+
                       x[i-1,j+1]+x[i  ,j+1]+x[i+1,j+1])
            +eta*x[i,j]*y[i,j])
            
def calcHalfDelta3(i,j,x,y,h,eta,B,alpha):
    return (-h*x[i,j]
            +B*x[i,j]*(alpha*x[i-1,j-1]+x[i  ,j-1]+alpha*x[i+1,j-1]+
                       x[i-1,j  ]           +x[i+1,j  ]+
                       alpha*x[i-1,j+1]+x[i  ,j+1]+alpha*x[i+1,j+1])
            +eta*x[i,j]*y[i,j])
            
def calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel):
    
    return (-h*x[i,j]
            +B*x[i,j]*np.sum(np.multiply(kernel,
                getZeroPaddedKernel(int(len(kernel)/2.0),x,i,j)), axis=(0,1))
            +eta*x[i,j]*y[i,j])

def CalcEnergy(x,y,h,eta,B):
    priorE=h*np.sum(x)
    
    adjEs=np.array([[-B*x[i,j]*(x[i-1,j]+x[i+1,j]+x[i,j-1]+x[i,j+1])/2
        for j in range(1,len(x[0])-1) ] 
            for i in range(1,len(x)-1)])
    
    yEs=-eta*x*y
    return priorE+np.sum(adjEs)+np.sum(yEs)

def getZeroPaddedKernel(halfKernelSize,x,i,j):
    i1,i2=max(i-halfKernelSize,0),min(i+halfKernelSize+1,len(x))
    j1,j2=max(j-halfKernelSize,0),min(j+halfKernelSize+1,len(x[0]))
    outhold = np.zeros((2*halfKernelSize+1,2*halfKernelSize+1)+x.shape[2:])
    outhold[i1-i+halfKernelSize:i2-i+halfKernelSize,j1-j+halfKernelSize:j2-j+halfKernelSize]=x[i1:i2,j1:j2]
    return outhold