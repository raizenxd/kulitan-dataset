import numpy as np
import cv2
import os

IMG_DIR = 'kulitan'

def createFileList(myDir, format='.png'):
    fileList = []
    print(myDir)
    ind = 0
    for root, dirs, files in os.walk(myDir, topdown=False):
        
        for name in files:
            
            
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append([ind,fullName])
        ind=+1
                
    return fileList
print(createFileList("kulitan"))
# ind =0
# for i,j,k in (os.walk("kulitan", topdown=False)):
#         print(k,ind)
#         ind=+1
