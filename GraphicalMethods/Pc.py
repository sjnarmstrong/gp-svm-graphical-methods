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

"""
Uncomment the code below for linear kernel
"""
eta,B,h=[1.0, 0.9733538906406877, 0.25664986425619485]
kernel = [[0.0,1.0,0.0],[0.0,0.0,0.0],[0.0,1.0,0.0]]
#kernel = [[0.0,0.0,0.0],[1.0,0.0,1.0],[0.0,0.0,0.0]]
deltafn = lambda i,j,x,y,h,eta,B: calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel)
baseExperement="linear kernel "+("Horisontal" if kernel[0][1]==0.0 else "Vertical")
"""
end code
"""
"""
Uncomment the code below for origional kernel
"""
#eta,B,h=[1.0, 1.0002173339804135, 0.0026599497677005732]
#kernel = [[0.0,1.0,0.0],[1.0,0.0,1.0],[0.0,1.0,0.0]]
#deltafn = lambda i,j,x,y,h,eta,B: calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel)
#baseExperement="origional kernel"
"""
end code
"""
"""
Uncomment the code below for 3x3 all ones kernel
"""
#eta,B,h=[1, 0.7279431887199235, -0.003404843432220862]
#kernel = [[1.0,1.0,1.0],[1.0,0.0,1.0],[1.0,1.0,1.0]]
#deltafn = lambda i,j,x,y,h,eta,B: calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel)
#baseExperement="3x3allones-kernel"
"""
end code
"""

"""
Uncomment the code below for 0.75 kernel
"""
#eta,B,h=[1, 0.731207314864619, 0.002424638538147326]
#kernel = [[0.75,1.0,0.75],[1.0,0.0,1.0],[0.75,1.0,0.75]]
#deltafn = lambda i,j,x,y,h,eta,B: calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel)
#baseExperement="0.75-kernel"
"""
end code
"""

"""
Uncomment the code below for 3x3 Self-taught
"""
#eta,B,h,alpha=[1, 0.335270367102513, 0.009194185328781215, 1.8934619502696788]
#kernel = [[alpha,1.0,alpha],[1.0,0.0,1.0],[alpha,1.0,alpha]]
#deltafn = lambda i,j,x,y,h,eta,B: calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel)
#baseExperement="3x3Self-taught-kernel"
"""
end code
"""

"""
Uncomment the code below for isotropic-kernel
"""
#eta,B,h=[1.,3.47061984, 0.05634049]
#kernel = np.array([[1,4,6,4,1],
#       [4,16,24,16,4],
#       [6,24,0,24,6],
#       [4,16,24,16,4],
#       [1,4,6,4,1]])/220
#deltafn = lambda i,j,x,y,h,eta,B: calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel)
#baseExperement="isotropic-kernel"
"""
end code
"""

"""
Uncomment the code below for all ones kernel
"""
Ksize,eta,B,h=[3, 1.,0.9870840230255296, 0.11076343683468912]
Ksize,eta,B,h=[5, 1.,0.13500390637795967, 0.025191847253556443]
Ksize,eta,B,h=[7, 1.,0.05533274935559791, 0.07901829449035577]
Ksize,eta,B,h=[9, 1.,0.033232126437277965, -0.023844184870502244]
Ksize,eta,B,h=[11, 1., 0.02070972036125934, -0.016085647132287703]
Ksize,eta,B,h=[13, 1., 0.014344931247742797, -0.032685960521097734]
Ksize,eta,B,h=[15, 1., 0.008585157977984325, 0.05101712096398803]
Ksize,eta,B,h=[17, 1., 0.008200758998751334, -0.12133292526033616]
kernel = np.ones((Ksize,Ksize))
kernel[2,2] = 0
deltafn = lambda i,j,x,y,h,eta,B: calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel)
baseExperement="{0}x{0}All-Ones-kernel".format(*(Ksize,))
"""
end code
"""

"""
Uncomment the code below for the diamond kernel
"""
#eta,B,h=[1.,0.32362707, 0.14628563]
#kernel = np.array([[0,0,1,0,0],
#                   [0,1,1,1,0],
#                   [1,1,0,1,1],
#                   [0,1,1,1,0],
#                   [0,0,1,0,0]])
#deltafn = lambda i,j,x,y,h,eta,B: calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel)
#baseExperement="diamond-kernel"
"""
end code
"""

"""
Uncomment the code below for the self taught kernel
"""
#eta,B,h, p1,p2,p3,p4,p5,p6,p7,p8=[1.0, 0.34188664016473047, -0.03575046095463899, 0.15687806091639994, 0.15011245823980432, 0.5177043219610065, 0.5820422652798767, 0.40708901901133887, 1.0030110550432347, 0.14775766072120836, 1.0496670650443842]
#kernel = np.array([[p1,p2,p3,p2,p1],
#                   [p4,p5,p6,p5,p4],
#                   [p7,p8,0,p8,p7],
#                   [p4,p5,p6,p5,p4],
#                   [p1,p2,p3,p2,p1]])
#deltafn = lambda i,j,x,y,h,eta,B: calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel)
#baseExperement="Self-taught-kernel"
"""
end code
"""

