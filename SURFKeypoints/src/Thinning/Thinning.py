'''
Created on 10.04.2012

@author: Marcus
'''

from ImageProc import ImageProc
import cv
import os
if __name__ == '__main__':
    image = ImageProc.getGrayscaleImages(ImageProc.getImage("hough92.bmp"))    
    binary = ImageProc.getBinaryImage(image, 30)     
    d = ImageProc.distanceTransformation(binary)
    thres = ImageProc.valueBetweenThresholds(d, 20, 100)  
    '''Erosion'''
    
    ImageProc.displayImage(d, "d")
    ImageProc.displayImage(thres, "thres")
    
    
    
    
    
    """value = image[20, 20]
    for i in xrange(0, image.height):
            for j in xrange(0, image.width):
                if (image[i, j] == value):
                    image[i, j] = 0"""
    
    