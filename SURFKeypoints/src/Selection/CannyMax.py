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
    cannyResultImages = []
    stack1 = images[0:31]
    stack2 = images[59:65]
    stack3 = images[80:85]
    stack4 = images[92:102] 
    intervalls = [stack1, stack2, stack3, stack4]
    index = 0
    for stack in intervalls:
        resultImage = 0
        resultCannyImage = 0
        count = 0
        for image in stack:
            canny = ImageProc.getCanny(image)
            newCount = ImageProc.countWhitePixels(canny, 50)
            if (newCount > count):
                resultImage = image
                resultCannyImage = canny
        resultImages.append(resultImage)
        cannyResultImages.append(resultCannyImage)   
    i = 0         
    for resultImage in resultImages:
        ImageProc.displayImage(resultImage, str(i))
        ImageProc.displayImage(cannyResultImages[i], "canny")
        ImageProc.saveImage(resultImage, "canny" + str(i))
        i += 1
    
            
            
        
        
    

