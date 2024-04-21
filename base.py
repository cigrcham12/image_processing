import numpy
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('/Users/cigrcham/Desktop/CodingWork/Python/image_processing_test/image/origin.png')

while 1:
    cv2.imshow('origin', img)
    if cv2.waitKey(20) & 0xff == 27:
        break

# origin_image = cv2.imread('/Users/cigrcham/Downloads/image.jpg')
# img = cv2.imread('/Users/cigrcham/Downloads/image.jpg', 0)
# hist = compute_hist(img=img).ravel()
# new_hist = equal_hist(hist=hist)
# h, w = img.shape[:2]
# for i in range(h):
#     for j in range(w):
#         img[i, j] = new_hist[img[i, j]]
# fig = plt.figure()
# ax = plt.subplot(121)
# plt.imshow(origin_image, cmap='gray')
# plt.subplot(122)
# plt.imshow(img, cmap='gray')
# plt.show()
