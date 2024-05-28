# Hien thi anh
import cv2
import matplotlib.pyplot as plt
import numpy as np

I = cv2.imread('/Users/cigrcham/Desktop/CodingWork/Python/image_processing/image/origin.png')

cv2.imshow('Origin', I)
cv2.waitKey()

# Chuyen sang ihsv
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
H_Channel = Ihsv[:, :, 0]
cv2.imshow("S_Channel", H_Channel)
cv2.waitKey()

max_S_channel = np.max(Ihsv[:, : 1])
print("Max value H channel", max_S_channel)

V_Channel = Ihsv[:, :, 2]
hist_V = cv2.calcHist(V_Channel, [0], None, [256], [0, 256])
plt.plot(hist_V)
plt.xlabel('Histogram of V channel')
plt.ylabel("Frequency")
plt.show()

#  Lam tron anh S theo bo loc medidan kich thuocj 7*7 duoc anh Is.
S_Channel = Ihsv[:, :, 1]
Is = cv2.medianBlur(S_Channel, 7)
cv2.imshow("Blurred S channel", Is)
(cv2.waitKey())

Is_2 = cv2.bitwise_not(Is)
ret, Ib = cv2.threshold(Is_2, 0, 255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Otsu Binary", Ib)
cv2.waitKey()

contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
max_contour = max(contours, key=cv2.contourArea)
cv2.drawContours(I, [max_contour], -1, (0, 255, 0) , 2)
cv2.imshow("Contour on Image", I)
cv2.waitKey()


