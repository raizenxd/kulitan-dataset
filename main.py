from PIL import Image
import numpy as np
import sys
import os
import csv

#Useful function
def createFileList(myDir, format='.png'):
    fileList = []    
    print(myDir)
    ind = 0
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append([ind,fullName])
        ind+=1
    return fileList

def imageToBinary(file):
    img_file = Image.open(file)
    # img_file.show()

    # get original image parameters...
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode

    # Make image Greyscale
    img_grey = img_file.convert('L')
    #img_grey.save('result.png')
    #img_grey.show()

    # Save Greyscale values
    value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
    value = value.flatten()
    return value

    
# load the original image
myFileList = createFileList('kulitan/')

print(myFileList)
with open("img_pixels.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    
    for file in myFileList:
        value = imageToBinary(file[1])    
        writer.writerow([file[0]]+value)
    
    
    