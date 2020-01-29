#drawing lines
import cv2
import numpy as np
def click_event(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        points.append((x,y))
        #cv2.imshow('image',img)
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        if len(points)>=2:
           cv2.line(img1,points[-1],points[-2],(0,255,255),12)
        cv2.imshow('image',img)            
        cv2.imshow('image1',img1)
   
img=np.zeros((512,512,3),np.uint8)
img1=np.zeros((512,512,3),np.uint8)
cv2.imshow('image',img)
points=[]
cv2.setMouseCallback('image',click_event)
k=cv2.waitKey(0)
if k==ord('a'):
    cv2.destroyAllWindows()
