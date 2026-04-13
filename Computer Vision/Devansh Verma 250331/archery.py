import cv2
import numpy as np

cap = cv2.VideoCapture("C:\Users\Devansh\Downloads\WhatsApp Video 2026-04-08 at 21.25.35.mp4")
while(cap.isOpened()):
  ret, frame = cap.read()
  if not ret:
    break
  frame = cv2.resize(frame, (540, 380), fx = 0, fy = 0,
                         interpolation = cv2.INTER_CUBIC)
  
  frame = frame[0:250, 30:540]
  img_ = frame.copy()
  red_low_rgb = np.array([150, 0, 0])
  red_high_rgb = np.array([255, 120, 120])
  frame = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
  mask1 = cv2.inRange(frame, red_low_rgb, red_high_rgb)
  imgray = cv2.cvtColor(mask1 , cv2.COLOR_RGB2GRAY)
  ret1, thresh = cv2.threshold(mask1, 127, 255, 0)
  contours, hierarchy = cv2.findContours(mask1,mode= cv2.RETR_TREE,method= cv2.CHAIN_APPROX_SIMPLE)
  if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        cv2.drawContours(img_, [largest_contour], -1, (0, 255, 0), thickness=3)

  cv2.imshow(img_)
