import numpy as np
import cv2
import matplotlib.pyplot as plt


def compute_hist(img):
    hist = np.zeros((256,), np.uint8)
    h, w = img.shape[:2]
    for i in range(h):
        for j in range(w):
            hist[img[i][j]] += 1
    return hist


def equal_hist(hist):
    cumulator = np.zeros_like(hist, np.float64)
    for i in range(1, len(cumulator)):
        cumulator[i - 1] = hist[:i].sum()
    print(cumulator)
    new_hist = (cumulator - cumulator.min()) / (cumulator.max() - cumulator.min()) * 255
    new_hist = np.uint8(new_hist)
    return new_hist


# Set algorithm
origin_image = cv2.imread('/Users/cigrcham/Downloads/image.jpg')
img = cv2.imread('/Users/cigrcham/Downloads/image.jpg', 0)
hist = compute_hist(img=img).ravel()
new_hist = equal_hist(hist=hist)
h, w = img.shape[:2]
for i in range(h):
    for j in range(w):
        img[i, j] = new_hist[img[i, j]]
fig = plt.figure()
ax = plt.subplot(121)
plt.imshow(origin_image, cmap='gray')
plt.subplot(122)
plt.imshow(img, cmap='gray')
plt.show()
