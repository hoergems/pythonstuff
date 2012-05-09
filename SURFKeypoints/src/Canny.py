'''
Created on 05.05.2012

@author: Marcus
'''
from ImageProc import ImageProc
if __name__ == '__main__':
    image = ImageProc.getGrayscaleImages(ImageProc.getImage(r'Bilder\Package142.bmp'))
    resultImage = ImageProc.getCanny(image)
    ImageProc.displayImage(image, "nocanny")
    ImageProc.displayImage(resultImage, "canny")
    ImageProc.saveImage(resultImage, r'Bilder\canny.png')