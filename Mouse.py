import cv2
import numpy as np
import autopy


class Mouse():
    def __init__(self, x1, y1, camera):
        self.x1 = x1
        self.y1 = y1
        self.frame_r = camera.frame_r
        self.w_cam = camera.w_cam
        self.h_cam = camera.h_cam
        self.smoothening = camera.smoothening
        self.w_scr, self.h_scr = camera.get_screen_details()

    
    def move(self, img):
        p_loc_x, p_loc_y = 0, 0
        c_loc_x, c_loc_y = 0, 0

        x3 = np.interp(self.x1, (self.frame_r, self.w_cam - self.frame_r), (0, self.w_scr))
        y3 = np.interp(self.y1, (self.frame_r, self.h_cam - self.frame_r), (0, self.h_scr))
        # smoothen values
        c_loc_x = p_loc_x + (x3 - p_loc_x) / self.smoothening
        c_loc_y = p_loc_y + (y3 - p_loc_y) / self.smoothening
        # move mouse
        autopy.mouse.move(self.w_scr - c_loc_x, c_loc_y)
        cv2.circle(img, (self.x1,self. y1), 15, (255, 0 ,255), cv2.FILLED)
        p_loc_x, p_loc_y = c_loc_x, c_loc_y
    
    def click(self, length, img, line_info):
        # print(length)
        # click mous if distance is short
        if length < 40:
            cv2.circle(img, (line_info[4], line_info[5]),
                        15, (0, 255,0), cv2.FILLED)
            autopy.mouse.click()
    
    def double_click(self):
        pass
    
    def right_click(self):
        pass
    
    def drag(self):
        pass

