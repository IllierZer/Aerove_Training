import cv2 
def dodgeV2(x,y):
    return cv2.divide(x,y,scale=256)

cap=cv2.VideoCapture(0)
while(True):
    (ret,frame)=cap.read()
    grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    smooth=cv2.GaussianBlur(grayimg,(21,21),sigmaX=0,sigmaY=0)
    sketch=dodgeV2(grayimg,smooth)
    cv2.imshow('sketched video',sketch)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()



