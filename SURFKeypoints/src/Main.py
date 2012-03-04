'''
Created on 22.01.2012

@author: Marcus
'''
import copy
import Filter

from SURF import SURF
from Filter import Filter
from ImageProc import ImageProc
from Loetstellen import Loetstellen

def main():
    
    # Read images from dir
    images = ImageProc.readFiles("Images/")
    
    # The result image
    resultImage = ImageProc.getImage(r'Images\Package142.bmp')
    
    # Image6 serves as an example image
    image6 = ImageProc.getImage(r'Images\Package142.bmp')
    
    # The template
    template = ImageProc.getImage(r'Images\Loetstelle2.bmp')
    
    # Convert the images to grayscale images
    grayImages = ImageProc.getGrayscaleImages(images) 
    
    # Convert the template to a grayscale image
    templateGray = ImageProc.getGrayscaleImages(template)
    
    # Calculate the keypoints and descriptors of the grayscale images
    keypointsImages = ImageProc.getKeypoints(grayImages)
    
    # Calculate the keypoints and descriptors of the grayscale template
    (keypointsTemplate, descriptorTemplate) = ImageProc.getKeypoints(templateGray)
    
    # Get the matching keypoints in the grayscale images for every keypoint in the grayscale template
    matches = ImageProc.filterMatches(ImageProc.getMatches(keypointsImages, (keypointsTemplate, descriptorTemplate)))   
    
    print ("Anzahl d. Loetstellen: " + str(len(matches)))    
    (keypoints6, desc6) = keypointsImages[5]
    
    # Draws the keypoints in the resulting images
    keypointsImage1 = ImageProc.drawKeypoints(image6, keypoints6)
    keypointsImage2 = ImageProc.drawKeypoints(template, keypointsTemplate)
    matchingKeypointsImage = ImageProc.drawKeypoints(resultImage, matches)
    ImageProc.safeMatches(matches)    
    #ImageProc.safeMatches(matches)
    
    # Displays the resulting images
    ImageProc.displayImage(ImageProc.getImage(r'Images\Package142.bmp'), 'image')
    ImageProc.displayImage(keypointsImage1, 'key1')
    ImageProc.displayImage(keypointsImage2, 'key2')
    ImageProc.displayImage(matchingKeypointsImage, 'matches')
if __name__ == '__main__':     
    main() 
        
    