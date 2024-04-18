import cv2

path = "/Users/cigrcham/Desktop/CodingWork/Others/image_processing/image/image_origin.png"
path_template = "/Users/cigrcham/Desktop/CodingWork/Others/image_processing/image/image_template.png"

image = cv2.imread(path)
image_template = cv2.imread(path_template)

# Convert images to RGB (OpenCV loads images in BGR format by default)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_template = cv2.cvtColor(image_template, cv2.COLOR_BGR2RGB)

# Choose the matching method (in this case, cv2.TM_CCOEFF)
method = cv2.TM_CCOEFF

# Perform template matching
res = cv2.matchTemplate(image, image_template, method)

# Display the original image and template
cv2.imshow('Original Image', image)
cv2.imshow('Template', image_template)

# Display the result of template matching
cv2.imshow('Matching Result', res)

# Detect
min_val, max_val, min_log, max_log = cv2.minMaxLoc(res)
if method in [cv2.TM_SQDIFF_NORMED, cv2.TM_SQDIFF]:
    top_left = min_log
else:
    top_left = max_log
height, width, channel = image_template.shape

bottom_right = (top_left[0] + width, top_left[1] + height)

# Draw rectangle around the detected region
cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 1)

# Display the image with rectangle
cv2.imshow('Detected Region', image)

# Wait for any key press, close all windows if ESC is pressed
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
