import cv2
import HandDetector as hd
import Camera as cm
import Mouse as ms
import time

camera = cm.Camera()
cap = camera.start_cam()

pTime = 0

detector = hd.HandDetector(maxHands=1)
# screen size

while True:
	# find hand landmarks
	_, img = cap.read()
	
	img = detector.find_hands(img)
	lm_list, bbox = detector.find_position(img)

	# get the tip of the index and middle fingers
	if len(lm_list) != 0:
		x1, y1 = lm_list[8 ][1:]
		x2, y2 = lm_list[12][1:]
		mouse = ms.Mouse(x1, y1, camera)

		# check which fingers are up
		fingers = detector.fingers_up()
		# print(fingers)
		cv2.rectangle(img, (camera.frame_r, camera.frame_r), (camera.w_cam - camera.frame_r, camera.h_cam - camera.frame_r),
						(255, 0, 255), 2)
		# only index finger = moving mode
		if fingers[1] == 1 and fingers[2] == 0:
			mouse.move(img)
		# 8. both index and middle fingers are up = clicking mode
		if fingers[1] == 1 and fingers[2] == 1:
			length, img, line_info = detector.find_distance(8, 12, img)
			mouse.click(length, img, line_info)

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