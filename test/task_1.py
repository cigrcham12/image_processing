import cv2

path = '/Users/cigrcham/Desktop/CodingWork/Python/image_processing/image/origin.png'
I = cv2.imread(path)

cv2.imshow('Origin', I)
cv2.waitKey()


def to_gray_scale(image_value):
    R, G, B = cv2.split(image_value)
    image_process = 0.39 * R + 0.5 * G + 0.11 * B
    image_process = image_process.astype("uint8")
    return image_process


Ig = to_gray_scale(I)
cv2.imshow('GrayScale', Ig)
cv2.waitKey()

max_gray = 0
for row in Ig:
    for pixel in row:
        if pixel > max_gray:
            max_gray = pixel

print("Mức xám lớn nhất:", max_gray)


# 3. (1 điểm) Lấy biên của ảnh Ig theo phương pháp Canny được ảnh biên le là ảnh nhị phân nền đen. Hiền thị ảnh le.
# cv2.Canny(image_value, 100, 200):
#
# image_value: Ảnh đầu vào.
# 100: Ngưỡng dưới, các điểm ảnh có gradient nhỏ hơn 100 sẽ bị loại bỏ.
# 200: Ngưỡng trên, các điểm ảnh có gradient lớn hơn 200 sẽ được coi là cạnh mạnh.
def image_canny(image_value):
    return cv2.Canny(image_value, 100, 200)


Ie = image_canny(Ig)
cv2.imshow('Canny', Ie)
cv2.waitKey()


# Kiểm tra xem pixel có toạ đọ dòng y = 160, x = 326 có là điểm biên của ...
def check_pixel_canny(image_value, x, y):
    if image_value[x, y] != 0:
        print(f"Pixel at [{x}, {y}] is an edge pixel detected by Canny.")
    else:
        print(f"Pixel at [{x}, {y}] is not an edge pixel detected by Canny.")


check_pixel_canny(
    image_value=Ie,
    x=326,
    y=160
)

# Ig: Ảnh đầu vào ở dạng grayscale.
# 0: Giá trị ngưỡng ban đầu (không cần thiết vì Otsu sẽ tự động xác định ngưỡng).
# 255: Giá trị tối đa được sử dụng để thay thế cho các giá trị lớn hơn ngưỡng (thường là 255 cho ảnh nhị phân).
# cv2.THRESH_BINARY + cv2.THRESH_OTSU: Sử dụng phân ngưỡng nhị phân kết hợp với phương pháp Otsu để tự động xác định ngưỡng.
# ret: Giá trị ngưỡng được tìm thấy bởi phương pháp Otsu.
# Ib: Ảnh đầu ra sau khi phân ngưỡng (ảnh nhị phân).

ret, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

while 1:
    cv2.imshow('Binary Image (Otsu)', Ib)
    if cv2.waitKey(20) & 0xff == 27:
        break

# 6. (1 điêm) Xác định các đường contour của ảnh Ib, tìm giá trị max area là diện tích lớn nhất trong các con our
# tren. Ve cac contours có diện tích > max _area/5.0 lên ảnh gốc I với mầu vàng bgr = (0,255,255).

# ❑Contour (chu tuyến): là một đường cong nối tất cả các
# điểm liên tục (dọc theo đường biên), có cùng màu sắc
# hoặc cường độ.
# ❑ Contour hữu ích trong phân tích hình dạng, tìm kích
# thước của đối tượng quan tâm và phát hiện đối tượng.
# ❑ Các bước thực hiện:
# ➢ B1: Đọc ảnh, chuyển sang ảnh đa cấp xám;
# ➢ B2: Tìm biên (làm nổi biên) ảnh;
# ➢ B3: Tìm contour;
# ➢ B4: Vẽ các contour tìm được trên ảnh

# contours, hierarchy = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# print('Number of Contours found: ' + str(len(contours)))

# max_area = 0
# max_area_contour = None
#
# for contour in contours:
#     area = cv2.contourArea(contour)
#     if area > max_area:
#         max_area = area
#         max_area_contour = contour
#
# if max_area_contour is not None:
#     for contour in contours:
#         area = cv2.contourArea(contour)
#         if area > max_area / 5.0:
#             cv2.drawContours(I, [contour], -1, (0, 255, 255), 2)
#
# cv2.imshow('Contours on Origin Image', I)
# cv2.waitKey(0)

contours, hierarchy = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print('Number of Contours found: ' + str(len(contours)))

max_area = 0
max_area_contour = None

for contour in contours:
    area = cv2.contourArea(contour)
    if area > max_area:
        max_area = area
        max_area_contour = contour

if max_area_contour is not None:
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area / 5.0:
            cv2.drawContours(I, [contour], -1, (0, 255, 255), 2)

cv2.imshow('Contours on Origin Image', I)
cv2.waitKey()
print('Number of Contours found' + str(len(contours)))
