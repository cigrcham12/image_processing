import cv2

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()

frame = ""

for i in range(10):
    _, frame = cap.read()

if frame is None:
    print("Error: Could not read frame.")
    cap.release()
    exit()

frame = cv2.resize(frame, (640, 480))
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (25, 25), 0)
last_frame = gray

while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (25, 25), 0)

    abs_img = cv2.absdiff(last_frame, gray)
    last_frame = gray

    _, img_mask = cv2.threshold(abs_img, 30, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(img_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 900:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imshow("frame", frame)
    cv2.imshow("img_mask", img_mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()