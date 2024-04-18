import cv2

path = "/Users/cigrcham/Desktop/CodingWork/Others/image_processing/image/image.jpg"
image = cv2.imread(path)

B, G, R = cv2.split(image)

cv2.imshow("Origin", image)
cv2.imshow("Blue", B)
cv2.imshow("Green", G)
cv2.imshow("Red", R)

cv2.waitKey()
