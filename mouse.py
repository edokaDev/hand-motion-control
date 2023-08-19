import cv2
import numpy as np
import HandDetector as hd
import time
import autopy

frame_r = 100
w_cam, h_cam = 640, 480
smoothening = 10

cap = cv2.VideoCapture(0)
cap.set(3, w_cam)
cap.set(4, h_cam)

pTime = 0
p_loc_x, p_loc_y = 0, 0
c_loc_x, c_loc_y = 0, 0

detector = hd.HandDetector(maxHands=1)
# screen size
w_scr, h_scr = autopy.screen.size()
# print(w_scr, h_scr)

while True:
	# 1. find hand landmarks
	_, img = cap.read()
	img = detector.find_hands(img)
	lm_list, bbox = detector.find_position(img)

	# 2. get the tip of the index and middle fingers
	if len(lm_list) != 0:
		x1, y1 = lm_list[8 ][1:]
		x2, y2 = lm_list[12][1:]

		# 3. check which fingers are up
		fingers = detector.fingers_up()
		# print(fingers)
		cv2.rectangle(img, (frame_r, frame_r), (w_cam - frame_r, h_cam - frame_r),
						(255, 0, 255), 2)
		# 4.only index finger = moving mode
		if fingers[1] == 1 and fingers[2] == 0:
			# 5.convert coordinates
			x3 = np.interp(x1, (frame_r, w_cam - frame_r), (0, w_scr))
			y3 = np.interp(y1, (frame_r, h_cam - frame_r), (0, h_scr))
			# 6. smoothen values
			c_loc_x = p_loc_x + (x3 - p_loc_x) / smoothening
			c_loc_y = p_loc_y + (y3 - p_loc_y) / smoothening
			# 7. move mouse
			autopy.mouse.move(w_scr - c_loc_x, c_loc_y)
			cv2.circle(img, (x1, y1), 15, (255, 0 ,255), cv2.FILLED)
			p_loc_x, p_loc_y = c_loc_x, c_loc_y
		# 8. both index and middle fingers are up = clicking mode
		if fingers[1] == 1 and fingers[2] == 1:
			# 9. find distance between finger
			length, img, line_info = detector.find_distance(8, 12, img)
			# print(length)
			# 10. click mous if distance is short
			if length < 40:
				cv2.circle(img, (line_info[4], line_info[5]),
	       					15, (0, 255,0), cv2.FILLED)
				autopy.mouse.click()

	# frame rate
	cTime = time.time()
	fps = 1/(cTime-pTime)
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