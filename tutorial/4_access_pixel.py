import cv2

path = "/Users/cigrcham/Desktop/CodingWork/Others/image_processing/image/image.jpg"
image = cv2.imread(path)

# px = image[100, 100]
# print(px)


# b = image[:,:,1]
a = image[200:800, 100:500]
image[50: 650, 50: 450] = a

b, g, r = cv2.split(image)

# cv2.imshow("Origin", image)
# cv2.imshow("Space Image", a)
# cv2.imshow("Result", image)
print(image.shape)
print(image.size)
print(image.dtype)

# cv2.imshow("Blue", b)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
