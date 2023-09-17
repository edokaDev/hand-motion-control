import cv2
import HandDetector as hd
import time

def run_detector():
    pTime = 0
    cTime = 0

    cap = cv2.VideoCapture(0)
    detector = hd.HandDetector()

    while True:
        _, img = cap.read()
        img = detector.find_hands(img)
        lm_list, bbox = detector.find_position(img)
        if len(lm_list) != 0:
            print(lm_list[4])

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

        cv2.imshow("Hand Tracker", img)
        cv2.waitKey(1)

if __name__ == '__main__':
    run_detector()
    