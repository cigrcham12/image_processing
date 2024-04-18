import cv2

path = "/Users/cigrcham/Desktop/CodingWork/Others/image_processing/image/image.jpg"
img = cv2.imread(path)

# start_point = (0, 0)
# end_point = (1900, 100)
# color = (0, 0, 255)
# thickness = 7
#
# img = cv2.line(
#     img=img,
#     pt1=start_point,
#     pt2=end_point,
#     color=color,
#     thickness=thickness
# )

# center = (100, 100)
# radius = 60
# color = (0, 0, 255)
# thickness = 6
# img = cv2.circle(
#     img=img,
#     center=center,
#     radius=radius,
#     color=color,
#     thickness=thickness
# )


# start_point = (40, 40)
# end_point = (150, 650)
# color = (0, 0, 255)
# thickness = 6
#
# img = cv2.rectangle(
#     img=img,
#     pt1=start_point,
#     pt2=end_point,
#     color=color,
#     thickness=thickness
# )

# font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
# org = (30, 30)
# font_scale = 1
# color = (0, 0, 255)
# thickness = 3
# img = cv2.putText(
#     img=img,
#     text="Hello World",
#     fontScale=font_scale,
#     org=org,
#     fontFace=font,
#     color=color,
#     thickness=thickness
# )

cv2.imshow("image", img)
cv2.waitKey()
