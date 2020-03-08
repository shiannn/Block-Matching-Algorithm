import numpy as np
import cv2

trucka = cv2.imread('trucka.bmp')
truckb = cv2.imread('truckb.bmp')

print(trucka.shape)
print(truckb.shape)

#sampleSize = [8,11,15,21,31]
sampleSize = 15

height = trucka.shape[0]
width = trucka.shape[1]
numH = height // sampleSize
if(height % sampleSize != 0):
    numH += 1
numW = width // sampleSize
if(width % sampleSize != 0):
    numW += 1
print(numH, numW)
for i in range(numH):
    for j in range(numW):
        m1 = i*sampleSize
        m2 = (i+1)*sampleSize if ((i+1)*sampleSize < height) else height
        n1 = j*sampleSize
        n2 = (j+1)*sampleSize if ((j+1)*sampleSize < width) else width
        #print(i*sampleSize, (i+1)*sampleSize, j*sampleSize, (j+1)*sampleSize)
        print(m1,m2,n1,n2)
        temp = trucka[m1:m2, n1:n2]
        cv2.line(trucka, (m1,n1), (m2,n1), (0,0,255), 1)
        cv2.line(trucka, (m1,n1), (m1,n2), (0,0,255), 1)

cv2.imshow('My Image', trucka)

# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()