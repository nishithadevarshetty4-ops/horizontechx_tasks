from ultralytics import YOLO
import cv2

# Load a more accurate YOLO model
model = YOLO("yolov8l.pt")
print("object YOLO can detect: ")
print(model.names)

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

# Create resizable window
cv2.namedWindow("Object Detection and Tracking", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    # Detect and track objects
    results = model.track(
        frame,
        persist=True,
        conf=0.25,
        verbose=False
    )

    # Draw bounding boxes, labels, and tracking IDs
    annotated_frame = results[0].plot()

    # Display output
    cv2.imshow("Object Detection and Tracking", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()