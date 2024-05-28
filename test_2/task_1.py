import cv2
import numpy as np

I = cv2.imread('/Users/cigrcham/Desktop/CodingWork/Python/image_processing/image/origin.png')

# Chuyen anh mau sang anh da cap xam
cv2.imshow('Origin', I)
cv2.waitKey()


def to_gray_luminosity(image):
    R, G, B = cv2.split(image)
    result = R * 0.39 + G * 0.5 + 0.11 * B
    result = result.astype("uint8")
    return result


Ig = to_gray_luminosity(image=I)
cv2.imshow("Ig", Ig)
cv2.waitKey()

max_gray = np.max(Ig)
print('Max value gray: ', max_gray)

# Lay bien cua anh ig theo phuwong phap canny
Ie = cv2.Canny(Ig, 100, 200)
cv2.imshow('Ie', Ie)
cv2.waitKey()

if Ie[326, 160] != 0:
    print(f"Value in [{326}][{160}] is detected by Canny")
else:
    print(f"Value in [{326}][{160}] is not dete"
          f"cted by Canny")

ret, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Binary Image', Ib)
cv2.waitKey()

contours, hierarchy = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print("Number of Contours found: ", str(len(contours)))

max_area = 0
max_area_contour = None

for contour in contours:
    area = cv2.contourArea(contour)
    if area > max_area:
        max_area = area
        max_area_contour = contour

if max_area_contour is not None:
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area / 5.0:
            cv2.drawContours(I, [contour], -1, (0, 255, 255), 2)
cv2.imshow('Contours on Original Image', I)
cv2.waitKey()
