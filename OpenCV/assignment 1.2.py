import cv2
cap=cv2.VideoCapture(0) #the arguement is basically the device index (0 means the webcam, if there was more than one camera so arg would be 1 for the second camera and so on)
while(True):
    (ret,frame)=cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1)==ord('q'):   # ord('q') return the unicode of q and waitKey(1) returns a 32 bit integer corresponding to the pressed key
        break
cap.release()
cv2.destroyAllWindows()

# waitKey(1) will display a frame for exactly 1ms and then close that frame and the next loop will open a new display frame hence giving a continuous feed
