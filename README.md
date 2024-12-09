# Gesture-Controlled-Home-Automation-System

Deployment Instructions
**1 Prerequisites**

Hardware:
Raspberry Pi (any model)
Webcam
5 Jumper Wires
4-channel Relay Board

Software:
Python 3.x
OpenCV
CVZone
RPi.GPIO library
3.2 Setup Steps
Connect the relay board to the Raspberry Pi GPIO pins:

Relay 1: Pin 3 /n
Relay 2: Pin 5 /n
Relay 3: Pin 7
Relay 4: Pin 8
Install required Python libraries:

 ```sh
pip install opencv-python cvzone RPi.GPIO
   ```
Place the project files (Control_Device_through_finger_movement.py and HandTrackingModule.py) in the same directory.

Run the main script:

 ```sh
python Control_Device_through_finger_movement.py
   ```
**Configuration**
Adjust GPIO pin mappings if needed in the Python script.
Ensure proper power supply for the relay board.

**Code Repository**
The complete code is available on GitHub: GitHub Repository Link
(Upload the project to GitHub and replace with the actual link.)

