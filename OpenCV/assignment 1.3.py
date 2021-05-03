import cv2
import numpy as np
path=r'/home/illierzer/Downloads/anonymous.jpeg'
img=cv2.imread(path)
cv2.imshow('original image',img)
modified_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_red=np.array([30,150,50])
upper_red=np.array([255,255,180])
mask=cv2.inRange(modified_img,lower_red,upper_red)
img[mask>0]=(255,0,0)
cv2.imshow('red to blue',img)
cv2.waitKey(0)


#we converted the original image colorspace BGR to another color space HSV and then we set a range within which a color is qualified to be called red
#then we checked the modified image (the HSV one) for HSV values within the range and stored the 1s (if in range) and 0s(if not in range) in the array mask
#now we set the indices corresponding to mask values 1 in the original image to (255,0,0) that is all blue
