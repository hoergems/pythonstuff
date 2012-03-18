'''
Created on 23.01.2012

@author: Marcus
'''
import math
from math import pi
import cv
import os
import collections
from Filter import Filter
from SURF import SURF
from Loetstellen import Loetstellen

class ImageProc:
    
    def filterMatchesImp(matches):        
        for i in reversed(range(len(matches))): 
            for j in reversed(range(0, i)):                
                if Loetstellen.euklidianDistancePosition(matches[i][0], matches[j][0]) < 5:
                    matches.pop(i)
                    break
        return matches                
                                                
                        
    filterMatches = staticmethod(filterMatchesImp)
    
    def safeMatchesImp(matches):
        coordinates = []
        file = open('keypoints.txt', 'w+')
        for keypoint in matches:            
            coordinates.append(keypoint[0])
        print(coordinates)
        file.writelines(str(coordinates))  
        file.close()       
    safeMatches = staticmethod(safeMatchesImp)
    
    # Gets the image with a specific filename
    def getImageImp(filename):
        image = cv.LoadImage(filename)
        return image 
    getImage = staticmethod(getImageImp)   
    
    # displays an image with a specific name
    def displayImageImp(image, name):
        cv.NamedWindow(name)
        cv.ShowImage(name, image)
        cv.WaitKey()
    displayImage = staticmethod(displayImageImp)      
    
    # Draws the given keypoints into an image  
    def drawKeypointsImp(image, keypoints):
        for ((x, y), laplacian, size, dir, hessian) in keypoints: 
            cv.Circle(image, (int(x),int(y)), 1, cv.RGB(155, 0, 25))           
            cv.Circle(image, (int(x),int(y)), 2, cv.RGB(155, 0, 25))
            cv.Circle(image, (int(x),int(y)), 3, cv.RGB(155, 0, 25))
            cv.Circle(image, (int(x),int(y)), 4, cv.RGB(155, 0, 25))
        return image 
    drawKeypoints = staticmethod(drawKeypointsImp)
    
    def getLaplaceImp(image):
        result = cv.CreateImage(cv.GetSize(image), 8, 1)
        cv.Laplace(image, result, 3)
        return result
    getLaplace = staticmethod(getLaplaceImp)
    
    # Draws the harris corners of a given cornerMap into an image
    def drawHarrisCornersImp(image, cornerMap):        
        for y in range(0, image.height):
            for x in range(0, image.width):
                harris = cv.Get2D(cornerMap, y, x)
                if harris[0] > 10e-06:
                    cv.Circle(image, (x,y), 2, cv.RGB(155, 0, 25))
        return image
    drawHarrisCorners = staticmethod(drawHarrisCornersImp)
    
    def readFilesImp(path):
        images = []
        fileList = os.listdir(path)
        for file in fileList:
            images.append(ImageProc.getImage(str(path) + str(file))) 
        return images           
    readFiles = staticmethod(readFilesImp)
    
    def getGrayscaleImagesImp(images):
        if isinstance(images, collections.Iterable):
            grayscaleImages = []
            for image in images:
                grayscaleImages.append(Filter.getGrayscale(image))
            return grayscaleImages
        else:
            return Filter.getGrayscale(images)
    getGrayscaleImages = staticmethod(getGrayscaleImagesImp)
    
    def getKeypointsImp(grayImages):
        if isinstance(grayImages, collections.Iterable):
            tup = []
            for grayImage in grayImages:
                (keypoint, descriptor) = SURF.getSURF(grayImage)
                tup.append((keypoint, descriptor))
            return tup
        else:
            return SURF.getSURF(grayImages)
    getKeypoints = staticmethod(getKeypointsImp)
    
    def getMatchesImp(tup, (keypointsTemplate, descriptorTemplate)):
        matches = []
        for (keypoint, descriptor) in tup:
            matches.extend(Loetstellen.findMatches((keypoint, descriptor), (keypointsTemplate, descriptorTemplate)))
        return matches
    getMatches = staticmethod(getMatchesImp)
    
    def getContrastImp(image):        
        cLoc = 0
        for i in range(1, image.height - 1):
            for j in range(1, image.width - 1):                               
                cLoc += math.fabs(image[i, j] - (1/4) *  (image[i, j - 1] + image[i - 1, j] + image[i + 1, j] + image[i, j + 1]))
        cLoc = (1.0 / (float(image.width * image.height))) * cLoc
        return cLoc                 
    getContrast = staticmethod(getContrastImp)
    
    def getGaussianImp(image):
        result = cv.CreateImage(cv.GetSize(image), 8, 1)
        cv.Smooth(image, result, cv.CV_GAUSSIAN, 17, 17)
        return result
    getGaussian = staticmethod(getGaussianImp)
    
    def getBinaryImageImp(image, threshold):
        for i in xrange(0, image.height):
            for j in xrange(0, image.width):
                if image[i, j] > threshold:
                    image[i, j] = 255
                else:
                    image[i, j] = 0
        return image
    getBinaryImage = staticmethod(getBinaryImageImp)
    
    def countWhitePixelsImp(image, threshold):
        count = 0
        for i in xrange(image.height):
            for j in xrange(image.width):
                if image[i, j] > threshold:
                    count += 1
        return count
    countWhitePixels = staticmethod(countWhitePixelsImp)
    
    def transformImp(image):
        result = cv.CreateImage(cv.GetSize(image), 8, 1)
        (min, max) = ImageProc.findMinMax(image)
        for i in range(0, image.height):
            for j in range(0, image.width):
                p = (255.0 / float(max-min)) * image[i, j] - (255.0 / (max-min)) * min
                p = int(p)                
                result[i, j] = p
        return result            
    transform = staticmethod(transformImp)
    
    def getCannyImp(images):
        if isinstance(images, collections.Iterable):
            cannyImages = []
            for image in images:
                cannyImages.append(Filter.getCanny(image))
            return cannyImages
        else:
            return Filter.getCanny(images)
            
    getCanny = staticmethod(getCannyImp)
    
    def repairImageImp(image):
        result = cv.CreateImage(cv.GetSize(image), 8, 1)
        mid = ImageProc.getMiddleGrayvalue(image)
        for i in range(0, 2):
            for j in range(0, image.width):
                result[i, j] = mid
        for i in range(2, image.height):
            for j in range(0, image.width):
                result[i, j] = image[i, j]
        for i in range(0, 35):
            for j in range(0, 165):
                result[i, j] = mid
        for i in range(image.height - 35, image.height):
            for j in range(0, 35):
                result[i, j] = mid
        for i in range(image.height - 20, image.height):
            for j in range(image.width - 30, image.width):
                result[i, j] = mid
        return result
    repairImage = staticmethod(repairImageImp)
    
    def getMiddleGrayvalueImp(image):
        (min, max) = ImageProc.findMinMax(image)
        mid = min + 1
        return mid
    getMiddleGrayvalue = staticmethod(getMiddleGrayvalueImp)
    
    
    def findMinMaxImp(image):
        min = 255
        max = 0
        for i in range(0, image.height):
            for j in range(0, image.width):
                if (image[i, j] > max):
                    max = image[i, j]
                if (image[i, j] < min):
                    min = image[i, j]
        return (min, max)  
    findMinMax = staticmethod(findMinMaxImp)  
    
    def saveImageImp(image, filename):
        cv.SaveImage(filename + ".jpg", image)
    saveImage = staticmethod(saveImageImp) 
    
    def buildPartialStacksImp(stack):
        stack1 = []
        stack2 = []
        stack3 = []
        stack4 = []  
        width = cv.GetSize(stack[0])[0] / 2
        height = cv.GetSize(stack[0])[1] / 2 
        for image in stack: 
            result1 = cv.CreateImage((width, height), 8, 1)
            result2 = cv.CreateImage((width, height), 8, 1)
            result3 = cv.CreateImage((width, height), 8, 1)
            result4 = cv.CreateImage((width, height), 8, 1)
            for i in xrange(0, height):
                for j in xrange(0, width):
                    result1[i, j] = image[i, j]
                    result2[i, j] = image[i, j + result1.width]
                    result3[i, j] = image[i + result1.height, j]
                    result4[i, j] = image[i + result1.height, j + result1.width]
            stack1.append(result1)
            stack2.append(result2)
            stack3.append(result3)
            stack4.append(result4)
        return (stack1, stack2, stack3, stack4)
    buildPartialStacks = staticmethod(buildPartialStacksImp)   
    
    def findHoughMaxImp(stack):
        max = 0
        resultImage = 0
        for i in range(0, len(stack)):
            storage = cv.CreateMemStorage(0)
            lines = cv.HoughLines2(ImageProc.getCanny(stack[i]), storage, cv.CV_HOUGH_PROBABILISTIC, 1, pi / 180, 50, 75, 10) 
            if (len(lines) > max):
                max = len(lines)
                resultImage = stack[i]                
        if (type(resultImage) == type(0)):
            return stack[len(stack) / 2]
        else:                               
            return resultImage
    findHoughMax = staticmethod(findHoughMaxImp) 
    
    def appendPartialImagesImp(partialImages):
        width = partialImages[0].width
        height = partialImages[0].height
        result = cv.CreateImage((width * 2, height * 2), 8, 1)
        for i in xrange(0, height):
            for j in xrange(0, width):
                result[i, j] = partialImages[0][i, j]
                result[i, j + width] = partialImages[1][i, j]
                result[i + height, j] = partialImages[2][i, j]
                result[i + height, j + width] = partialImages[3][i, j]
        return result
    appendPartialImages = staticmethod(appendPartialImagesImp)
            
            
            
            
    
    
    
    
