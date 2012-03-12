'''
Created on 23.02.2012

@author: Marcus
'''
from ImageProc import ImageProc
import cv
import os

"""Gets the picture with the most white pixels in the canny filtered picture"""
if __name__ == '__main__':    
    images = ImageProc.getGrayscaleImages(ImageProc.readFiles("../stack/"))
    cannyImages = ImageProc.getCanny(images)
    resultImages = []
    cannyResultImages = []
    stack1 = images[0:70]
    stack2 = images[71:85]
    stack3 = images[86:108]
    intervalls = [stack1, stack2, stack3]
    index = 0
    for stack in intervalls:
        count = 0  
        resultImage = 0 
        cannyResultImage = 0
        for image in stack:            
            newCount = ImageProc.countWhitePixels(image, 70)
            if (newCount > count):
                count = newCount
                cannyResultImage = image
                resultImage = images[index]
            index += 1
        cannyResultImages.append(cannyResultImage)
        resultImages.append(resultImage)
    i = 0    
    for resultImage in resultImages:
        ImageProc.displayImage(resultImage, str(i))
        ImageProc.saveImage(resultImage, "canny" + str(i))
        i += 1
    
            
            
        
        
    

