# No_Helmet_Motorcycle_License_Plate_Recognition

## Description
The "No Helmet Motorcycle License Plate Recognition System" is an advanced project aimed at enhancing road safety by identifying motorcyclists without helmets and capturing their license plate information in real-time. It utilizes computer vision and machine learning algorithms to detect helmetless riders, extract license plate data, and alert authorities for enforcement. Key features include helmet detection, license plate recognition, real-time monitoring, database integration, alerts, analytics, and scalability. Benefits include improved road safety, efficient enforcement, and data-driven decision-making for policymakers. In addition to the features of the "No Helmet Motorcycle License Plate Recognition System," this project includes mechanisms to detect excessive noise levels and automatically close the road by deploying a barrier when necessary.

### Helmet Detection Part
We have Trained YoloV8 model on custom dataset

### License Detection & Recognition
We have used pretrained YoloV5 model to detect license plate and used easyOCR library for text recognition.

### Noise Pollution Reduction
We have used arduino as micro-controller and added sound sensor to detect noise on the road. If noise excludes certain threshold we close the servo 
