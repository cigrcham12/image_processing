"""
Sử dụng ngôn ngữ lập trình tuỷ chọn C++/Python, ...
"""
import cv2
import numpy as np

# Đọc ảnh  và hiển thị ảnh
I = cv2.imread('/Users/cigrcham/Desktop/CodingWork/Python/image_processing/image/origin.png')
cv2.imshow('Origin', I)
cv2.waitKey()

# Chuyển ảnh sang biểu diện HSV được mà trần Ihsv
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)

# Hien thi kenh V cuar anh Ihsv
V_Channel = Ihsv[:, :, 2]
cv2.imshow('V_Channel', V_Channel)
cv2.waitKey()

# xac dinh muc xam lon nhat cuar kenh v cuar anh ihsv

max_brightness = np.max(V_Channel)
print("Max brightness value of V channel", max_brightness)

#  Cau 3: Lafm tron anh kenh S cuar Ihsv theo bo loc trung binfh cong , kich thuowcs cuar cuar so lan can laf 5* 5
# duowjc anh Is

S_Channel = Ihsv[:, :, 1]
S_bulr = cv2.blur(S_Channel, (5, 5))
cv2.imshow("Blurred S channel", S_bulr)
cv2.waitKey()

# Nhi phan hoa anh nghich dao cua anh IS theo nguowng Otsu dduwojc anh nhin phan Ib
inv_S_blur = cv2.bitwise_not(S_bulr)
ret, Ib = cv2.threshold(inv_S_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Otsu Binary', Ib)
cv2.waitKey()

contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
max_contour = max(contours, key=cv2.contourArea)
cv2.drawContours(I, [max_contour], -1, (0, 255, 0), 2)
cv2.imshow('Contour on Image', I)
cv2.waitKey(0)

# Tăng độ sáng của kênh V bằng phương pháp giãn mức xám
V_channel = Ihsv[:, :, 2]  # Lấy kênh V
V_channel_stretched = cv2.equalizeHist(V_channel)  # Giãn mức xám kênh V
Ihsv[:, :, 2] = V_channel_stretched  # Cập nhật lại kênh V trong ảnh Ihsv

# Chuyển đổi Ihsv về biểu diễn màu RGB
I_rgb = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)

# Hiển thị ảnh đã tăng độ sáng
cv2.imshow('Enhanced Image', I_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()