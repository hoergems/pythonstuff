'''
Created on 23.02.2012

@author: Marcus
'''
from ImageProc import ImageProc
import cv
import os

if __name__ == '__main__':    
    images = ImageProc.getGrayscaleImages(ImageProc.readFiles("../Bilder/"))
    resultImages = []
    stack1 = images[0:31]
    stack2 = images[59:65]
    stack3 = images[80:85]
    stack4 = images[92:102] 
    intervalls = [stack1, stack2, stack3, stack4]
    names = []
    for stack in intervalls:
        count = 0  
        resultImage = 0 
        ind = 0
        for i in range(0, len(stack)):            
            newCount = ImageProc.countWhitePixels(stack[i], 70)
            if (newCount > count):
                count = newCount
                resultImage = stack[i]
                ind = i
        resultImages.append(resultImage) 
        names.append(ind)       
    i = 0    
    
    for resultImage in resultImages:
        ImageProc.displayImage(resultImage, str(names[i]))
        ImageProc.saveImage(resultImage, "binary" + str(i))
        i += 1
        
