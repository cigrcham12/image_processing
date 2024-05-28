import cv2
import matplotlib.pyplot as plt
import numpy as np

# Đọc ảnh màu
I = cv2.imread('/Users/cigrcham/Desktop/CodingWork/Python/image_processing/image/origin.png')

# Hiển thị kênh B của ảnh I
B_channel = I[:, :, 0]
cv2.imshow('B Channel', B_channel)
cv2.waitKey(0)

# Chuyển ảnh sang biểu diễn HSV
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)

# Hiển thị kênh H của Ihsv
H_channel = Ihsv[:, :, 0]
cv2.imshow('H Channel', H_channel)
cv2.waitKey(0)

# Tính giá trị mức sáng trung bình của kênh S của ảnh Ihsv
S_channel = Ihsv[:, :, 1]
mean_S = np.mean(S_channel)
print('Giá trị mức sáng trung bình của kênh S:', mean_S)

# Vẽ histogram của kênh S của ảnh Ihsv
plt.hist(S_channel.ravel(), bins=256, range=[0, 256])
plt.title('Histogram of S Channel')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()

# Làm trơn ảnh kênh V của Ihsv theo bộ lọc trung bình cộng, kích thước cửa sổ lân cận là 3x3
V_channel = Ihsv[:, :, 2]
Is = cv2.blur(V_channel, (3, 3))

# Hiển thị ảnh Is
cv2.imshow('Smoothed V Channel', Is)
cv2.waitKey(0)

# Nhị phân hóa ảnh Is theo ngưỡng Otsu
_, Ib = cv2.threshold(Is, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Hiển thị ảnh nhị phân Ib
cv2.imshow('Binary Image Ib', Ib)
cv2.waitKey(0)

# Vẽ đường contour trên ảnh gốc I
contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Tìm đường contour có tỷ lệ giữa chu vi và diện tích lớn nhất
max_ratio = 0
best_contour = None

for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    area = cv2.contourArea(contour)
    if area > 0:  # Tránh chia cho 0
        ratio = perimeter / area
        if ratio > max_ratio:
            max_ratio = ratio
            best_contour = contour

# Vẽ đường contour tốt nhất trên ảnh gốc
if best_contour is not None:
    cv2.drawContours(I, [best_contour], -1, (0, 255, 0), 2)

# Hiển thị ảnh gốc với contour
cv2.imshow('Image with Best Contour', I)
cv2.waitKey(0)
cv2.destroyAllWindows()
