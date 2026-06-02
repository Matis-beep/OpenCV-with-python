import cv2
import numpy as np

img = np.zeros((500, 500, 3), dtype="uint8")

cv2.line(img, (0, 0), (250, 250), (0, 255, 0), 9)

cv2.rectangle(img, (5, 5), (220, 220), (255, 0, 0), -1)

cv2.circle(img, (120, 50), 20, (0, 255, 255), -1)

cv2.putText(img, "Open CV", (50, 50), cv2.FONT_HERSHEY_COMPLEX,
            1, (255, 255, 0), 4)

cv2.imshow("drawings", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

