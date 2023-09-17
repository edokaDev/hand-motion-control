import Camera as cam
import cv2

camera = cam.Camera().start_cam()

while True:
	# find hand landmarks
	_, img = camera.read()

	cv2.imshow("Image", img)
	cv2.waitKey(1)