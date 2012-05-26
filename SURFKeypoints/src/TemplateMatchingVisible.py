'''
Created on 09.05.2012

@author: Marcus
'''
from ImageProc import ImageProc

if __name__ == '__main__':
    template = ImageProc.getGrayscaleImages(ImageProc.getImage(r'Images\template.bmp'))
    templateBright = ImageProc.brighten(template)    
    ImageProc.saveImage(templateBright, r'Images\template_bright.bmp')
    image = ImageProc.getGrayscaleImages(ImageProc.getImage(r'Images\templa.png.bmp'))
    sample = ImageProc.getGrayscaleImages(ImageProc.getImage(r'Images\Package142.bmp'))
    ImageProc.displayImage(sample, 'samp')
    ImageProc.displayImage(image, 'inverted')    
    for i in xrange(0, image.height):
        for j in xrange(0, image.width):
            if image[i, j] > 50:
                image[i, j] = 255
    ImageProc.displayImage(image, 'inverted2')
    ImageProc.saveImage(image, r'Images\templa_invert4')
                    
                
    
