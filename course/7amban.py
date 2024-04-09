import cv2

img = cv2.imread('/Users/cigrcham/Desktop/CodingWork/others/image_processing/image/image.jpg')
cv2.imshow('image origin: ', img)
cv2.waitKey()

# [w, h] = img.shape[:2]
# for i in range(w):
#     for j in range(h):
#         img[i][j] = 255 - img[i][j]

img = 255 - img

cv2.imshow('result', img)
cv2.waitKey()