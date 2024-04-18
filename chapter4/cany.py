import cv2

image = cv2.imread('/Users/cigrcham/Desktop/CodingWork/others/image_processing/image/ahsdjkfasdf'.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray, (3, 3), 0)
img_canny = cv2.Canny(img_gaussian, 200, 250)


cv2.imshow('canny', img_canny)
cv2.waitKey()
