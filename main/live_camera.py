import cv2
from ultralytics import YOLO
path = r'C:\Users\Intern-Tech\Documents\Sign language detection YOLO\dataset\runs\detect\train2\weights\best.pt' 
model = YOLO(path)
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)
    annotated_frame = results[0].plot()
    cv2.imshow("Sign Language Detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
