#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

import dlib

import cv2

import pygame
import time



class Player:
    def __init__(self, filename):
        pygame.mixer.init(frequency=44100)
        self.soundC = pygame.mixer.Sound(filename)
        self.playFlag = False
        self.playStartTime = 0

    def playsound(self):
        if self.playFlag == False:
            self.soundC.play(maxtime=1000)
            self.playStartTime = time.time()
            self.playFlag = True

        if time.time() - self.playStartTime > 1.0:
            self.soundC.stop()
            self.playFlag = False

if __name__ == "__main__":
    detector = dlib.get_frontal_face_detector()
    cap= cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception, 'video not found'

    playerC = Player("sounds/pianoC.wav")
    playerD = Player("sounds/pianoD.wav")
    playerE = Player("sounds/pianoE.wav")
    playerF = Player("sounds/pianoF.wav")
    playerG = Player("sounds/pianoG.wav")
    playerA = Player("sounds/pianoA.wav")
    playerB = Player("sounds/pianoB.wav")

    rangeC = 640.0/7.0 * 1.0
    rangeD = 640.0/7.0 * 2.0
    rangeE = 640.0/7.0 * 3.0
    rangeF = 640.0/7.0 * 4.0
    rangeG = 640.0/7.0 * 5.0
    rangeA = 640.0/7.0 * 6.0
    rangeB = 640.0/7.0 * 7.0

    while(cap.isOpened()):
        cv2.waitKey(1)
        ret, frame = cap.read()
        dets = detector(frame)
        for d in dets:

            r ,g ,b = 0, 0, 0
            if d.left() < rangeC:
                playerC.playsound()
                r = 255

            elif d.left() < rangeD:
                playerD.playsound()
                r, g = 255, 165

            elif d.left() < rangeE:
                playerE.playsound()
                r, g = 255, 255

            elif d.left() < rangeF:
                playerF.playsound()
                g = 255

            elif d.left() < rangeG:
                playerG.playsound()
                g, b = 255, 255

            elif d.left() < rangeA:
                playerA.playsound()
                b = 255

            elif d.left() < rangeB:
                playerB.playsound()
                r, b = 128, 128

            cv2.rectangle(frame, (d.left(), d.top()), (d.right(), d.bottom()),\
                    (b, g, r), 2)

        cv2.imshow("SatouPiano", frame)

        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            sys.exit()
