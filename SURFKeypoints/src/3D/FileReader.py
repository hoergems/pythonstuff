'''
Created on 17.04.2012

@author: Marcus
'''
import time

class FileReader:
    def loadData(self):
        start = time.time()
        print "Loading",
        p1 = "Data//WLAN2"
        p2 = " - Original"
        p3 = ".raw"
        file = open(p1 + p2 + p3, 'rb')
        raw = list(file.read())
        file.close
        print "done: Needed %ss" % (time.time() - start) 
        return raw
