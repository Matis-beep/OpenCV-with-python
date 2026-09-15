import cv2
import numpy as np



img = cv2.imread('boat.jpg')
kernel3=np.ones((3,3),np.uint8)
erosion3=cv2.erode(img,kernel3)

kernel5=np.ones((5,5),np.uint8)
erosion5=cv2.erode(img,kernel5)

kernel7=np.ones((7,7),np.uint8)
erosion7=cv2.erode(img,kernel7)

kernel9=np.ones((9,9),np.uint)
erosion9=cv2.erode(img,kernel9)

cv2.imshow("3x3 erosion",erosion3)
cv2.imshow("5x5 Erosion",erosion5)
cv2.imshow("7x7 Erosion",erosion7)
cv2.imshow("9x9 erosion",erosion9)

cv2.waitKey(0)
cv2.destroyAllWindows()