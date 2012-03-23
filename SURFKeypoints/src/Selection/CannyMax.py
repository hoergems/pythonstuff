'''
Created on 23.02.2012

@author: Marcus
'''
from ImageProc import ImageProc
import cv
import os

"""Gets the picture with the most white pixels in the canny filtered picture"""
if __name__ == '__main__':    
    images = ImageProc.getGrayscaleImages(ImageProc.readFiles("../Bilder/"))
    cannyImages = ImageProc.getCanny(images)
    resultImages = []
    resultCannyImages = []
    stack1 = images[0:31]
    stack2 = images[59:65]
    stack3 = images[80:85]
    stack4 = images[92:102] 
    intervalls = [stack1, stack2, stack3, stack4]
    index = 0
    for stack in intervalls:
        resultImage = (stack[0], 0)
        resultCannyImage = 0        
        count = 0
        for image in stack:
            canny = ImageProc.getCanny(image)
            newCount = ImageProc.countWhiteCannyPixels(canny)            
            if (newCount > count):
                resultImage = (image, newCount) 
                resultCannyImage = (canny, newCount)
                count = newCount               
        resultImages.append(resultImage) 
        resultCannyImages.append(resultCannyImage)          
    for (image, count) in resultImages:             
        ImageProc.saveImage(image, "result" + str(count))
    for (canny, count) in resultCannyImages:
        ImageProc.saveImage(canny, "canny" + str(count))
    
        
    
            
            
        
        
    

