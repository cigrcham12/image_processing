"""
Câu 1:
Sử dụng ngôn ngữ lập trình tùy chọn Python/C+ +/C#/Java, thư viện thị giác máy tính OpenCV, viết chương trình thực hiện yêu câu sau:
Đọc ảnh mầu 104.jpg vào biến ma trận I.
1. (2 điểm) Hiển thị tỷ lệ giữa giá trị độ cao và độ rông của ảnh I.
2. (4 điểm) Hiệu chỉnh lại ảnh I với size mới là độ cao 256, ảnh giữ nguyên tỷ lệ so với ảnh gốc, được ảnh mới 12. Hiến thị ảnh I2.
3. (1 điểm) Chuyển đôi ảnh I sang ảnh HSV được ma trận ảnh Thsv. Hiển thị kênh S của ảnh Ihsv.
4. (1 điểm) Làm trơn kênh S của ảnh Ihsv với bộ lọc median kích thước cửa số 3x3. Biến đổi ngược ảnh Ihsv về biểu diễn mầu RGB được ảnh I3. Hiến thị ảnh 13.
5. (1 điêm) Xác định histogram của kênh S của ănh Ihsv. Ve histogram.
6. (1 điểm) Cân bằng histogram của kênh S của ảnh Ihsv. Biên đôi ngược ảnh Ihsv vê biêu diễn mâu RGB được ảnh 14. Hiển thị ảnh I4.
"""
import cv2
from matplotlib import pyplot as plt

# Câu 1: Đọc ảnh màu 104.jpg vào biến ma trận I
I = cv2.imread('/Users/cigrcham/Desktop/CodingWork/Python/image_processing/image/origin.png')

# Câu 1: Hiển thị tỷ lệ giữa giá trị độ cao và độ rộng của ảnh I
height, width, _ = I.shape
aspect_ratio = height / width
print("Tỷ lệ giữa độ cao và độ rộng của ảnh I:", aspect_ratio)

# Câu 2: Hiệu chỉnh lại kích thước ảnh I với độ cao 256, giữ nguyên tỷ lệ so với ảnh gốc
new_height = 256
new_width = int(width * (new_height / height))
I2 = cv2.resize(I, (new_width, new_height))
cv2.imshow('Image I2', I2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Câu 3: Chuyển đổi ảnh I sang biểu diễn HSV và hiển thị kênh S
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
S_channel = Ihsv[:, :, 1]  # Lấy kênh S (Saturation)
cv2.imshow('S Channel', S_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Câu 4: Làm trơn kênh S của ảnh Ihsv với bộ lọc median kích thước cửa số 3x3
S_blur = cv2.medianBlur(S_channel, 3)
Ihsv[:, :, 1] = S_blur  # Cập nhật lại kênh S trong ảnh Ihsv
I3 = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)  # Chuyển đổi Ihsv về biểu diễn màu RGB
cv2.imshow('Image I3', I3)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Câu 5: Xác định histogram của kênh S của ảnh Ihsv và vẽ histogram
hist_S = cv2.calcHist([S_channel], [0], None, [256], [0, 256])
plt.plot(hist_S)
plt.title('Histogram of S channel')
plt.xlabel('Pixel value')
plt.ylabel('Frequency')
plt.show()

# Câu 6: Cân bằng histogram của kênh S của ảnh Ihsv
equ_S = cv2.equalizeHist(S_channel)
Ihsv[:, :, 1] = equ_S  # Cập nhật lại kênh S trong ảnh Ihsv
I4 = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)  # Chuyển đổi Ihsv về biểu diễn màu RGB
cv2.imshow('Image I4', I4)
cv2.waitKey(0)
cv2.destroyAllWindows()
