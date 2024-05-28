import cv2
import numpy as np

I = cv2.imread('/Users/cigrcham/Desktop/CodingWork/Python/image_processing/image/origin.png')
cv2.imshow('Origin', I)
cv2.waitKey()

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
V_Channel = Ihsv[:, :, 2]
cv2.imshow('V Channel', V_Channel)
cv2.waitKey()

print("Max value V_Channel: ", np.max(V_Channel))

S_Channel = Ihsv[:, :, 1]
Is = cv2.blur(S_Channel, (5, 5))
cv2.imshow("Blurred S channel", Is)
cv2.waitKey()

Is_2 = cv2.bitwise_not(Is)
ret, Ib = cv2.threshold(Is_2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("IB", Ib)
cv2.waitKey()

contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

max_contour = max(contours, key=cv2.contourArea)
cv2.drawContours(I, [max_contour], -1, (0, 255, 0), 2)
cv2.imshow('Contour on Image', I)
cv2.waitKey()

V_Channel_stretched = cv2.equalizeHist(V_Channel)
Ihsv[:, :, 2] = V_Channel_stretched
I_rgb = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
cv2.imshow('I rgb', I_rgb)
cv2.waitKey()
