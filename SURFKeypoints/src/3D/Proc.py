'''
Created on 17.04.2012

@author: Marcus
'''

class Proc:
    def getBoundaryBox(self, x, y, z, raw):
        result = [[[0 for _ in xrange(z[0], z[1])] for _ in xrange(y[0], y[1])] for _ in xrange(x[0], x[1])]
        for i in xrange(x[0], x[1]):
            for j in xrange(y[0], y[1]):
                for k in xrange(z[0], z[1]):
                    result[i][j][k] = self.getValue(i, j, k, raw)
        return result
    
    def getValue(self, x,y,z, raw):
        index = 2*x + 400*y + 196800*z
        return self.toValue((raw[index], raw[index+1]))
    
    def setValue(x,y,z, value):
        #index = 2*x + 2*200*y + 2*200*492*z
        index = 2*x + 400*y + 196800*z
        bytes = toBytes(value)
        raw[index] = bytes[1]
        raw[index+1] = bytes[0]
    
    def toValue(self, s):
        ''' s entspricht den beiden Bytezeichen '''        
        bin1 = self.addZeros(self.bin(ord(s[0])))
        bin2 = self.addZeros(self.bin(ord(s[1])))        
        return int(bin2 + bin1, 2)
    
    def toBytes(decN):
        binN = self.addZeros(self.bin(decN), 16)  # Adde 0en bis str-laenge = 16
        return chr(int("".join(list(binN )[0:8]), 2)), chr(int("".join(list(binN )[8:17]), 2))   # returnt die beiden Bytes als Zeichen

    
    def addZeros(self, s, max=8):
        return s if len(s) >= max else self.addZeros('0' + s, max)
    
    def bin(self, s):
        return str(s) if s<=1 else self.bin(s>>1) + str(s&1)
    