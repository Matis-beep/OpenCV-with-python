import cv2
import numpy as np

img = cv2.imread("face.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayBlur = cv2.GaussianBlur(gray, (9, 9), 2)
detectedCircles = cv2.HoughCircles(
    grayBlur,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=100,
    param1=100,
    param2=40,
    minRadius=30,
    maxRadius=80,
)

if detectedCircles is not None:
    detectedCircles = np.uint16(np.around(detectedCircles))
    for pt in detectedCircles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)
        cv2.circle(img, (a, b), 2, (0, 0, 255), 3)

cv2.imshow("detected circles", img)
cv2.waitKey(0)
cv2.destroyAllWindows()