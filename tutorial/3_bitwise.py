import cv2

# Load the images
path1 = "/Users/cigrcham/Desktop/CodingWork/Others/image_processing/image/img1.png"
path2 = "/Users/cigrcham/Desktop/CodingWork/Others/image_processing/image/img2.png"

img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

# Crop images to the same shape
min_height = min(img1.shape[0], img2.shape[0])
min_width = min(img1.shape[1], img2.shape[1])

img1_cropped = img1[:min_height, :min_width]
img2_cropped = img2[:min_height, :min_width]

# Perform bitwise AND operation
dest_and = cv2.bitwise_xor(img2_cropped, img1_cropped, mask=None)
dest_not = cv2.bitwise_not(img2_cropped, mask=None)

# Display the images
cv2.imshow("Image 1", img1_cropped)
cv2.imshow("Image 2", img2_cropped)
cv2.imshow("Result", dest_and)
cv2.imshow("Not", dest_not)

# Wait for any key press, close all windows if ESC is pressed
key = cv2.waitKey(0)
if key == 27:  # ASCII value for ESC key
    cv2.destroyAllWindows()
