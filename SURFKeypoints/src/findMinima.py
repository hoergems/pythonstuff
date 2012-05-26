'''
Created on 09.05.2012

@author: Marcus
'''
from ImageProc import ImageProc
import cv

if __name__ == '__main__':
    image = ImageProc.getGrayscaleImages(ImageProc.getImage(r'Images\templa2.bmp'))
    
    minima = ImageProc.countLocalMinima(image)
    ImageProc.saveImage(minima, r'Images\minima')
    ImageProc.displayImage(minima, 'minima')
