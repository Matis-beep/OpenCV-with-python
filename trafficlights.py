import cv2
import numpy as np

img=np.zeros((500,500,3),dtype="uint8")

cv2.rectangle(img, (180,50),(320,410),(100,100,100), -1)

cv2.circle(img,(250,120),40, (0,0,255), -1)
cv2.circle(img,(250,230),40, (0,255,255),-1)
cv2.circle(img,(250,340),40, (0,255,0),-1)

cv2.imshow("traffic light", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
