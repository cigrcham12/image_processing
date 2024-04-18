import cv2
import numpy as np

image = cv2.imread('/Users/cigrcham/Desktop/CodingWork/others/image_processing/image/img.png')

cv2.imshow('image', image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

img_gaussian = cv2.GaussianBlur(gray, (9, 9), 0)
print(type(img_gaussian))  # Thêm dấu ngoặc đơn sau 'type'
print((img_gaussian))  # Thêm dấu ngoặc đơn sau 'type'

kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])

img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)

img_prewitt = cv2.addWeighted(img_prewittx, 0.5, img_prewitty, 0.5, 0)  # Thay đổi phép cộng thành phép trọng số

cv2.imshow("prewitt_x", img_prewittx)
cv2.imshow("prewitt_y", img_prewitty)

cv2.imshow("prewitt", img_prewitt)
cv2.waitKey(0)  # Thêm đối số 0 cho đến khi một phím bất kỳ được nhấn
cv2.destroyAllWindows()  # Đóng tất cả các cửa sổ khi thoát