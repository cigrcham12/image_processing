# Hien thi anh I
import cv2
import numpy as np

I = cv2.imread('/Users/cigrcham/Desktop/CodingWork/Python/image_processing/image/origin.png')
cv2.imshow('Origin', I)
cv2.waitKey()

# Chuyen anh sang biern dien hsv duoc man tran Ihsv
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
V_Channel = Ihsv[:, :, 2]
cv2.imshow('V channel', V_Channel)
cv2.waitKey()

# Hien thi muc xam lon nhat
max_brightness = np.max(V_Channel)
print("Max brightness vlaue of V channel: ", max_brightness)

# Lam trong anh kenh S cuar Ihsv theo bo loc trung binfh cong kich htuoc cua cuar so lan can laf 5* 5
S_Channel = Ihsv[:, :, 1]
Is = cv2.blur(S_Channel, (5, 5))
cv2.imshow('Blurred Image', Is)
cv2.waitKey()

Is_2 = 255 - Is
ret, Ib = cv2.threshold(Is_2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Otsu Binary", Ib)
cv2.waitKey()

contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
max_contour = max(contours, key=cv2.contourArea)
cv2.drawContours(I, [max_contour], -1, (0, 255, 0), 2)
cv2.imshow('Contour on Image', I)
cv2.waitKey()

# Lấy kênh V
V_Channel = Ihsv[:, :, 2]

# Giãn mức xám cho kênh V
V_Channel_stretched = cv2.equalizeHist(V_Channel)

# Gán lại kênh V đã giãn mức xám vào ảnh
Ihsv[:, :, 2] = V_Channel_stretched

# Chuyển đổi lại thành không gian màu BGR
I_rgb = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)

# Hiển thị ảnh đã tăng độ sáng
cv2.imshow("Enhanced Image", I_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()