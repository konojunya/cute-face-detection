# -*- coding: utf-8 -*-
import cv2
import os.path
import sys
import urllib
import numpy as np

class FaceDetection(object):

    def __init__(self):
        self.cascade_path = {
            "face": "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml",
            "eye": "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_eye.xml",
            "nose": "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_mcs_nose.xml"
        }

    def print(self, text):
        print '\033[92m' + text + '\033[0m'

    def readImage(self, url):
        print "downloading %s" % (url)
        resp = urllib.urlopen(url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        return image

    def convertToGrayScale(self, image):
        return cv2.cvtColor(image, cv2.cv.CV_BGR2GRAY)

    def recognition(self, url):
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

            self.print("\nface rect:\t\t" + str(facerect_len))
            self.print("eye rect:\t\t" + str(eyerect_len))
            self.print("nose rect:\t\t" + str(noserect_len))
            print "\n"
        except:
            facerect_len = 0
            eyerect_len = 0
            noserect_len = 0

        return int(facerect_len) + int(eyerect_len) + int(noserect_len) > 10 if True else False


faceDetection = FaceDetection()
