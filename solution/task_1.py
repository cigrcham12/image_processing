import cv2
import numpy as np

# Câu 1: Sử dụng ngôn ngữ lập trình tùy chọn Python/C+ +/C#/Java, thư viện thị giác máy tính OpenCV, viêt chương
# trinh thực hiện yêu cầu sau:

# Đọc ảnh mầu anh5.jpg vào biến ma trận I.
# 1. (2 điểm) Hiển thị ảnh I.

# 2. (4 điểm) Chuyển ảnh mầu I sang ảnh đa cấp xám (grayscale) theo công thức xác định mức độ xám từ tổ hợp các thành
# phần mầu (r,g,b) theo tỷ lệ (0.39,0.5,0.11), được ma trận ảnh Ig. Hiển thị ảnh Ig. Xác định mức xám lớn nhất của
# ảnh 1g.

# 3. (1 điểm) Lấy biên của ảnh Ig theo phương pháp Canny được ảnh biên le là ảnh nhị phân nền đen. Hiền thị ảnh le.

# 4. (1 điểm) Kiểm tra pixel có tọa độ dòng y=160, cột x=326 có là điểm biên của ảnh Ig theo phép dò biên
# Canny không?

# 5. (1 điệm) Nhị phân ảnh Ig theo ngưỡng Otsu được ảnh nhị phân nền đen được ảnh Ib. Hiển thị ảnh Ib.

# 6. (1 điêm) Xác định các đường contour của ảnh Ib, tìm giá trị max area là diện tích lớn nhất trong các con our
# tren. Ve cac contours có diện tích > max _area/5.0 lên ảnh gốc I với mầu vàng bgr = (0,255,255).

# 1. (2 điểm) Hiển thị ảnh I.
image = cv2.imread('/Users/cigrcham/Desktop/CodingWork/Python/image_processing_test/image/origin.png')

while 1:
    cv2.imshow('origin', image)
    if cv2.waitKey(20) & 0xff == 27:
        break

# 2. (4 điểm) Chuyển ảnh mầu I sang ảnh đa cấp xám (grayscale) theo công thức xác định mức độ xám từ tổ hợp các thành
# phần mầu (r,g,b) theo tỷ lệ (0.39,0.5,0.11),

# def to_gray(I):
#     Ig = 0.39 * I[:, :, 2] + 0.5 * I[:, :, 1] + 0.11 * I[:, :, 0]
#     Ig = Ig.astype('uint8')
#     return Ig

# gray_image = to_gray(image)

gray_image = cv2.transform(image, np.array([[0.39, 0.5, 0.11]]))
while 1:
    cv2.imshow('origin', gray_image)
    if cv2.waitKey(20) & 0xff == 27:
        break

# 3. (1 điểm) Lấy biên của ảnh Ig theo phương pháp Canny được ảnh biên le là ảnh nhị phân nền đen. Hiển thị ảnh le.
edges = cv2.Canny(gray_image, 100, 200)

while 1:
    cv2.imshow('Edges', edges)
    if cv2.waitKey(20) & 0xff == 27:
        break

# 4. (1 điểm) Kiểm tra pixel có tọa độ dòng y=160, cột x=326 có là điểm biên của ảnh Ig theo phép dò biên
# Canny không?
if edges[160, 326] != 0:
    print("Pixel at (y=160, x=326) is an edge pixel detected by Canny.")
else:
    print("Pixel at (y=160, x=326) is not an edge pixel detected by Canny.")

# 5. (1 điệm) Nhị phân ảnh Ig theo ngưỡng Otsu được ảnh nhị phân nền đen được ảnh Ib. Hiển thị ảnh Ib.
ret, ib = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

while 1:
    cv2.imshow('Binary Image (Otsu)', ib)
    if cv2.waitKey(20) & 0xff == 27:
        break

# 6. (1 điêm) Xác định các đường contour của ảnh Ib, tìm giá trị max area là diện tích lớn nhất trong các con our
# tren. Ve cac contours có diện tích > max _area/5.0 lên ảnh gốc I với mầu vàng bgr = (0,255,255).
# Find contours in the binary image
contours, _ = cv2.findContours(ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize variables to store maximum area and corresponding contour
max_area = 0
max_area_contour = None

# Find the contour with the maximum area
for contour in contours:
    area = cv2.contourArea(contour)
    if area > max_area:
        max_area = area
        max_area_contour = contour

# Draw contours with areas greater than max_area/5.0 on the original image
if max_area_contour is not None:
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area / 5.0:
            cv2.drawContours(image, [contour], -1, (0, 255, 255), 2)

# Display the original image with contours drawn
cv2.imshow('Contours on Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
