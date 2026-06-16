


# NIGHT VILLAGE SCENERY

import cv2
import numpy as np

img = np.full((600, 900, 3), (40, 0, 0), dtype = "uint8")

#MOON

cv2.circle(img, (750, 100), 50, (220, 220, 220), -1)

#STARS

stars = [
    (100, 50),
    (150, 100),
    (250, 80),
    (350, 60),
    (500, 120),
    (600, 70),
    (700, 180),
    (820, 50),
    (300, 150),
    (450, 40),
    (550, 170),
    (850, 130)
]

for star in stars:
    cv2.circle(img, star, 3, (255, 255, 255), -1)

# CLOUD 1

cv2.circle(img, (180, 120), 30, (84, 84, 84), -1)
cv2.circle(img, (220, 120), 30, (84, 84, 84), -1)
cv2.circle(img, (260, 120), 30, (84, 84, 84), -1)

# CLOUD 2

cv2.circle(img, (500, 180), 30, (84, 84, 84), -1)
cv2.circle(img, (540, 180), 30, (84, 84, 84), -1)
cv2.circle(img, (580, 180), 30, (84, 84, 84), -1)

#Ground

cv2.rectangle(img, (0, 450), (900, 600), (0, 80, 0), -1)

#Tree1

cv2.rectangle(img, (80, 280), (110, 450), (42, 42, 165), -1)

cv2.circle(img, (96, 240), 50, (0, 120, 0), -1)
cv2.circle(img, (60, 260), 40, (0, 100, 0), -1)
cv2.circle(img, (130, 260), 40, (0, 100, 0), -1)

#Tree2

cv2.rectangle(img, (760, 280), (790, 450), (42, 42, 165), -1)

cv2.circle(img, (775, 240), 50, (0, 120, 0), -1)
cv2.circle(img, (740, 260), 40, (0, 100, 0), -1)
cv2.circle(img, (810, 260), 40, (0, 100, 0), -1)

#Hut
cv2.rectangle(img, (320, 280), (580, 450), (42, 42, 165), -1)

roof = np.array([[290, 280], [450, 150], [610, 280]])
cv2.fillPoly(img, [roof], (19, 69, 139))

#Chimney
cv2.rectangle(img, (520, 180), (550, 260), (70, 70, 70), -1)

#Chimney Smoke

cv2.circle(img, (535, 160), 12, (180, 180, 180), -1)
cv2.circle(img, (555, 130), 18, (200, 200, 200), -1)
cv2.circle(img, (580, 95), 25, (220, 220, 220), -1)#

#Door
cv2.rectangle(img, (430, 350), (490, 450), (0, 0, 0), -1)

#Windows
cv2.rectangle(img, (350, 330), (400, 380), (0, 255, 255), -1)
cv2.rectangle(img, (500, 330), (550, 380), (0, 255, 255), -1)

#Fence

for x in range(0, 901, 40):
    cv2.line(img, (x, 420), (x, 470), (139, 69, 19), 3)

cv2.line(img, (0, 435), (900, 435), (139, 69, 19), 2)
cv2.line(img, (0, 455), (900, 455), (139, 69, 19), 2)

# Sheep 1
cv2.circle(img, (180, 500), 22, (255, 255, 255), -1)
cv2.circle(img, (205, 500), 22, (255, 255, 255), -1)
cv2.circle(img, (192, 480), 22, (255, 255, 255), -1)

cv2.circle(img, (225, 500), 12, (40, 40, 40), -1)

cv2.line(img, (175, 520), (175, 550), (0, 0, 0), 3)
cv2.line(img, (190, 520), (190, 550), (0, 0, 0), 3)
cv2.line(img, (205, 520), (205, 550), (0, 0, 0), 3)
cv2.line(img, (220, 520), (220, 550), (0, 0, 0), 3)

# Sheep 2
cv2.circle(img, (700, 500), 22, (255, 255, 255), -1)
cv2.circle(img, (725, 500), 22, (255, 255, 255), -1)
cv2.circle(img, (712, 480), 22, (255, 255, 255), -1)

cv2.circle(img, (745, 500), 12, (40, 40, 40), -1)

cv2.line(img, (695, 520), (695, 550), (0, 0, 0), 3)
cv2.line(img, (710, 520), (710, 550), (0, 0, 0), 3)
cv2.line(img, (725, 520), (725, 550), (0, 0, 0), 3)
cv2.line(img, (740, 520), (740, 550), (0, 0, 0), 3)

#Camp fire wood

wood1 = np.array([[420, 520], [470, 560], [460, 565], [410, 525]])
wood2 = np.array([[470, 520], [420, 560], [430, 565], [480, 525]])

cv2.fillPoly(img, [wood1], (19, 69, 139))
cv2.fillPoly(img, [wood2], (19, 69, 139))

#Campfire Flame

flame = np.array([[445, 450], [420, 520], [445, 490], [470, 520]])
cv2.fillPoly(img, [flame], (0, 140, 255))

InnerFlame = np.array([[445, 470], [432, 510], [445, 495], [548, 510]])
cv2.fillPoly(img, [InnerFlame], (0, 255, 255))

#Fireflies
fireflies = [
    (120, 300),
    (220, 250),
    (310, 350),
    (620, 320),
    (730, 260),
    (810, 340),
    (540, 280)
]

for fly in fireflies:
    cv2.circle(img, fly, 4, (0, 255, 255), -1)

#Grass
for x in range(0, 900, 10):
    cv2.line(img, (x, 600), (x+3, 590), (0, 255, 0), 1)

cv2.imshow("Night Village Scenery", img)
cv2.waitKey(0)
cv2.destroyAllWindows()