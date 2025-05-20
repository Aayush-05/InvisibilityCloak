import cv2
import numpy as np
import time 

print("""✨ Preparing your cloak of invisibility...
Quickly vanish from the camera's sight for 5 seconds while we capture the untouched realm behind you!
""")

video = cv2.VideoCapture(0) #start Webcam and Capture the background
time.sleep(3)

bg_frame = 0
for _ in range(30):
    success, bg_frame = video.read()

bg_frame = np.flip(bg_frame, axis=1)

while video.isOpened():   #keep running until the video is opened
    success, frame = video.read()
    if not success:
        break
    frame = np.flip(frame, axis=1)

    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #convert the frame to HSV color space
    blurred_hsv = cv2.GaussianBlur(hsv_img, (35,35), 0) #apply GaussianBlur to reduce noise

    red_lower_1 = np.array([0,120,70])
    red_upper_1 = np.array([10,255,255])
    mask_red1 = cv2.inRange(hsv_img, red_lower_1, red_upper_1)
    red_lower_2 = np.array([170,120,70])
    red_upper_2 = np.array([180,255,255])
    mask_red2 = cv2.inRange(hsv_img, red_lower_2, red_upper_2)

    full_mask = mask_red1 + mask_red2

    full_mask = cv2.morphologyEx(
        full_mask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8)
    )

    frame[np.where(full_mask==255)] = bg_frame[np.where(full_mask==255)]

    cv2.imshow('Magic Window', frame)

    if cv2.waitKey(10) == 27:
        break