import cv2
import matplotlib.pyplot as plt
import numpy as np

I = cv2.imread('/Users/cigrcham/Desktop/CodingWork/Python/image_processing/image/origin.png')
cv2.imshow('Origin', I)
cv2.waitKey()
# chuyen sang Hsv sa Ihsv

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("Channel H", Ihsv[:, :, 0])
cv2.waitKey()

print("Mean value of S channel", np.mean(Ihsv[:, :, 1]))

S_Channel = Ihsv[:, :, 1]
hist_S = cv2.calcHist([S_Channel], [0], None, [256], [0, 256])
plt.plot(hist_S)
plt.title("Histogram of S Channel")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()

V_Channel = Ihsv[:, :, 2]
Is = cv2.blur(V_Channel, (3, 3))
cv2.imshow("Blurred", Is)
cv2.waitKey()

ret, Ib = cv2.threshold(Is, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Is', Is)
cv2.waitKey()

contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

max_ratio = 0
max_contour = None

for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    area = cv2.contourArea(contour)
    if area != 0:
        ratio = perimeter / area
        if ratio > max_ratio:
            max_ratio = ratio
            max_contour = contour

if max_contour is not None:
    cv2.drawContours(I, [max_contour], -1, (0, 0, 255), 2)
    cv2.imshow('Final', I)
    cv2.waitKey()
