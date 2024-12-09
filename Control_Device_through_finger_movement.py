import cv2 
from cvzone.HandTrackingModule import HandDetector 
import RPi.GPIO as GPIO     # Import Library to access GPIO PIN
import time                 # To access delay function

GPIO.setmode(GPIO.BOARD)    # Consider complete raspberry-pi board
GPIO.setwarnings(False)     # To avoid same PIN use warning
Relay_1_Pin = 3             
Relay_2_Pin = 5
Relay_3_Pin = 7
Relay_4_Pin = 8

GPIO.setup(Relay_1_Pin,GPIO.OUT)   
GPIO.setup(Relay_2_Pin,GPIO.OUT)
GPIO.setup(Relay_3_Pin,GPIO.OUT)   
GPIO.setup(Relay_4_Pin,GPIO.OUT)

GPIO.output(Relay_1_Pin,GPIO.HIGH)
GPIO.output(Relay_2_Pin,GPIO.HIGH)
GPIO.output(Relay_3_Pin,GPIO.HIGH)
GPIO.output(Relay_4_Pin,GPIO.HIGH)

relay_1_status = 0
relay_2_status = 0
relay_3_status = 0
relay_4_status = 0
# font 
font = cv2.FONT_HERSHEY_SIMPLEX 
  
# org 
org = (0, 80) 
  
# fontScale 
fontScale = 1.7
   
# white color in BGR 
color = (0,255,255) 
  
# Line thickness of 2 px 
thickness = 6

detector = HandDetector(maxHands=1, detectionCon=0.8) 
video = cv2.VideoCapture(0) 
text = ""
while True: 
    _, img = video.read() 
    img = cv2.flip(img, 1) 
    hand = detector.findHands(img, draw=False)
    text = "Show Finger"
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup == [0, 1, 0, 0, 0]:
                if(relay_1_status == 0):
                    relay_1_status = 1
                    index_text = "Index Finger : Bulb ON"
                    GPIO.output(Relay_1_Pin,GPIO.LOW)
                    time.sleep(0.1)
                elif(relay_1_status == 2):
                    relay_1_status = 3
                    index_text = "Index Finger : Bulb OFF"
                    GPIO.output(Relay_1_Pin,GPIO.HIGH)
                    time.sleep(0.1)
                else:
                    text = index_text
            if fingerup == [0, 0, 1, 0, 0]: 
                if(relay_2_status == 0):
                    relay_2_status = 1
                    middle_text = "Middle Finger : Fan ON"
                    GPIO.output(Relay_2_Pin,GPIO.LOW)
                    time.sleep(0.1)
                elif(relay_2_status == 2):
                    relay_2_status = 3
                    middle_text = "Middle Finger : Fan OFF"
                    GPIO.output(Relay_2_Pin,GPIO.HIGH)
                    time.sleep(0.1)
                else:
                    text = middle_text 
            if fingerup == [0, 0, 0, 1, 0]: 
                text = "Ring Finger"
            if fingerup == [0, 0, 0, 0, 1]: 
                if(relay_3_status == 0):
                    relay_3_status = 1
                    pinky_text = "Pinky Finger:Tube ON"
                    GPIO.output(Relay_3_Pin,GPIO.LOW)
                    time.sleep(0.1)
                elif(relay_3_status == 2):
                    relay_3_status = 3
                    pinky_text = "Pinky Finger:Tube OFF"
                    GPIO.output(Relay_3_Pin,GPIO.HIGH)
                    time.sleep(0.1)
                else:
                    text = pinky_text 
            if fingerup == [1, 0, 0, 0, 0]: 
                if(relay_4_status == 0):
                    relay_4_status = 1
                    thumb_text = "Thumb : Buzzer ON"
                    GPIO.output(Relay_4_Pin,GPIO.LOW)
                    time.sleep(0.1)
                elif(relay_4_status == 2):
                    relay_4_status = 3
                    thumb_text = "Thumb :Buzzer OFF"
                    GPIO.output(Relay_4_Pin,GPIO.HIGH)
                    time.sleep(0.1)
                else:
                    text = thumb_text 
        else:
            if(relay_1_status == 1):
                relay_1_status = 2
            elif(relay_1_status == 3):
                relay_1_status = 0
            elif(relay_2_status == 1):
                relay_2_status = 2
            elif(relay_2_status == 3):
                relay_2_status = 0
            elif(relay_3_status == 1):
                relay_3_status = 2
            elif(relay_3_status == 3):
                relay_3_status = 0
            elif(relay_4_status == 1):
                relay_4_status = 2
            elif(relay_4_status == 3):
                relay_4_status = 0
    img = cv2.putText(img,text, org, font,fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow("Video", img) 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
        
video.release() 
cv2.destroyAllWindows() 

