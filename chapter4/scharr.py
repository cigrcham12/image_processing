import cv2

image = cv2.imread('/Users/cigrcham/Desktop/CodingWork/others/image_processing/image/img.png')

cv2.imshow('image', image)

scharrx = cv2.Scharr(image, cv2.CV_64F, 1, 0)
scharry = cv2.Scharr(image, cv2.CV_64F, 0, 1)

cv2.imshow("Scharr X", scharrx)
cv2.imshow("Scharr Y", scharry)

cv2.waitKey()
cv2.destroyWindow()
