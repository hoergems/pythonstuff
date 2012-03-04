'''
Created on 04.03.2012

@author: Marcus
'''
import cv
from ImageProc import ImageProc

if __name__ == '__main__': 
    image = ImageProc.getImage('t1.jpg')
    image = ImageProc.getGrayscaleImages(image) 
    image = ImageProc.transformToRange(image, 0, 4)   
    dm = [[1, 3], [2, 0]] 
    image = ImageProc.dither(image, dm)  
    ImageProc.displayImage(image, 'img')
