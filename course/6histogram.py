import cv2
import numpy as np
import matplotlib.pyplot as plt

fn = '/Users/cigrcham/Desktop/CodingWork/others/image_processing/image/image.jpg'
img = cv2.imread(fn)
cv2.imshow('input image: ', img)
cv2.waitKey(0)

hist = np.zeros((256,), np.uint8)
[w, h] = img.shape[:2]
print('w:', w)  # Corrected concatenation
print('h:', h)  # Corrected concatenation

# Tinh tia tri cua histogram
for i in range(w):
    for j in range(h):
        hist[img[i, j]] += 1  # Corrected pixel value access

# Hien thi bieu do histogram
fig = plt.figure()
plt.plot(hist)
plt.show()