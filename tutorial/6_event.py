import cv2


def drawCircle(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 10, (0, 0, 255), -1)


path = "/Users/cigrcham/Desktop/CodingWork/Others/image_processing/image/image.jpg"
img = cv2.imread(path)
cv2.namedWindow('image')
cv2.setMouseCallback('image', drawCircle)
while 1:
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xff == 27:
        break
cv2.waitKey()
