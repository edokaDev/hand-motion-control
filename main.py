import cv2
import HandDetector as hd
import Camera as cm
import Mouse as ms
import time
import numpy as np

camera = cm.Camera()
mouse = ms.Mouse()
cap = camera.start_cam()

pTime = 0
p_loc_x, p_loc_y = 0, 0
c_loc_x, c_loc_y = 0, 0

detector = hd.HandDetector(maxHands=1)

w_scr, h_scr = camera.get_screen_details()
frame_r = camera.frame_r
w_cam = camera.w_cam
h_cam = camera.h_cam

while True:
	# find hand landmarks
	_, img = cap.read()
	
	img = detector.find_hands(img)
	lm_list, bbox = detector.find_position(img)

	# get the tip of the index and middle fingers
	if len(lm_list) != 0:
		x1, y1 = lm_list[8][1:]
		x2, y2 = lm_list[12][1:]

		# check which fingers are up
		fingers = detector.fingers_up()
		# print(fingers)
		cv2.rectangle(img, (camera.frame_r, camera.frame_r), (camera.w_cam - camera.frame_r, camera.h_cam - camera.frame_r),
						(255, 0, 255), 2)

		# 7. Move 

		# MOVE GESTURE 1: ONLY INDEX FINGER UP
		# if fingers[1] == 1 and fingers[2] == 0:

		# MOVE GESTURE 2: ALL FINGERS UP
		if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
			# 5.convert coordinates
			x3 = np.interp(x1, (frame_r, w_cam - frame_r), (0, w_scr))
			y3 = np.interp(y1, (frame_r, h_cam - frame_r), (0, h_scr))
			# 6. smoothen values
			c_loc_x = p_loc_x + (x3 - p_loc_x) / camera.smoothening
			c_loc_y = p_loc_y + (y3 - p_loc_y) / camera.smoothening
			# 7. move mouse
			mouse.move(w_scr - c_loc_x, c_loc_y)
			cv2.circle(img, (x1, y1), 15, (255, 0 ,255), cv2.FILLED)
			p_loc_x, p_loc_y = c_loc_x, c_loc_y


		# 8. Click

		# CLICK GESTURE 1: INDEX AND MIDDLE FINGER UP AND JOINED TOGETHER
		# if fingers[1] == 1 and fingers[2] == 1:
		# CLICK GESTURE 2: MAKE A FIST (ALL FINGERS DOWN)
		if fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
			# 9. find distance between finger
			length, img, line_info = detector.find_distance(8, 12, img)
			# print(length)
			# 10. click mous if distance is short
			if length < 50:
				cv2.circle(img, (line_info[4], line_info[5]),
	       					15, (0, 255,0), cv2.FILLED)
				mouse.click()

	# frame rate
	cTime = time.time()
	fps = camera.get_frame_rate(cTime, pTime)
	pTime = cTime

	cv2.putText(
		img,
		str(int(fps)),
		(10, 70),
		cv2.FONT_HERSHEY_PLAIN,
		3,
		(255, 0, 255),
		3
	)

	# display
	cv2.imshow("Image", img)
	cv2.waitKey(1)