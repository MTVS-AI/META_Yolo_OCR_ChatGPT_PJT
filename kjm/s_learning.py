import cv2
from ultralytics import YOLO

model = YOLO('yolov8s.pt')

# cap = cv2.VideoCapture(0)

# while cap.isOpened():
#     ret, frame = cap.read()

#     if ret:
#         results = model.track(frame, persist=True)
#         frame = results[0].plot()

#     cv2.imshow('tracking', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

model = YOLO("C:/Users/user/Desktop/yolo8_tracking/best.pt")
results = model.track(source='https://www.youtube.com/watch?v=E818sv8-Pao',show=True)
