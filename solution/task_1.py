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
image = cv2.imread('/Users/cigrcham/Desktop/CodingWork/Python/image_processing/image/origin.png')

cv2.imshow('Origin', image)
cv2.waitKey()

# 2. (4 điểm) Chuyển ảnh mầu I sang ảnh đa cấp xám (grayscale) theo công thức xác định mức độ xám từ tổ hợp các thành
# phần mầu (r,g,b) theo tỷ lệ (0.39,0.5,0.11),

"""
Have three methods to convert iamge to grayscale: 
* Lightness: Lấy giá trị trung bình của các thành phần có giấ trị cao nhất và thấp nhất: 
* Average(Trung bình): Lấy giá trị trung bình của 3 thành phần đó(R, G, B) làm giá tị thang độ xám
* Luminosity: Lấy giá trị trung bình có trọng số của các thành phần
"""


# Luminosity
def to_gray_luminosity(image_value):
    R, G, B = cv2.split(image_value)
    Ig = 0.39 * R + 0.5 * G + 0.11 * B
    Ig = Ig.astype("uint8")
    return Ig


def to_gray_2_luminosity(image_value):
    transformation_matrix = np.array([[0.39, 0.5, 0.11]])
    Ig = cv2.transform(image_value, transformation_matrix)
    Ig = Ig.astype("uint8")
    return Ig


def to_gray_lightness(image_value):
    R, G, B = cv2.split(image_value)
    Ig = (np.maximum(R, np.maximum(G, B)) + np.minimum(R, np.minimum(G, B))) / 2
    Ig = Ig.astype("uint8")
    return Ig


def to_gray_average(image_value):
    R, G, B = cv2.split(image_value)
    Ig = np.mean([R, G, B], axis=0)
    Ig = Ig.astype("uint8")
    return Ig


Ig = to_gray_average(image)
cv2.imshow('Gray scale', Ig)
cv2.waitKey()

# 3. (1 điểm) Lấy biên của ảnh Ig theo phương pháp Canny được ảnh biên Ie là ảnh nhị phân nền đen. Hiển thị ảnh le.
"""
    * Canny là một phương pháp bao gồm nhiều giai đoạn để phát hiện một loạt các cạnh trong hình ảnh
    * Các bước của thuật toán Canny:
- Giảm nhiễu(Gaussion, trung bình, trung vị, ...)
- Tính toán Gradient độ xám của ảnh(nhân chập với mặt nạ Sobel)
- Làm mỏng biên( Non-manimum suppression)
- Ngưỡng kép(Double threshold)
- Theo dõi cạnh bằng độ trễ( Edge Tracking by Hytesis)
"""


def image_canny(image_value):
    return cv2.Canny(image_value, 100, 200)


Ie = image_canny(Ig)
cv2.imshow('Canny', Ie)
cv2.waitKey()


# 4. (1 điểm) Kiểm tra pixel có tọa độ dòng y=160, cột x=326 có là điểm biên của ảnh Ig theo phép dò biên Canny không?
def check_pixel_canny(image_value, x, y):
    print(image_value[x, y])
    # Check if the pixel value is non-zero, indicating an edge pixel detected by Canny
    if image_value[x, y] != 0:
        print(f"Pixel at [{x}, {y}] is an edge pixel detected by Canny.")
    else:
        print(f"Pixel at [{x}, {y}] is not an edge pixel detected by Canny.")
    # # Fill color red for the pixel at position (x, y)
    # modified_image = image_value.copy()
    # modified_image[x, y] = (0, 0, 255)
    # cv2.imshow('Check', modified_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


check_pixel_canny(
    image_value=Ie,
    x=326,
    y=160
)

# 5. (1 điệm) Nhị phân ảnh Ig theo ngưỡng Otsu được ảnh nhị phân nền đen được ảnh Ib. Hiển thị ảnh Ib.
ret, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

while 1:
    cv2.imshow('Binary Image (Otsu)', Ib)
    if cv2.waitKey(20) & 0xff == 27:
        break

# 6. (1 điêm) Xác định các đường contour của ảnh Ib, tìm giá trị max area là diện tích lớn nhất trong các con our
# tren. Ve cac contours có diện tích > max _area/5.0 lên ảnh gốc I với mầu vàng bgr = (0,255,255).

# Find contours in the binary image
contours, hierarchy = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print('Number of Contours found = ' + str(len(contours)))
#
# cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
# cv2.imshow('Contours', image)
# cv2.waitKey(0)

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

# while 1:
#     cv2.imshow('Edges', image)
#     if cv2.waitKey(20) & 0xff == 27:
#         cv2.destroyAllWindows()
#         break
