'''
Created on 17.04.2012

@author: Marcus
'''
from FileReader import FileReader
from Proc import Proc

if __name__ == '__main__':
    reader = FileReader()
    proc = Proc()
    raw = reader.loadData()
    print "Painting ...",
    boundary = proc.getBoundaryBox([0, 20], [0, 20], [0, 20], raw)
    
    print "Done!",
                            