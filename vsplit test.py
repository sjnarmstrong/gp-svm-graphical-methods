import numpy as np

a=np.split(np.arange(100).reshape(20,5),5)
train=np.empty((int(20*4/5),5))
for i in range(len(a)):
    test=a.pop(0)
    np.concatenate(a,out=train)
    a.append(test)
    print(test)
    print(train)
