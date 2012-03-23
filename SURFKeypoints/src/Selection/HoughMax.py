'''
Created on 23.02.2012

@author: Marcus
'''
"""

"""
from math import pi
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
    lines = []    
    for stack in intervalls:
        max = 0
        resultImage = 0
        cannyResultImage = 0
        for image in stack:
            storage = cv.CreateMemStorage(0)
            canny = ImageProc.getCanny(image)
            lines = cv.HoughLines2(canny, storage, cv.CV_HOUGH_PROBABILISTIC, 1, pi / 180, 50, 75, 10) 
            if (len(lines) > max):
                max = len(lines)
                resultImage = (image, max)
                cannyResultImage = (canny, max)                               
        resultImages.append(resultImage)
        cannyResultImages.append(cannyResultImage)    
    for (image, max) in resultImages:        
        ImageProc.saveImage(image, "hough" + str(max))
    for (image, max) in cannyResultImages:
        ImageProc.saveImage(image, "houghCanny" + str(max))
    
        
    
