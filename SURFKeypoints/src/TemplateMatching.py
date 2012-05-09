'''
Created on 05.05.2012

@author: Marcus
'''
from ImageProc import ImageProc

if __name__ == '__main__':
    image = ImageProc.getGrayscaleImages(ImageProc.getImage(r'Images\Package142.bmp'))
    resultImage = ImageProc.getGrayscaleImages(ImageProc.getImage(r'Images\Package142.bmp'))
    template = ImageProc.getGrayscaleImages(ImageProc.getImage(r'Images\template.bmp'))    
    res = ImageProc.templateMatching(image, template)
    ImageProc.saveImage(res, r'Images\templa.png')
    #image = ImageProc.getGrayscaleImages(ImageProc.getImage(r'Images\templa.png.bmp'))
    #result = ImageProc.getBinaryImage(ImageProc.invert(image), 155)
                
    #ImageProc.displayImage(result, 'inv')
    