"""
Câu 1:
Sư dụng ngôn ngữ lập trinh tùy chọn Python/C++/C#/Java, thư viện thị giác máy tính OpenCV, viêt chương trinh thực hiện
yêu câu sau:

Đọc ảnh mầu anh5.jpg vào biến ma trận I.
1. (2 điểm) Hiển thị ảnh I.
2. (4 điểm) Chuyển ảnh sang biểu diễn HSV được ma trận Ihsv. Hiển thị kênh V của Ihsv. Xác định giá trị mức sáng lớn
nhất của kênh V của ảnh Ihsv.
3. (1 điểm) Làm trơn ảnh kênh S của Ihsv theo bộ lọc trung bình cộng, kích thước cửa sổ lân cận là 5x5 được ảnh Is.
Hiển thị ảnh Is.
4. (1 điểm) Nhị phân hóa ảnh nghịch đảo của ảnh Is (ảnh nghịch đảo là ảnh; Is 2-255-Is) theo ngưỡng Otsu được ảnh nhị
phân Ib. Hiển thị ảnh Ib.
5. (1 điểm) Xác định đường contour có diện tích lớn nhất của ảnh Ib. Vẽ đường contour trên ảnh gôc I và hiên thị ảnh I.
6. (1 điêm) Tăng độ sáng của kênh V của ảnh Ihsv băng phương pháp giãn mức xám. Biến đối ngược ảnh Ihsv vê biêu diền
mâu RGB được ảnh I. Hiên thị lại ảnh I.
"""
import cv2
import numpy as np

I = cv2.imread('/Users/cigrcham/Desktop/CodingWork/Python/image_processing/image/origin.png')

# Câu 1: Hiển thị ảnh I
cv2.imshow('Image I', I)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Câu 2: Chuyển ảnh sang biểu diễn HSV và hiển thị kênh V
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
V_channel = Ihsv[:, :, 2]  # Lấy kênh V (Value)
max_brightness = np.max(V_channel)
print("Max brightness value of V channel:", max_brightness)
cv2.imshow('V Channel', V_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Câu 3: Làm trơn ảnh kênh S của Ihsv theo bộ lọc trung bình cộng 5x5
# Lấy kênh S (Saturation)
S_channel = Ihsv[:, :, 1]
S_blur = cv2.blur(S_channel, (5, 5))  # Làm trơn ảnh kênh S
cv2.imshow('Blurred S Channel', S_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Câu 4: Nhị phân hóa ảnh nghịch đảo của ảnh Is theo ngưỡng Otsu
# Ảnh nghịch đảo của Is
inv_S_blur = cv2.bitwise_not(S_blur)
ret, Ib = cv2.threshold(inv_S_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Otsu Binary', Ib)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Câu 5: Xác định và vẽ contour có diện tích lớn nhất của ảnh Ib
contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
max_contour = max(contours, key=cv2.contourArea)
cv2.drawContours(I, [max_contour], -1, (0, 255, 0), 2)  # Vẽ contour lớn nhất lên ảnh gốc I
cv2.imshow('Contour on Image', I)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Câu 6: Tăng độ sáng của kênh V bằng phương pháp giãn mức xám
V_channel = Ihsv[:, :, 2]  # Lấy kênh V
V_channel_stretched = cv2.equalizeHist(V_channel)  # Giãn mức xám kênh V
Ihsv[:, :, 2] = V_channel_stretched  # Cập nhật lại kênh V trong ảnh Ihsv
I_rgb = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)  # Chuyển đổi Ihsv về biểu diễn màu RGB
cv2.imshow('Enhanced Image', I_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
