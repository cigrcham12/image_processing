import cv2

image = cv2.imread('/Users/cigrcham/Desktop/CodingWork/others/image_processing/image/img.png')
cv2.imshow('image', image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

blurred = cv2.GaussianBlur(gray, (7, 7), 0)
(T, threshlnv) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow('threshold', threshlnv)

print(('[INFO] otsu \'s thresholding value: {} '.format(T)))
masked = cv2.bitwise_and(image, image, mask=threshlnv)
cv2.imshow('output', masked)
cv2.waitKey(0)
