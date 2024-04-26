"""
Câu 1:
Sử dụng ngôn ngữ lập trình tùy chọn Python/C++/C#/Java, thư viện thị giác máy tính OpenCV, viết chương trình thực hiện
yêu câu sau:
Đọc ảnh mầu hat1.png vào biến ma trận I.
1. (2 điểm) Hiển thị ảnh I.
2. (4 điểm) Chuyển ảnh sang biểu diễn HSV được ma trận Ihsv. Hiển thị kênh H của Ihsv. Xác định giá trị mức sáng lớn
nhất của kênh S của ảnh Ihsv.
3. (1 điểm) Xác định và vẽ histogram của kênh V của ảnh Ihsv.
4. (1 điểm) Làm trơn ảnh kênh S của Ihsv theo bộ lọc median, kích thước cửa sổ lân cận là 7x7 được ảnh Is. Hiển thị ảnh
Is.
5. (1 điểm) Nhi phân hóa ảnh nghịch đảo của ảnh Is (ảnh nghịch đảo là: Is_2 = 255 - Is) theo ngường Otsu được ảnh nhị
phân Ib. Hiển thị ảnh Ib.
6. (1 điểm) Xác định đường contour có diện tích lớn nhất của ảnh Ib. Vẽ đường contour trên ảnh gôc I Hiển thị ảnh I.
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Câu 1: Đọc ảnh mầu hat1.png vào biến ma trận I
I = cv2.imread('/Users/cigrcham/Desktop/CodingWork/Python/image_processing_test/image/origin.png')

# Câu 1: Hiển thị ảnh I
cv2.imshow('Image I', I)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Câu 2: Chuyển ảnh sang biểu diễn HSV và hiển thị kênh H
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
H_channel = Ihsv[:, :, 0]  # Lấy kênh H (Hue)
cv2.imshow('Hue Channel', H_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Xác định giá trị mức sáng lớn nhất của kênh S
max_brightness_S = np.max(Ihsv[:, :, 1])
print("Max brightness value of S channel:", max_brightness_S)

# Câu 3: Xác định và vẽ histogram của kênh V
V_channel = Ihsv[:, :, 2]  # Lấy kênh V (Value)
hist_V = cv2.calcHist([V_channel], [0], None, [256], [0, 256])
plt.plot(hist_V)
plt.title('Histogram of V channel')
plt.xlabel('Pixel value')
plt.ylabel('Frequency')
plt.show()

# Câu 4: Làm trơn ảnh kênh S của Ihsv theo bộ lọc median, kích thước cửa sổ lân cận là 7x7
S_channel = Ihsv[:, :, 1]  # Lấy kênh S (Saturation)
S_blur = cv2.medianBlur(S_channel, 7)
cv2.imshow('Blurred S Channel', S_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Câu 5: Nhị phân hóa ảnh nghịch đảo của ảnh Is theo ngưỡng Otsu
inv_S_blur = cv2.bitwise_not(S_blur)  # Ảnh nghịch đảo của Is
ret, Ib = cv2.threshold(inv_S_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Otsu Binary', Ib)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Câu 6: Xác định và vẽ contour có diện tích lớn nhất của ảnh Ib, và vẽ lên ảnh gốc I
contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
max_contour = max(contours, key=cv2.contourArea)
cv2.drawContours(I, [max_contour], -1, (0, 255, 0), 2)  # Vẽ contour lớn nhất lên ảnh gốc I
cv2.imshow('Contour on Image', I)
cv2.waitKey(0)
cv2.destroyAllWindows()
