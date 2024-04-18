import cv2

image = cv2.imread('/Users/cigrcham/Desktop/CodingWork/others/image_processing/image/img.png')

cv2.imshow('image', image)
# Phát hiện biên bằng phương pháp Laplace

# scharrx = cv2.Scharr(image, cv2.CV_64F, 1, 0)
# scharry = cv2.Scharr(image, cv2.CV_64F, 0, 1)
#
# cv2.imshow('Scharr X', scharrx)
# cv2.imshow('Scharr Y', scharry)
# cv2.waitKey()
# cv2.destroyWindow()

ddepth = cv2.CV_16S

kernel_size = 3

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray, (3, 3), 0)
img_laplace = cv2.Laplacian(img_gaussian, ddepth, ksize=kernel_size)

img_laplace = cv2.convertScaleAbs(img_laplace)

cv2.imshow('img_laplace', img_laplace)
cv2.waitKey(0)
cv2.destroyAllWindows()
