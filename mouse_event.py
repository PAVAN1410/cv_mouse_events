import cv2
import numpy as np
#events=[i for i in dir(cv2) if 'EVENT' in i]
#print(events)
def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,' , ',y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        strXY=str(x)+' , '+str(y)
        cv2.putText(img,strXY,(x,y),font,0.6,(0,255,0),2)
        cv2.imshow('image',img)
    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font=cv2.FONT_HERSHEY_SIMPLEX
        str_BGR=str(blue)+' , '+str(red)+' , '+str(green)
        cv2.putText(img,str_BGR,(x,y),font,0.4,(0,0,255),2)
        cv2.imshow('image',img)
        
#img=np.zeros((512,512,3),np.uint8)
#img=cv2.imread(r'C:\Users\nanin\Desktop\opencv\opencv-master\samples\data\apple.jpg')
img=cv2.imread(r'C:\Users\nanin\Desktop\CV\opencv\opencv-master\samples\data\messi5.jpg')
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
k=cv2.waitKey(0)
if k==ord('a'):
   cv2.destroyAllWindows()
