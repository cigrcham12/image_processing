"""Câu 1: Sử dụng ngôn ngữ lập trình tùy chọn Python/C++/C#/Java, thư viện thị giác máy tính OpenCV, viết chương
trình thực hiện yêu câu sau:

Đọc ảnh mầu hat1.png vào biến ma trận I.
1. (2 điểm) Hiển thị kênh B của ảnh I.
2. (4 điểm) Chuyển ảnh sang biểu diễn HSV được ma trận Ihsv. Hiển thị kênh H của Thsv. Xác định giá trị mức sáng trung
bình của kênh S của ảnh Ihsv.
3. (1 điểm) Xác định và vẽ histogram của kênh S của ảnh Ihsv.
4. (1 điểm) Làm trơn ảnh kênh V của Ihsv theo bộ lọc trung bình cộng, kích thước cửa sổ lân cận là 3x3 được ảnh Is.
Hiển thị ảnh Is.
5. (1 điểm) Nhị phân hóa ảnh Is theo ngưỡng Otsu được ảnh nhị phân Ib. Hiển thị ảnh Ib. Vẽ đường contour đó trên ảnh
góc I. Hiển thị ảnh I.

6. Xác định đường contour có tỷ lệ giữa chu vi và diện tích là lớn nhất của anh Ib. Vẽ đường contour đó trên ảnh gốc I. HIển thị ảnh I
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

I = cv2.imread('/Users/cigrcham/Desktop/CodingWork/Python/image_processing/image/origin.png')
cv2.imshow('Origin', I)

# 1. (2 điểm) Hiển thị kênh B của ảnh I.
cv2.imshow("Channel B", I[:, :, 0])

# 2. (4 điểm) Chuyển ảnh sang biểu diễn HSV được ma trận Ihsv. Hiển thị kênh H của Thsv. Xác định giá trị mức sáng trung
# bình của kênh S của ảnh Ihsv.

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
H_channel = Ihsv[:, :, 0]  # Lấy kênh H (Hue)
cv2.imshow('Hue Channel', H_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Xác định giá trị mức sáng trung bình của kênh S
mean_S = np.mean(Ihsv[:, :, 1])
print("Mean brightness of S channel:", mean_S)

# 3. (1 điểm) Xác định và vẽ histogram của kênh S của ảnh Ihsv.
S_channel = Ihsv[:, :, 1]  # Lấy kênh S (Saturation)
hist_S = cv2.calcHist([S_channel], [0], None, [256], [0, 256])
plt.plot(hist_S)
plt.title('Histogram of S channel')
plt.xlabel('Pixel value')
plt.ylabel('Frequency')
plt.show()

# 4. (1 điểm) Làm trơn ảnh kênh V của Ihsv theo bộ lọc trung bình cộng, kích thước cửa sổ lân cận là 3x3 được ảnh Is.
# Hiển thị ảnh Is.
V_channel = Ihsv[:, :, 2]  # Lấy kênh V (Value)
V_blur = cv2.blur(V_channel, (3, 3))  # Làm trơn ảnh kênh V
cv2.imshow('Blurred V Channel', V_blur)

# 5. (1 điểm) Nhị phân hóa ảnh Is theo ngưỡng Otsu được ảnh nhị phân Ib. Hiển thị ảnh Ib. Vẽ đường contour đó trên ảnh
# góc I. Hiển thị ảnh I.
ret, Ib = cv2.threshold(V_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Otsu Binary', Ib)

while 1:
    if cv2.waitKey(20) & 0xff == 27:
        cv2.destroyAllWindows()


# Tìm và vẽ đường contour có tỷ lệ giữa chu vi và diện tích lớn nhất trên ảnh gốc I
contours, _ = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
max_ratio = 0
max_contour = None

for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    area = cv2.contourArea(contour)
    if area > 0:
        ratio = perimeter / area
        if ratio > max_ratio:
            max_ratio = ratio
            max_contour = contour

if max_contour is not None:
    cv2.drawContours(I, [max_contour], -1, (0, 255, 0), 2)

cv2.imshow('Contour Image', I)
cv2.waitKey(0)

cv2.destroyAllWindows()
#
# import cv2
# import matplotlib.pyplot as plt
# import numpy as np
#
# I = cv2.imread('/Users/cigrcham/Desktop/CodingWork/Python/image_processing/image/origin.png')
# cv2.imshow('Origin', I)
# cv2.waitKey()
#
# Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
# H_Channel = Ihsv[:, :, 0]
#
# cv2.imshow("H channel", H_Channel)
# cv2.waitKey()
#
# print('Max S channel Ihsv', np.mean(Ihsv[:, :, 1]))
#
# # Hien  av ve histogram cuar S
# S_Channel = cv2.calcHist([Ihsv[:, :, 1]], [0], None, [256], [0, 256])
# plt.plot(S_Channel)
# plt.title("Histogram of S channel")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()
#
# Is = cv2.blur(Ihsv[:, :, 2], (3, 3))
# cv2.imshow('Is', Is)
# cv2.waitKey()
#
# ret, Ib = cv2.threshold(Is, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# cv2.imshow('Otsu Binary', Ib)
# cv2.waitKey()
#
# # Vẽ đường contour lên ảnh gốc I
# contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(I, contours, -1, (0, 255, 0), 2)
# cv2.imshow('Contours on original image', I)
# cv2.waitKey(0)
#
# # Câu 6
# # Xác định đường contour có tỷ lệ giữa chu vi và diện tích là lớn nhất
# max_ratio = 0
# max_contour = None
# for contour in contours:
#     perimeter = cv2.arcLength(contour, True)
#     area = cv2.contourArea(contour)
#     if area != 0:
#         ratio = perimeter / area
#         if ratio > max_ratio:
#             max_ratio = ratio
#             max_contour = contour
#
# # Nếu tỷ lệ lớn hơn 0 (tức là có ít nhất một contour được tìm thấy)
# if max_contour is not None:
#     # Vẽ đường contour lên ảnh gốc I
#     cv2.drawContours(I, [max_contour], -1, (0, 0, 255), 2)
#     cv2.imshow('Contours with max perimeter-to-area ratio', I)
#     cv2.waitKey(0)
# else:
#     print("Không tìm thấy contour nào.")
#
# cv2.destroyAllWindows()
#
