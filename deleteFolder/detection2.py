import cv2
import numpy as np

img = cv2.imread('img1.png',1)
cv2.imshow('Original',img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('img3.png',0)
cv2.imshow('Template',template)
w,h = template.shape[0], template.shape[1]

matched = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8

loc = np.where( matched >= threshold)

for pt in zip(*loc[::-1]):
   cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow('Matched with Template',img)
cv2.waitKey(0)