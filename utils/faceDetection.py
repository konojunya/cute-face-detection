# -*- coding: utf-8 -*-
import cv2
import os.path
import sys
import urllib
import numpy as np
import re


class FaceDetection(object):

    def __init__(self):
        self.cascade_path = {
            "face": "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml",
            "eye": "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_eye.xml",
            "nose": "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_mcs_nose.xml"
        }

    def _print(self, text):
        print '\033[92m' + text + '\033[0m'

    def readImage(self, url):
        print "\ndownloading %s" % (url)
        resp = urllib.urlopen(url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        return image

    def convertToGrayScale(self, image):
        return cv2.cvtColor(image, cv2.cv.CV_BGR2GRAY)

    def recognition(self, line):
        url = str.strip(line)
        path = os.path.basename(url)
        try:
            image = self.readImage(url)
            image_gray = self.convertToGrayScale(image)

            face_cascade = cv2.CascadeClassifier(self.cascade_path["face"])
            facerect = face_cascade.detectMultiScale(
                image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

            eyerect = []
            noserect = []

            if len(facerect) > 0:
                eye_cascade = cv2.CascadeClassifier(self.cascade_path["eye"])
                eyerect = eye_cascade.detectMultiScale(
                    image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
                nose_cascade = cv2.CascadeClassifier(self.cascade_path["nose"])
                noserect = nose_cascade.detectMultiScale(
                    image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

            facerect_len = len(facerect)
            eyerect_len = len(eyerect)
            noserect_len = len(noserect)

            self._print("face rect:\t" + str(facerect_len))
            self._print("eye rect:\t" + str(eyerect_len))
            self._print("nose rect:\t" + str(noserect_len))
        except:
            print "Exception!"
            facerect_len = 0
            eyerect_len = 0
            noserect_len = 0

        self._print("Total Point:\t" + str(int(facerect_len) +
                                           int(eyerect_len) + int(noserect_len)))

    def file_recognition(self, file):
        file = str.strip(file)
        print "\nrecognition...\t" + file

        facerect_len = 0
        eyerect_len = 0
        noserect_len = 0

        try:
            image = cv2.imread(file)
            image_gray = self.convertToGrayScale(image)

            face_cascade = cv2.CascadeClassifier(self.cascade_path["face"])
            facerect = face_cascade.detectMultiScale(
                image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

            eyerect = []
            noserect = []

            if len(facerect) > 0:
                eye_cascade = cv2.CascadeClassifier(self.cascade_path["eye"])
                eyerect = eye_cascade.detectMultiScale(
                    image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
                nose_cascade = cv2.CascadeClassifier(self.cascade_path["nose"])
                noserect = nose_cascade.detectMultiScale(
                    image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

            facerect_len = len(facerect)
            eyerect_len = len(eyerect)
            noserect_len = len(noserect)

            self._print("face rect:\t" + str(facerect_len))
            self._print("eye rect:\t" + str(eyerect_len))
            self._print("nose rect:\t" + str(noserect_len))

            i = 1
            for rect in facerect:
                x = rect[0]
                y = rect[1]
                w = rect[2]
                h = rect[3]

                if w > 32 and h > 32:
                    cv2.rectangle(image, tuple(rect[0:2]), tuple(
                        rect[0:2] + rect[2:4]), (255, 255, 255), thickness=2)
                    cv2.imwrite(
                        "face-detect/" + re.sub(r'datasets\/', str(i) + "-", file), image)
                    size = (32, 32)
                    image = image[y:y + h, x:x + w]
                    image = cv2.resize(image, size)
                    cv2.imwrite("face-clip/" + re.sub(r'datasets\/',
                                                      str(i) + "-", file), image)
                    i += 1

        except:
            print "Exception!"

        self._print("Total Point:\t" + str(int(facerect_len) +
                                           int(eyerect_len) + int(noserect_len)))

        # if int(facerect_len) + int(eyerect_len) + int(noserect_len) < 5:
        #     os.remove(file)


faceDetection = FaceDetection()
