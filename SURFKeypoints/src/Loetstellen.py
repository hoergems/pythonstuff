'''
Created on 25.01.2012

@author: Marcus
'''
import math
from SURF import SURF
from Filter import Filter

class Loetstellen:    
    
    def findMatchesImp((keypointsImage, descriptorsImage), (keypointsTemplate, descriptorsTemplate)):
        matches = []
        for i in range(0, len(keypointsTemplate)):
            for j in range(0, len(keypointsImage)):
                if (Loetstellen.euklidianDistance(descriptorsTemplate[i], descriptorsImage[j]) < 0.45):
                    matches.append(keypointsImage[j])        
        return matches                    
    findMatches = staticmethod(findMatchesImp)
    
    def euklidianDistanceImp(keypoint1, keypoint2):
        dist = float(0) 
        try:            
            for i in range(0, len(keypoint1)):
                dist += (float(keypoint1[i]) - float(keypoint2[i]))**2
            dist2 = math.sqrt(dist)
            return dist2            
        except: 
            return 100.0;
            print("Exception")
    euklidianDistance = staticmethod(euklidianDistanceImp)
    
    def euklidianDistancePositionImp(position1, position2):        
        return math.sqrt((position1[0] - position2[0])**2 + (position1[1] - position2[1])**2)
    euklidianDistancePosition = staticmethod(euklidianDistancePositionImp)
        
            
    
    
    
