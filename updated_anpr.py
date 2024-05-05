import torch
import cv2
import numpy as np
from pathlib import Path
import easyocr

# Model paths
model_path = Path("best.pt")  # Custom model path
img_path = Path("/home/saadlockholmes/Videos/automatic-number-plate-recognition-main/images.jpeg")  # Input image path

# Choose device: "cpu" or "cuda" (if CUDA is available)
cpu_or_cuda = "cpu"
device = torch.device(cpu_or_cuda)

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)
model = model.to(device)

# Load image
image = cv2.imread(str(img_path))

# Perform inference
output = model(image)

# Get bounding boxes and classes
result = np.array(output.pandas().xyxy[0])

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Iterate through detected objects
for i in result:
    p1 = (int(i[0]), int(i[1]))
    p2 = (int(i[2]), int(i[3]))
    roi = image[p1[1]:p2[1], p1[0]:p2[0]]  # Region of interest (number plate)
    
    # Perform OCR on the region of interest
    result = reader.readtext(roi)
    
    # Extract and save text to a file
    if result:
        with open('number_plate_text.txt', 'a') as file:
            for detection in result:
                text = detection[1]
                file.write(text + '\n')

    # Draw bounding box and text on the image
    image = cv2.rectangle(image, p1, p2, color=(0, 0, 255), thickness=2)
    image = cv2.putText(image, f"{i[-1]}", org=(p1[0], p1[1] - 5), fontFace=cv2.FONT_HERSHEY_PLAIN,
                        fontScale=1.25, color=(0, 0, 255), thickness=2)

# Display image
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
