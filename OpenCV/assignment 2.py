import cv2
import numpy as np 
path=r'/home/illierzer/Downloads/T.jpeg'
img = cv2.imread(path)
cv2.imshow('original image',img)
rows=img.shape[0]
cols=img.shape[1]

M=np.float32([[1,0,100],[0,1,50]])
t_image1=cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('translated image 1',t_image1)
M=np.float32([[1,0,-100],[0,1,50]])
t_image2=cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('translated image 2',t_image2)
M=np.float32([[1,0,100],[0,1,-50]])
t_image3=cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('translated image 3',t_image3)
M=np.float32([[1,0,-100],[0,1,-50]])
t_image4=cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('translated image 4',t_image4)

R=cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
r_image1=cv2.warpAffine(img,R,(cols,rows))
cv2.imshow('rotated image 1', r_image1)
R=cv2.getRotationMatrix2D((cols/2,rows/2),60,1)
r_image2=cv2.warpAffine(img,R,(cols,rows))
cv2.imshow('rotated image 2', r_image2)

R=cv2.getRotationMatrix2D((cols/2,rows/2),120,1)
r_image3=cv2.warpAffine(img,R,(cols,rows))
cv2.imshow('rotated image 3', r_image3)

R=cv2.getRotationMatrix2D((cols/2,rows/2),220,1)
r_image4=cv2.warpAffine(img,R,(cols,rows))
cv2.imshow('rotated image 4', r_image4)


blur1=cv2.blur(img,(5,5))
cv2.imshow('blurred image 1', blur1)

blur2=cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('blurred image 2', blur2)
cv2.waitKey(0)

