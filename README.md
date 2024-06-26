# No_Helmet_Motorcycle_License_Plate_Recognition

## Description
The "No Helmet Motorcycle License Plate Recognition System" is an advanced project aimed at enhancing road safety by identifying motorcyclists without helmets and capturing their license plate information in real-time. It utilizes computer vision and machine learning algorithms to detect helmetless riders, extract license plate data, and alert authorities for enforcement. Key features include helmet detection, license plate recognition, real-time monitoring, database integration, alerts, analytics, and scalability. Benefits include improved road safety, efficient enforcement, and data-driven decision-making for policymakers. In addition to the features of the "No Helmet Motorcycle License Plate Recognition System," this project includes mechanisms to detect excessive noise levels and automatically close the road by deploying a barrier when necessary.

### Helmet Detection Part
We have Trained YoloV8 model on custom dataset

Dataset Link: https://app.roboflow.com/microlab2

![val_batch1_pred](https://github.com/SakibSaad/No_Helmet_Motorcycle_License_Plate_Recognition/assets/87976927/8a40f336-e275-4c60-8061-42d1af78a335)


### License Detection & Recognition
We have used pretrained YoloV5 model to detect license plate and used easyOCR library for text recognition. Recognised text is saved in a text file.

![images (1)](https://github.com/SakibSaad/No_Helmet_Motorcycle_License_Plate_Recognition/assets/87976927/08f54469-a912-4afc-8521-ed3c29543a6e)

### Noise Pollution Reduction System

We've implemented an Arduino-based micro-controller integrated with a sound sensor to monitor noise levels on roads. When the noise exceeds a predefined threshold, the system triggers the closure of the road barrier (servo motor), simultaneously displaying "Road Closed" on the screen while the red LED blinks. Conversely, if the noise remains below the threshold, the road remains open, indicated by a steady green LED.

**System Logic:**

![Logic Diagram](https://github.com/SakibSaad/No_Helmet_Motorcycle_License_Plate_Recognition/assets/87976927/73196ea5-7d1f-4733-9b09-e289f5e843fb)

**Pin Diagram & System Overview:**

![Pin Diagram & Overview](https://github.com/SakibSaad/No_Helmet_Motorcycle_License_Plate_Recognition/assets/87976927/1df875ee-9a27-4460-9607-b192c4ad6660)

**System Prototype:**

![Prototype](https://github.com/SakibSaad/No_Helmet_Motorcycle_License_Plate_Recognition/assets/87976927/53381540-33cb-40f6-bf63-26597d7f35a0)






### How to Run the Project

To run the project, follow these steps:

1. **Install Python 3:** If you haven't already, install Python 3 from the [official Python website](https://www.python.org/).

2. **Clone the Repository:** Clone this repository to your local machine using the following command:
 ```shell
 git clone https://github.com/SakibSaad/No_Helmet_Motorcycle_License_Plate_Recognition.git
 ```

3. **Navigate to the Project Directory:** Use the `cd` command to navigate into the project directory:
   
 ```shell
 cd No_Helmet_Motorcycle_License_Plate_Recognition
 ```

5. **Run the Python Script:** Execute the following command to run the project:
 ```shell
 python3 plateXhelmet.py
 ```
This will start the project and execute the `plateXhelmet.py` script.

5. **Follow On-Screen Instructions:** Depending on the project, you may need to follow additional on-screen instructions or interact with the script as it runs.

That's it! You've successfully run the project. If you encounter any issues, feel free to open an [issue](https://github.com/your-username/your-repository/issues) on this repository for assistance.

