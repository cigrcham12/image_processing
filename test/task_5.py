import cv2
import matplotlib.pyplot as plt

# Doc anh
I = cv2.imread('/Users/cigrcham/Desktop/CodingWork/Python/image_processing/image/origin.png')
# Hien thi do cao va do rong cua anh
height, width, color = I.shape

print('Do cao ', height)
print('Do rong', width)
aspect_ratio = height / width
print('Ty le giua do cao va do rong cua anh I: ', aspect_ratio)

cv2.imshow('Origin', I)
cv2.waitKey()
# Hieu chinh lai kich thuoc cua anh I voi do cao laf 256

new_height = 256
new_width = int(width * (new_height / height))
I2 = cv2.resize(I, (new_width, new_height))
cv2.imshow("Image I2", I2)
cv2.waitKey()

# Chuyen doi anh I sang HSv duco ma tran anh ihsv hien thi kenh S
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
S_Channel = Ihsv[:, :, 1]
cv2.imshow("S channel", S_Channel)
cv2.waitKey()

#  Lam tron kenh S cua anh Ihsv voi bo loc meidan kich thuoc cua so 3 * 3. Bien doi nguoc anh Ihsv  ve bieu dien max RGB duocj aanh I3
S_blur = cv2.medianBlur(S_Channel, 3)
Ihsv[:, :, 1] = S_blur  # Cập nhật lại kênh S trong ảnh Ihsv
I3 = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)  # Chuyển đổi Ihsv về biểu diễn màu RGB
cv2.imshow('Image I3', I3)
cv2.waitKey(0)

# Xac dinh historgram cua kenh S cuar Ihsv va ve historgram

hist_S = cv2.calcHist([S_Channel], [0], None, [256], [0, 256])
plt.plot(hist_S)
plt.title('Histogram of S channel')
plt.xlabel('Pixel value')
plt.ylabel("Frequency")
plt.show()

euq_S = cv2.equalizeHist(S_Channel)
Ihsv[:, :, 1] = euq_S
I4 = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
cv2.imshow('Image I4', I4)
cv2.waitKey()

hist_S = cv2.calcHist([euq_S], [0], None, [256], [0, 256])
plt.plot(hist_S)
plt.title('Histogram of S channel')
plt.xlabel('Pixel value')
plt.ylabel("Frequency")
plt.show()
