'''
Created on 09.03.2012

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
    partialCannyResults = []
    for stack in intervalls:
        partialStacks.append(ImageProc.buildPartialStacks(stack))    
    for partialStack in partialStacks[1]:
        partialResults.append(ImageProc.findHoughMax(partialStack))  
    i = 0
    for partialResult in partialResults:
        partialCannyResults.append(ImageProc.getCanny(partialResult)) 
    resultImage = ImageProc.appendPartialImages(partialResults)
    cannyResultImage = ImageProc.appendPartialImages(partialCannyResults)
    ImageProc.displayImage(cannyResultImage, "res")
    ImageProc.displayImage(resultImage, "res2")
        
        
