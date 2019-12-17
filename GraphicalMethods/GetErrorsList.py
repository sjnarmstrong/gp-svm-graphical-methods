from os import listdir

from os.path import isfile, join, exists
import numpy as np

mypath="Outputs"
onlyfolders = [join(mypath,f) for f in listdir(mypath) if not isfile(join(mypath, f))]

for foldername in onlyfolders:
    if not exists(join(foldername,"errors.txt")):
        continue
    with open(join(foldername,"errors.txt")) as fp:
        hold = fp.read()
    hold=hold.replace("[","").replace("]","")
    a=np.fromstring(hold, sep=", ")
    print("{0}: {1:.2f}".format(*(foldername,a[-1]*100)))
