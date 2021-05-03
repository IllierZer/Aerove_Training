import cv2 
import math
path=r'/home/illierzer/Downloads/shapes.jpg'
img = cv2.imread(path)
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
(ret,bnw)=cv2.threshold(grayimg,127,255,cv2.THRESH_BINARY)
contours, _ =cv2.findContours(bnw,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
i=0
for contour in contours:
    if i==0:
        i=1
        continue
    approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    cv2.drawContours(img,[contour], 0, (0,0,255))
    M= cv2.moments(contour)
    x=int(M['m10']/M['m00'])
    y=int(M['m01']/M['m00'])
    if len(approx)==3: 
        cv2.putText(img,"Triangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0))
    elif len(approx)==4:
        a,b,w,h=cv2.boundingRect(approx)
        aspectRatio=float(w)/h
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv2.putText(img,"Square",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0))
        else:
            (cx,cy),radius=cv2.minEnclosingCircle(contour)
            center=(int (cx),int (cy))
            radius=int(radius)
            circumr=int(math.sqrt(w*w+h*h))/2
            if abs(radius-circumr)<=3:
                cv2.putText(img,"Rectangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0))
            else:
                cv2.putText(img,"Rhombus",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0))



    
    else:
        a,b,w,h=cv2.boundingRect(approx)
        aspectRatio=float(w)/h
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv2.putText(img,"Circle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0))
        else:
            cv2.putText(img,"Ellipse",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0))
    




img=cv2.resize(img,(0,0),fx=0.5,fy=0.5)
cv2.imshow('detected shapes', img)
cv2.waitKey(0)