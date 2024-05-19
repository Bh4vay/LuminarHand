import cv2
import time
import numpy as np
import mediapipe as mp
import screen_brightness_control as sbc
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
pTime = 0

while True:
    success, img = cap.read()
    imgHeight,imgWidth,_ = img.shape
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    hand_landmarks = result.multi_hand_landmarks
    if hand_landmarks:
        for hand_landmark in hand_landmarks:
            mp_draw.draw_landmarks(img,hand_landmark, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmark.landmark
            # print(landmarks)
            for id,landmark in enumerate(landmarks):
                x = int(landmark.x * imgWidth)
                y = int(landmark.y * imgHeight)
                
                if (id==4):
                    cv2.circle(img=img,center=(x,y),radius=12,color=(0,255,0),thickness=cv2.FILLED)
                    thumb_x = x
                    thumb_y = y
                
                if (id == 8):
                    cv2.circle(img=img,center=(x,y),radius=12,color=(0,255,0),thickness=cv2.FILLED)
                    index_x = x
                    index_y = y
                    cv2.line(img,(thumb_x,thumb_y),(index_x,index_y),(255,0,0),3)
                        
                    length = math.hypot(index_x - thumb_x, index_y - thumb_y)
                    bright = np.interp(length,[15,220],[0,100])
                    sbc.set_brightness(int(bright))
                    
                
    
    
    
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(40,50),cv2.FONT_HERSHEY_SIMPLEX,1.2,(255,0,0),3)
    
    
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()