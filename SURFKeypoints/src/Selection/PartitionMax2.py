'''
Created on 15.03.2012

@author: Marcus
'''
from ImageProc import ImageProc
import cv
import os
if __name__ == '__main__':
    images = ImageProc.getGrayscaleImages(ImageProc.readFiles("../stack/"))
    resultImages = []    
    stack1 = images[57:70]
    stack2 = images[71:85]
    stack3 = images[86:108] 
    intervalls = [stack1, stack2, stack3]
    partialStacks = []
    partialResults = []
    partialResults2 = []
    partialCannyResults = []
    for stack in intervalls:
        partialStacks.append(ImageProc.buildPartialStacks(stack))    
    for partialStack in partialStacks[1]:       
        partialResults.append(ImageProc.findHoughMax(partialStack)) 
    resultImage = ImageProc.appendPartialImages(partialResults)         
    for partialResult in partialResults:        
        partialCannyResults.append(ImageProc.getCanny(ImageProc.getBinaryImage(partialResult, 65)))
    i = 0    
           
    cannyResultImage = ImageProc.appendPartialImages(partialCannyResults)
    ImageProc.displayImage(resultImage, "res!")
    ImageProc.saveImage(resultImage, "partitionRes")
    ImageProc.displayImage(cannyResultImage, "res")
    ImageProc.saveImage(cannyResultImage, "partitionCannyRes")
    