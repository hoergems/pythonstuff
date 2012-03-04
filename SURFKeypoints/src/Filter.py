'''
Created on 21.01.2012

@author: Marcus
'''
import cv
import math

class Filter:
    
    # Calculates a grayscale image
    def getGrayscaleImp(image):
        grayImage = cv.CreateImage(cv.GetSize(image), 8, 1)
        cv.CvtColor(image, grayImage, cv.CV_BGR2GRAY)
        return grayImage 
    getGrayscale = staticmethod(getGrayscaleImp)
    
    def getHarrisCornersImp(image):
        cornerMap = cv.CreateMat(image.height, image.width, cv.CV_32FC1)        
        cv.CornerHarris(image, cornerMap, 3)        
        return cornerMap
    getHarrisCorners = staticmethod(getHarrisCornersImp)
    
    # Gets the laplacian filtered image. Requires an 8 bit gray image as input
    def getLaplaceImp(image):
        laplace = cv.CreateImage(cv.GetSize(image), cv.IPL_DEPTH_16S, 1)
        grayImage = cv.CreateImage(cv.GetSize(image), 8, 1)
        cv.Laplace(image, laplace)
        cv.ConvertScale(laplace, grayImage, 0.5, 0)
        return grayImage
    getLaplace = staticmethod(getLaplaceImp)
    
    # Gets the canny image. Requires an 8 bit gray image as input
    def getCannyImp(image):
        canny = cv.CreateImage(cv.GetSize(image), 8, 1)
        cv.Canny(image, canny, 25, 50)
        return canny
    getCanny = staticmethod(getCannyImp)       
     