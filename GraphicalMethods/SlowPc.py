import numpy as np
import matplotlib.pyplot as plt
from PcUtils import calcHalfDelta, calcHalfDelta2, calcHalfDelta3, calcHalfDeltaKernel

y = np.loadtxt('y.txt', dtype=None, delimiter='\t')
x_gt = np.loadtxt('x_gt.txt', dtype=None, delimiter='\t')


#eta,B,h=[1.0, 1.0002173339804135, 0.0026599497677005732]
#kernel = [[0.0,1.0,0.0],[1.0,0.0,1.0],[0.0,1.0,0.0]]
#deltafn = lambda i,j,x,y,h,eta,B: calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel)

#eta,B,h=[1, 0.7279431887199235, -0.003404843432220862]
#kernel = [[1.0,1.0,1.0],[1.0,0.0,1.0],[1.0,1.0,1.0]]
#deltafn = lambda i,j,x,y,h,eta,B: calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel)

#eta,B,h=[1, 0.731207314864619, 0.002424638538147326]
#kernel = [[0.75,1.0,0.75],[1.0,0.0,1.0],[0.75,1.0,0.75]]
#deltafn = lambda i,j,x,y,h,eta,B: calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel)

#eta,B,h,alpha=[1, 0.335270367102513, 0.009194185328781215, 1.8934619502696788]
#kernel = [[alpha,1.0,alpha],[1.0,0.0,1.0],[alpha,1.0,alpha]]
#deltafn = lambda i,j,x,y,h,eta,B: calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel)

#eta,B,h=[1.,3.47061984, 0.05634049]
#kernel = np.array([[1,4,6,4,1],
#       [4,16,24,16,4],
#       [6,24,0,24,6],
#       [4,16,24,16,4],
#       [1,4,6,4,1]])/220
#deltafn = lambda i,j,x,y,h,eta,B: calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel)

#eta,B,h=[ 1.,0.14314946,-0.04078734]
#kernel = np.ones((5,5))
#kernel[2,2] = 0
#deltafn = lambda i,j,x,y,h,eta,B: calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel)

eta,B,h=[1.,0.32362707, 0.14628563]
kernel = np.array([[0,0,1,0,0],
                   [0,1,1,1,0],
                   [1,1,0,1,1],
                   [0,1,1,1,0],
                   [0,0,1,0,0]])
deltafn = lambda i,j,x,y,h,eta,B: calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel)

#eta,B,h, p1,p2,p3,p4,p5,p6,p7,p8=[1.,0.26520571, 0.05290612, 0.08490018, 0.34262142, 0.24595569,
# 0.41110715, 0.49137222, 1.35086212, 0.62694615, 1.68961397]
#kernel = np.array([[p1,p2,p3,p2,p1],
#                   [p4,p5,p6,p5,p4],
#                   [p7,p8,0,p8,p7],
#                   [p4,p5,p6,p5,p4],
#                   [p1,p2,p3,p2,p1]])
#deltafn = lambda i,j,x,y,h,eta,B: calcHalfDeltaKernel(i,j,x,y,h,eta,B,kernel)

x=y.copy()
plt.imshow(x_gt[1:-1,1:-1])
plt.show()

flipped = True
while flipped:
    flipped = False
    plt.imshow(x)
    plt.show()
    error=np.count_nonzero(x_gt-x)/x.size
    print(error)
    for i in range(0,len(x)):
        for j in range(0,len(x[0])):
            if deltafn(i,j,x,y,h,eta,B) < 0:
                flipped = True
                x[i,j]=-x[i,j]
                
