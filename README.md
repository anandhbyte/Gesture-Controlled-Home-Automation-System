# Gesture-Controlled-Home-Automation-System


**Deployment Instructions**

Hardware:
- Raspberry Pi (any model)
- Webcam
- Jumper Wires
- 4-channel Relay Board

Software:
- Python 3.x
- OpenCV
- CVZone
- RPi.GPIO library
  
Setup Steps
Connect the relay board to the Raspberry Pi GPIO pins:

- Relay 1: Pin 3 
- Relay 2: Pin 5 
- Relay 3: Pin 7
- Relay 4: Pin 8
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


