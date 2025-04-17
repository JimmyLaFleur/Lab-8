import cv2
import time
from PIL import Image

#Task 1

image_path = r"C:\Users\osnov\Downloads\variant-8.jpg"
image = Image.open(image_path)
width, height = image.size

left = (width - 400) // 2
top = (height - 400) // 2
right = left + 400
bottom = top + 400

cropped_image = image.crop((left, top, right, bottom))

cropped_image_path = r"C:\Users\osnov\Downloads\variant-8(crop).jpg"

cropped_image.save(cropped_image_path)

print("Обрезанное изображение сохранено как", cropped_image_path)

#Task 2

cap = cv2.VideoCapture(0)
down_points = (640, 480)
i = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        if i % 5 == 0:
            a = x + (w // 2)
            b = y + (h // 2)
            print(a, b)
        cv2.line(frame, (a, 500), (a, 0), (0, 0, 0), 5)
        cv2.line(frame, (0, b), (1000, b), (0, 0, 0), 5)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.1)
    i += 1

cap.release()
