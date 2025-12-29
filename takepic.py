import cv2
import os
import time

labels = ['hello', 'thanks', 'iloveyou', 'yes', 'no']
images_per_label = 15
capture_interval = 2  # seconds
dataset_dir = "dataset"

# Create folders
for label in labels:
    os.makedirs(os.path.join(dataset_dir, label), exist_ok=True)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access webcam")
    exit()

print("Press 'q' to quit early.")

for label in labels:
    print(f"\nCollecting images for '{label}'")
    time.sleep(3)

    count = 0
    last_capture_time = time.time()

    while count < images_per_label:
        ret, frame = cap.read()
        if not ret:
            break

        # Make a COPY for display only
        display_frame = frame.copy()

        # Draw text ONLY on display frame
        cv2.putText(display_frame,
                    f"Label: {label} ({count+1}/{images_per_label})",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2)

        cv2.imshow("Sign Language Data Collection", display_frame)

        current_time = time.time()
        if current_time - last_capture_time >= capture_interval:
            img_path = os.path.join(dataset_dir, label, f"{label}_{count}.jpg")

            # Save ORIGINAL frame (no text)
            cv2.imwrite(img_path, frame)

            print(f"Saved: {img_path}")
            count += 1
            last_capture_time = current_time

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            exit()

print("\nDone collecting data!")

cap.release()
cv2.destroyAllWindows()
