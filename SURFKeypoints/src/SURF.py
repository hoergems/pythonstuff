'''
Created on 23.01.2012

@author: Marcus
'''
import math
import cv 

class SURF:
    
    # calculates the euklidian distance between two keypoint vectors
    def euklidianDistanceImp(keypoint1, keypoint2):
        dist = float(0) 
        try:            
            for i in range(2, len(keypoint1)):
                dist += (float(keypoint1[i]) - float(keypoint2[i]))**2
            return math.sqrt(dist)
        except: 
            return 100.0;
            print("Exception")
    euklidianDistance = staticmethod(euklidianDistanceImp)
    
    # Finds the best match of a keypoint in a collection of keypoints
    def findBestMatchImp(keypoint, keypoints):
        match = None
        if (len(keypoints) > 0):
            match = keypoints[0]
        for key in keypoints:
            if (type(key) is tuple and type(keypoint) is tuple):
                dist = SURF.euklidianDistance(key, keypoint)
                if (dist < SURF.euklidianDistance(match, keypoint)):
                    match = key
            else:
                print("wat")
        return match
    findBestMatch = staticmethod(findBestMatchImp)
    
    # Finds the match of a keypoint in a collection of keypoints
    def findMatchImp(keypoint, keypoints):                           
        bestMatch = SURF.findBestMatch(keypoint, keypoints)
        keypoints.remove(bestMatch)        
        secondMatch = SURF.findBestMatch(keypoint, keypoints)        
        dist1 = SURF.euklidianDistance(bestMatch, keypoint) 
        dist2 = SURF.euklidianDistance(secondMatch, keypoint)
        if (dist2 == 0.0):
            dist2 = 0.000001        
        return bestMatch       
        return None
    findMatch = staticmethod(findMatchImp)
    
    # Gets the matching keypoints in an image for the keypoints in a template
    def getMatchingKeypointsImp(keypointsImage, keypointsTemplate):
        matches = []               
        for key in keypointsTemplate:
            match = SURF.findMatch(key, keypointsImage)
            if (match != None):
                matches.append(match)                    
        return matches
    getMatchingKeypoints = staticmethod(getMatchingKeypointsImp)    
    
    def getSURFImp(image):
        return cv.ExtractSURF(image, None, cv.CreateMemStorage(), (0, 500, 3, 1))
    getSURF = staticmethod(getSURFImp)
    
    getSURF = staticmethod(getSURFImp)