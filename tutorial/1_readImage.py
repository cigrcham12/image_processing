import cv2

path = "/Users/cigrcham/Desktop/CodingWork/Others/image_processing/image/image.jpg"

img = cv2.imread(path)
cv2.imshow("Read image", img)

cv2.waitKey(1000)

path_save = "/Users/cigrcham/Desktop/CodingWork/Others/image_processing/image/image_save.jpg"
path_save1 = "/Users/cigrcham/Desktop/CodingWork/Others/image_processing/image"

print(cv2.imwrite(path_save, img))