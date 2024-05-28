import cv2
import numpy as np

I = cv2.imread('/Users/cigrcham/Desktop/CodingWork/Python/image_processing/image/origin.png')
cv2.imshow('Origin', I)
cv2.waitKey()

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("V Channel", Ihsv[:, :, 1])
cv2.waitKey()
print('Max value channel V: ', np.max(Ihsv[:, :, 2]))

Is = cv2.blur(Ihsv[:, :, 1], (5, 5))
cv2.imshow('Is', Is)
cv2.waitKey()

Is_2 = cv2.bitwise_not(Is)
ret, Ib = cv2.threshold(Is_2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Ib', Ib)
cv2.waitKey()

contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
max_contour = max(contours, key=cv2.contourArea)

cv2.drawContours(I, [max_contour], -1, (0, 255, 0), 2)
cv2.imshow("Contour", I)
cv2.waitKey()

V_Channel = Ihsv[:, :, 2]
V_Channel_stretched = cv2.equalizeHist(V_Channel)
Ihsv[:, :, 2] = V_Channel_stretched
I_rgb = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
cv2.imshow("I brighten", I_rgb)
cv2.waitKey()