"""
Uncomment the code below for the gaussian kernal of sizek
"""
#Ksize,eta,B,h=[3, 1, 6.3026128732084175, 0.11931728867851185]
#Ksize,eta,B,h=[5, 1, 3.258966782128783, 0.006147828825118745]
#Ksize,eta,B,h=[7, 1, 3.2594461602698326, 0.014590365327907376]
#Ksize,eta,B,h=[9, 1, 3.317084213127566, 0.01835127362462531]
#Ksize,eta,B,h=[11, 1, 2.646606549820204, -0.02935892057239342]
#Ksize,eta,B,h=[13, 1, 2.805965782216654, 0.04594185359048869]
#Ksize,eta,B,h=[15, 1, 2.63178013188511, 0.002482373887654085]
#Ksize,eta,B,h=[17, 1, 2.552281149277945, -0.01981831963091582]
#hlenK=int(Ksize/2)
#itemsToCheck=np.mgrid[-hlenK:hlenK+1:1, -hlenK:hlenK+1:1].reshape(2,Ksize,Ksize).T
#kernel=multivariate_normal.pdf(itemsToCheck, mean=[0,0], cov=hlenK*np.eye(2))
#kernel[hlenK,hlenK]=0
#kernel/=np.sum(kernel)
#deltafn = lambda i,j,x,y,h,eta,B: calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel)
#baseExperement="{0}x{0}GaussianKernel".format(*(Ksize,))
"""
end code
"""

"""
Uncomment the code below for Questions
"""
#eta,B,h, p1,p2,p3,p4,p5,p6,p7,p8=[0, 0.34188664016473047, -0.03575046095463899, 0.15687806091639994, 0.15011245823980432, 0.5177043219610065, 0.5820422652798767, 0.40708901901133887, 1.0030110550432347, 0.14775766072120836, 1.0496670650443842]
#baseExperement="a1"
##eta,B,h, p1,p2,p3,p4,p5,p6,p7,p8=[1.0, 0, -0.03575046095463899, 0.15687806091639994, 0.15011245823980432, 0.5177043219610065, 0.5820422652798767, 0.40708901901133887, 1.0030110550432347, 0.14775766072120836, 1.0496670650443842]
##baseExperement="a2"
#eta,B,h, p1,p2,p3,p4,p5,p6,p7,p8=[1.0, 0.34188664016473047, 0, 0.15687806091639994, 0.15011245823980432, 0.5177043219610065, 0.5820422652798767, 0.40708901901133887, 1.0030110550432347, 0.14775766072120836, 1.0496670650443842]
#baseExperement="a3"
#kernel = np.array([[p1,p2,p3,p2,p1],
#                   [p4,p5,p6,p5,p4],
#                   [p7,p8,0,p8,p7],
#                   [p4,p5,p6,p5,p4],
#                   [p1,p2,p3,p2,p1]])
#deltafn = lambda i,j,x,y,h,eta,B: calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel)

"""
end code
"""


x=y.copy()
hlenK=int(len(kernel)/2)
itemsToCheck=np.mgrid[-hlenK:hlenK+1:1, -hlenK:hlenK+1:1].reshape(2,-1).T
toCheck=set()      

if not os.path.exists("Outputs/{0}".format(*(baseExperement,))):
    os.makedirs("Outputs/{0}".format(*(baseExperement,)))       

errors = []

looper=0
showImage(x,looper,baseExperement)
error=np.count_nonzero(x_gt-x)/x.size
errors.append(error)
print(error)
for i in range(0,len(x)):
    for j in range(0,len(x[0])):
        if deltafn(i,j,x,y,h,eta,B) < 0:
            x[i,j]=-x[i,j]
            toCheck|=set(map(tuple,[i,j]+itemsToCheck))
            
while len(toCheck)>0:
    looper+=1
    showImage(x,looper,baseExperement)
    error=np.count_nonzero(x_gt-x)/x.size
    errors.append(error)
    toCheckNext=set() 
    for i,j in toCheck:
        if -1 < i < len(y) and -1< j < len(y[0]):
            if deltafn(i,j,x,y,h,eta,B) < 0:
                x[i,j]=-x[i,j]
                toCheckNext|=set(map(tuple,[i,j]+itemsToCheck))
    toCheck=toCheckNext

with open("Outputs/"+baseExperement+"/errors.txt",'w') as f:
    f.write(str(errors))