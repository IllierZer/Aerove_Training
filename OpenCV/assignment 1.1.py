import cv2
path=r'/home/illierzer/Downloads/colour.jpg'
img=cv2.imread(path)
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #returns a grayscale image
(thresh,bnw)=cv2.threshold(grayimg,127,255,cv2.THRESH_BINARY)   #the command on the RHS returns a tuple containing the value of the threshold as the first entry and the image as the second entry
cv2.imshow('black and white image',bnw)
cv2.imshow('grayscale image',grayimg)
cv2.imshow('original image',img)
cv2.waitKey(0)
