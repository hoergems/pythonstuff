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
    partialLaplaceResults = []
    for stack in intervalls:
        partialStacks.append(ImageProc.buildPartialStacks(stack))    
    for partialStack in partialStacks[1]:
        partialResults.append(ImageProc.findHoughMax(partialStack))  
    i = 0
    print partialResults
    for partialResult in partialResults:
        partialLaplaceResults.append(ImageProc.getLaplace(partialResult))
    resultImage = ImageProc.appendPartialImages(partialResults)
    laplaceResultImage = ImageProc.appendPartialImages(partialLaplaceResults)
    ImageProc.displayImage(laplaceResultImage, "res")
    ImageProc.displayImage(resultImage, "res2")
