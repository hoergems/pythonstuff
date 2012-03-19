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
    nextImages = []
    stack1 = images[0:31]
    stack2 = images[59:65]
    stack3 = images[80:85]
    stack4 = images[92:102] 
    intervalls = [stack1, stack2, stack3, stack4]
    lines = []
    ind = 0
    for stack in intervalls:
        max = 0
        resultImage = 0
        for i in range(0, len(stack)):
            storage = cv.CreateMemStorage(0)
            lines = cv.HoughLines2(ImageProc.getCanny(stack[i]), storage, cv.CV_HOUGH_PROBABILISTIC, 1, pi / 180, 50, 75, 10) 
            if (len(lines) > max):
                max = len(lines)
                resultImage = stack[i] 
                ind = i               
        resultImages.append(resultImage)
    i = 0
    for i in range(0, len(resultImages)):
        ImageProc.displayImage(resultImages[i], str(i))
        ImageProc.saveImage(resultImages[i], "hough" + str(i))
    
        
    
