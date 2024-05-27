import cv2

image_path = '/Users/cigrcham/Desktop/CodingWork/Python/image_processing_test/image/origin.png'
I = cv2.imread(image_path)


# cv2.imshow('Origin', I)
# cv2.waitKey()

def to_gray(image_value):
    R, G, B = cv2.split(image_value)
    Ig = 0.39 * R + 0.5 * G + 0.11 * B
    Ig = Ig.astype('uint8')
    return Ig


Ig = to_gray(I)
# cv2.imshow('Gray scale', Ig)
# cv2.waitKey()
#
# max_gray_value = Ig.max()
# print(f'Value gray scale max: {max_gray_value}')
#
Ie = cv2.Canny(Ig, 100, 200)
# cv2.imshow('Canny', Ie)
# cv2.waitKey()

if Ig[326][160]:
    print(f'Pixel at [{326}, {160}] is an edge pixel detected by Canny.')
else:
    print(f'Pixel at [{326}, {160}] is not an edge pixel detected by Canny.')

ret, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

contours, hierarchy = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print('Number of Contours found = ' + str(len(contours)))

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
            cv2.drawContours(I, [contour], -1, (0, 255, 255), 2)

# Display the original image with contours drawn
cv2.imshow('Contours on Original Image', I)
cv2.waitKey(0)
cv2.destroyAllWindows()
