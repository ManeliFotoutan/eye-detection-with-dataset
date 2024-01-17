from ultralytics import YOLO
import cv2
import cvzone  # Assuming you have the cvzone library installed
import math

# Set up the video capture
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Load YOLO model
model = YOLO("best.pt")

# Define the class names for YOLO model
className = ["eye"]

# Main loop for capturing and processing frames
while True:
    # Read a frame from the camera
    success, img = cap.read()

    # Run YOLO on the frame and get detection results
    results = model(img, stream=True)

    # Process each detection result
    for r in results:
        boxes = r.boxes

        # Process each bounding box in the result
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1

            # Draw a rectangle around the detected object
            cv2.rectangle(img, (x1, y1), (x2, y2), (225, 0, 225), 3)

            # Get confidence and class label for the detection
            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])

            # Display class name and confidence on the image
            cvzone.putTextRect(img, f'{className} {conf}',
                               (max(0, x1), max(35, y1)), scale=2, thickness=3,
                               colorB=(255, 0, 255), colorT=(225, 225, 225), colorR=(255, 0, 255))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    # Display the processed image
    cv2.imshow("Image", img)

    # Wait for a key event (1 millisecond delay)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()