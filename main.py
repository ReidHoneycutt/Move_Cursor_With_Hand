import cv2
import pyautogui
import time
import random
from cvzone.HandTrackingModule import HandDetector
import math


def init_cap():
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    return cap

def init_detector():
    detector = HandDetector(detectionCon=0.8, maxHands=1)
    return detector



def move_cursor(cap, detector):
    while True:
        success, img = cap.read()
        hands, img = detector.findHands(img)

        if hands:
            pyautogui.moveTo(1920-(7/6)*hands[0]["lmList"][8][0], (1/2)*hands[0]["lmList"][8][1])

        cv2.waitKey(0)


def main():
    cap = init_cap()
    detector = init_detector()
    move_cursor(cap, detector)


if __name__ == '__main__':
    main()