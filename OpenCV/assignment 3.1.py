import cv2 
def dodgeV2(x,y):
    return cv2.divide(x,y,scale=256)   #dividing the grayscale image by the inverse of the blurred image to highlight the boldest edges

path=r'/home/illierzer/Downloads/colour.jpg'
img=cv2.imread(path)
cv2.imshow('Original Image',img)
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

smooth=cv2.GaussianBlur(grayimg,(21,21),sigmaX=0,sigmaY=0)
sketch=dodgeV2(grayimg,smooth)
cv2.imshow('Sketch',sketch)

cv2.waitKey(0)


