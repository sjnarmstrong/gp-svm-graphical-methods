import numpy as np
import matplotlib.pyplot as plt
import svmutil

def create1Dplot(dfn,da,db,N,m,i,j,Xpositive,Xnegative,minx,maxx):
    x,y=np.meshgrid(da,db)
    X=np.concatenate(dfn(x,y)).T.reshape(-1,4)
    
    p_label, p_acc, p_val = svmutil.svm_predict([0]*len(X),X.tolist(), m, '-q')
    p_val=np.array(p_val).reshape(N,N).T
    Imin=np.argmin(np.abs(p_val),axis=0)
    Iminm1=np.argmin(np.abs(p_val-1),axis=0)
    Iminp1=np.argmin(np.abs(p_val+1),axis=0)
    
    plt.scatter(Xpositive[:,i], Xpositive[:,j], c='b')
    plt.scatter(Xnegative[:,i], Xnegative[:,j], c='r')
    
    includeI=np.where(db[Imin]!=minx[j])
    Imin=Imin[includeI]
    daplot=da[includeI]
    includeI=np.where(db[Imin]!=maxx[j])
    Imin=Imin[includeI]
    daplot=daplot[includeI]
    
    plt.plot(daplot,db[Imin], c='k')
    
    includeI=np.where(db[Iminp1]!=minx[j])
    Iminp1=Iminp1[includeI]
    daplot=da[includeI]
    includeI=np.where(db[Iminp1]!=maxx[j])
    Iminp1=Iminp1[includeI]
    daplot=daplot[includeI]
    
    plt.plot(daplot,db[Iminp1], c='k', ls='--')
    
    includeI=np.where(db[Iminm1]!=minx[j])
    Iminm1=Iminm1[includeI]
    daplot=da[includeI]
    includeI=np.where(db[Iminm1]!=maxx[j])
    Iminm1=Iminm1[includeI]
    daplot=daplot[includeI]
    
    plt.plot(daplot,db[Iminm1], c='k', ls='--')
    plt.show()
    
    

    
minx=np.min(XTest,axis=0)
maxx=np.max(XTest,axis=0)
N=1000
d1=np.linspace(minx[0],maxx[0],N,dtype=np.float16)
d2=np.linspace(minx[1],maxx[1],N,dtype=np.float16)
d3=np.linspace(minx[2],maxx[2],N,dtype=np.float16)
d4=np.linspace(minx[3],maxx[3],N,dtype=np.float16)     

prob = svmutil.svm_problem(yTrain,XTrain.tolist())
bestparams = svmutil.svm_parameter(pstring)
                
m = svmutil.svm_train(prob, bestparams)
    
Xpositive=XTest[np.where(yTest == 1)]
Xnegative=XTest[np.where(yTest == -1)]

#plt.scatter(Xpositive[:,0], Xpositive[:,1], c='b')
#plt.scatter(Xnegative[:,0], Xnegative[:,1], c='r')
#plt.show()
#plt.scatter(Xpositive[:,0], Xpositive[:,2], c='b')
#plt.scatter(Xnegative[:,0], Xnegative[:,2], c='r')
#plt.show()
#plt.scatter(Xpositive[:,0], Xpositive[:,3], c='b')
#plt.scatter(Xnegative[:,0], Xnegative[:,3], c='r')
#plt.show()
#plt.scatter(Xpositive[:,1], Xpositive[:,2], c='b')
#plt.scatter(Xnegative[:,1], Xnegative[:,2], c='r')
#plt.show()
#plt.scatter(Xpositive[:,1], Xpositive[:,3], c='b')
#plt.scatter(Xnegative[:,1], Xnegative[:,3], c='r')
#plt.show()


create1Dplot(lambda x,y:([x],[y],[np.ones((N,N))*(maxx[2]-minx[2])/2],[np.ones((N,N))*(maxx[2]-minx[2])/2]),d1,d2,N,m,0,1,Xpositive,Xnegative,minx,maxx)
create1Dplot(lambda x,y:([x],[np.zeros((N,N))],[y],[np.zeros((N,N))]),d1,d3,N,m,0,2,Xpositive,Xnegative,minx,maxx)
create1Dplot(lambda x,y:([x],[np.zeros((N,N))],[np.zeros((N,N))],[y]),d1,d4,N,m,0,3,Xpositive,Xnegative,minx,maxx)
create1Dplot(lambda x,y:([np.zeros((N,N))],[x],[y],[np.zeros((N,N))]),d2,d3,N,m,1,2,Xpositive,Xnegative,minx,maxx)
create1Dplot(lambda x,y:([np.zeros((N,N))],[x],[np.zeros((N,N))],[y]),d2,d4,N,m,1,3,Xpositive,Xnegative,minx,maxx)
create1Dplot(lambda x,y:([np.zeros((N,N))],[np.zeros((N,N))],[x],[y]),d3,d4,N,m,2,3,Xpositive,Xnegative,minx,maxx)

#a,b,c,d=np.meshgrid(d1,d2,d3,d4)
#X=np.concatenate(([a],[b],[c],[d])).T.reshape(-1,4)
#p_label, p_acc, p_val = svmutil.svm_predict([0]*len(X),X.tolist(), m, '-q')
#p_val=np.array(p_val).reshape(N,N,N,N).T
#
#Imin = np.abs(p_val.reshape(N,-1)).argmax(1)
#Imin = np.column_stack(np.unravel_index(Imin, p_val[0,:,:].shape))
#Iminm1 = np.abs(p_val-1).argmax(1)
#Iminm1 = np.column_stack(np.unravel_index(Imin, p_val[0,:,:].shape))
#Iminp1 = np.abs(p_val+1).argmax(1)
#Iminp1 = np.column_stack(np.unravel_index(Imin, p_val[0,:,:].shape))

#Imin=np.argmin(np.abs(p_val),axis=(1,2,3))
#Iminm1=np.argmin(np.abs(p_val-1),axis=(1,2,3))
#Iminp1=np.argmin(np.abs(p_val+1),axis=(1,2,3))


#a=k(1.0,1.0)