import cv2
import autopy

class Camera():
    def __init__(self,frame_r=100,w_cam=640,h_cam=480,smoothening=10):
        self.frame_r = frame_r
        self.w_cam = w_cam
        self.h_cam = h_cam
        self.smoothening = smoothening

    def start_cam(self):
        cap = cv2.VideoCapture(0)
        cap.set(3, self.w_cam)
        cap.set(4, self.h_cam)
        return cap
    
    def get_screen_details(self):
        w_scr, h_scr = autopy.screen.size()
        return w_scr, h_scr

    def get_frame_rate(self, c_time, p_time):
        fps = 1/(c_time-p_time)
        return fps
