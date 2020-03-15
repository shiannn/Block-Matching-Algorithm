import numpy as np
import cv2
import sys
import math

def SAD(m,n,u,v,frame1,frame2,sampleSize,height,width):
    if(legal(m,n,height,width)==0
    or legal(m+sampleSize,n,height,width)==0
    or legal(m,n+sampleSize,height,width)==0
    or legal(m+sampleSize,n+sampleSize,height,width)==0):
        #print('illegal')
        return None
    if(legal(m+u,n+v,height,width)==0
    or legal(m+u+sampleSize,n+v,height,width)==0
    or legal(m+u,n+v+sampleSize,height,width)==0
    or legal(m+u+sampleSize,n+v+sampleSize,height,width)==0):
        #print('illegal')
        return None
    ret = 0
    for i in range(sampleSize):
        for j in range(sampleSize):
            """
            temp2 = int(frame2[m+i,n+j])
            temp1 = int(frame1[m+u+i,n+v+j])
            #ret += abs(frame2[m+i,n+j] - frame1[m+u+i,n+v+j])
            ret += abs(temp2 - temp1)
            """
            ret += abs(int(frame2[m+i,n+j][0])-int(frame1[m+u+i,n+v+j][0]))+abs(int(frame2[m+i,n+j][0])-int(frame1[m+u+i,n+v+j][0]))+abs(int(frame2[m+i,n+j][0])-int(frame1[m+u+i,n+v+j][0]))

    return ret

def legal(m,n,height,width):
    if m < 0 or m > height:
        return 0
    if n < 0 or n > width:
        return 0
    else:
        return 1

def BlockMatch(imageA, imageB, sampleSize):
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
            cv2.line(truckb, (m1,n1), (m2,n1), (0,0,255), 1)
            cv2.line(truckb, (m1,n1), (m1,n2), (0,0,255), 1)

#ret = SAD(30,30,6,6,trucka,truckb,sampleSize,height,width)
#print(ret)

if __name__ == '__main__':
    #trucka = cv2.imread('trucka.bmp', cv2.IMREAD_GRAYSCALE)
    #truckb = cv2.imread('truckb.bmp', cv2.IMREAD_GRAYSCALE)

    trucka = cv2.imread('trucka.bmp')
    truckb = cv2.imread('truckb.bmp')

    print(trucka.shape)
    print(truckb.shape)

    #sampleSize = [8,11,15,21,31]
    #sampleSize = 15
    sampleSize = int(input('sample size [9,11,15,21,31]: '))
    height = trucka.shape[0]
    width = trucka.shape[1]
    numH = height // sampleSize
    if(height % sampleSize != 0):
        numH += 1
    numW = width // sampleSize
    if(width % sampleSize != 0):
        numW += 1
    print(numH, numW)

    #Threshold search range 50 => W = 50

    #W = 5
    W = int(input('search range: '))

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
            cv2.line(truckb, (m1,n1), (m2,n1), (0,0,255), 1)
            cv2.line(truckb, (m1,n1), (m1,n2), (0,0,255), 1)

            minSumDis = 2147483647
            minU = None
            minV = None
            for u in range(-W,W+1):
                for v in range(-W,W+1):
                    ret = SAD(m1,n1,u,v,trucka,truckb,sampleSize,height,width)
                    if(ret == None):
                        pass
                    else:
                        if(ret < minSumDis):
                            minSumDis = ret
                            minU = u
                            minV = v
            print('u,v',minU, minV)
            if minU!=None and minV!=None:
                vecLen = math.ceil((minU**2 + minV**2)**(1/2))
                length = sampleSize-1
                st = ((m1+m2)//2,(n1+n2)//2)
                if(vecLen == 0):
                    ed = (st[0], st[1])
                else:
                    ed = (st[0]+length*minU//vecLen, st[1]+length*minV//vecLen)
                print('st',st)
                print('ed',ed)
                #cv2.line(trucka, st, ed, (0,255,0), 5)
                cv2.arrowedLine(trucka, st, ed, (0,255,0), 1)

    filename = str(sampleSize)+'x'+str(sampleSize)+'_W'+str(W)+'.jpg'
    cv2.imwrite(filename,trucka)
"""
    cv2.imshow('My Image', trucka)

    # 按下任意鍵則關閉所有視窗
    cv2.waitKey(0)
    cv2.destroyAllWindows()
"""
"""
    cv2.imshow('My Image', truckb)

    # 按下任意鍵則關閉所有視窗
    cv2.waitKey(0)
    cv2.destroyAllWindows()
"""