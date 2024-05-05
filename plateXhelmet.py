import torch
import cv2
import numpy as np
import os
from pathlib import Path
import easyocr
from ultralytics import YOLO

# Model paths
helmet_model_path = "/home/saadlockholmes/Videos/Helmet Detection/best (2).pt"
numberplate_model_path = "best.pt"  # Custom model path

# Load YOLOv5 helmet detection model
helmet_model = YOLO(helmet_model_path)
helmet_names = helmet_model.names

# Load YOLOv5 number plate detection model
numberplate_model = torch.hub.load('ultralytics/yolov5', 'custom', path=numberplate_model_path, force_reload=True)

# Choose device: "cpu" or "cuda" (if CUDA is available)
cpu_or_cuda = "cpu"
device = torch.device(cpu_or_cuda)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

video_path = "/home/saadlockholmes/Videos/automatic-number-plate-recognition-main/Shout hero bike entry video  shout super ster bike rideing it's RIDER BOY @itsriderboy.mp4"

# Capture video from webcam
cap = cv2.VideoCapture(video_path)
# cap = cv2.VideoCapture(0)
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Output video writer
video_writer = cv2.VideoWriter("object_cropping_output_with_numberplate.avi",
                               cv2.VideoWriter_fourcc(*'mp4v'),
                               fps, (w, h))

crop_dir_name = "ultralytics_crop"
if not os.path.exists(crop_dir_name):
    os.mkdir(crop_dir_name)

idx = 0
while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break

    results = helmet_model.predict(im0, show=False)
    boxes = results[0].boxes.xyxy.cpu().tolist()
    clss = results[0].boxes.cls.cpu().tolist()

    if boxes is not None:
        for box, cls in zip(boxes, clss):
            idx += 1
            # Check if the class is "No_Helmet" (assuming "No_Helmet" is the last class)
            if int(cls) == len(helmet_names) - 1:
                crop_obj = im0[int(box[1]):int(box[3]), int(box[0]):int(box[2])]
                cv2.imwrite(os.path.join(crop_dir_name, str(idx) + ".png"), crop_obj)

                # Perform number plate detection on the cropped image
                numberplate_output = numberplate_model(crop_obj)

                # Get bounding boxes and classes
                numberplate_result = np.array(numberplate_output.pandas().xyxy[0])

                # Iterate through detected objects
                for i in numberplate_result:
                    p1 = (int(i[0]), int(i[1]))
                    p2 = (int(i[2]), int(i[3]))
                    roi = crop_obj[p1[1]:p2[1], p1[0]:p2[0]]  # Region of interest (number plate)

                    # Perform OCR on the region of interest
                    result = reader.readtext(roi)

                    # Extract and save text to a file
                    if result:
                        with open('number_plate_text.txt', 'a') as file:
                            for detection in result:
                                text = detection[1]
                                file.write(text + '\n')

                    # Draw bounding box and text on the original image
                    im0 = cv2.rectangle(im0, (p1[0] + int(box[0]), p1[1] + int(box[1])),
                                         (p2[0] + int(box[0]), p2[1] + int(box[1])),
                                         color=(0, 0, 255), thickness=2)
                    im0 = cv2.putText(im0, f"{i[-1]}", org=(p1[0] + int(box[0]), p1[1] + int(box[1]) - 5),
                                      fontFace=cv2.FONT_HERSHEY_PLAIN,
                                      fontScale=1.25, color=(0, 0, 255), thickness=2)

    cv2.imshow("ultralytics", im0)
    video_writer.write(im0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
video_writer.release()
cv2.destroyAllWindows()
