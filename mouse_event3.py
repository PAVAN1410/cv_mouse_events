# finding colour of a particular pixel 
import cv2
import numpy as np
def click_event(event,x,y,flag,param):
    if event==cv2.EVENT_RBUTTONDOWN:
        img1=np.zeros((512,512,3),np.uint8)
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        img1[:]=[blue,green,red]
        cv2.imshow('imagei',img1)

img=cv2.imread(r'C:\Users\apple.jpg')
#img=np.zeros((512,512,3),np.uint8)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
