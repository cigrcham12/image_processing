import cv2

image = cv2.imread('/Users/cigrcham/Desktop/CodingWork/others/image_processing/image/img.png')

cv2.imshow('image', image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

img_gaussian = cv2.GaussianBlur(gray, (3, 3), 0)

img_sobelx = cv2.Sobel(img_gaussian, cv2.CV_8U, 1, 0, ksize=5)
img_sobely = cv2.Sobel(img_gaussian, cv2.CV_8U, 0, 1, ksize=5)

img_sobel = cv2.addWeighted(img_sobelx, 0.5, img_sobely, 0.5, 0)

cv2.imshow('img_sobelx', img_sobelx)
cv2.imshow('img_sobely', img_sobely)

cv2.imshow("img_sobel", img_sobel)

cv2.waitKey(0)
cv2.destroyAllWindows()
