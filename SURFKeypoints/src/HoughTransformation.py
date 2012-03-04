__author__ = 'Lixe'

from math import pi
import cv

img = cv.LoadImage('H:\down2\Jojo\pcb2_01.bmp', 1)

cv.NamedWindow('original')
cv.ShowImage('original', img)
cv.WaitKey()

#cv.Smooth(img, img, cv.CV_GAUSSIAN, 5, 5);
gray = cv.CreateImage(cv.GetSize(img), 8, 1)
cv.CvtColor(img, gray, cv.CV_BGR2GRAY)

edge = cv.CreateImage(cv.GetSize(img), 8, 1)
cv.Canny(gray, edge, 25, 50)

cv.NamedWindow('canny')
cv.ShowImage('canny', edge)
cv.WaitKey()

storage = cv.CreateMemStorage(0)
lines = cv.HoughLines2(edge, storage, cv.CV_HOUGH_PROBABILISTIC, 1, pi / 180, 50, 75, 10)
for line in lines:
    cv.Line(img, line[0], line[1], cv.CV_RGB(0, 255, 0), 2, 8)

cv.NamedWindow('lines')
cv.ShowImage('lines', img)
cv.WaitKey()

storage = cv.CreateMat(1, gray.width, cv.CV_32FC3)
cv.HoughCircles(gray, storage, cv.CV_HOUGH_GRADIENT, 1, 10, 25, 50, 8, 30)

for i in xrange(storage.cols):
    x, y, r = storage[0,i]
    print 'circle #%i | x = %f, y = %f, r = %f' % (i, x, y, r)
    cv.Circle(img, (int(x), int(y)), int(r), cv.CV_RGB(255, 0, 0), 2, 8)

cv.NamedWindow('circles')
cv.ShowImage('circles', img)
cv.WaitKey()