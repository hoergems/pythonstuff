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
    cannyResultImages = []
    stack1 = images[0:31]
    stack2 = images[59:65]
    stack3 = images[80:85]
    stack4 = images[92:102] 
    intervalls = [stack1, stack2, stack3, stack4]
    names = []
    for stack in intervalls:
        count = 0  
        resultImage = 0
        cannyResultImage = 0         
        for image in stack:            
            newCount = ImageProc.countWhitePixels(image, 70)
            if (newCount > count):
                count = newCount
                resultImage = (image, count)
                cannyResultImage = (ImageProc.getCanny(image), count)                
        resultImages.append(resultImage) 
        cannyResultImages.append(cannyResultImage) 
    for (image, count) in resultImages:        
        ImageProc.saveImage(image, "binaryMax" + str(count))
    for (image, count) in cannyResultImages:
        ImageProc.saveImage(image, "binaryMaxCanny" + str(count))                                
        
