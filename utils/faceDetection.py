# -*- coding: utf-8 -*-
import cv2, os.path, sys, urllib


class FaceDetection(object):

    def __init__(self):
        self.cascade_path = {
            "face": "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml",
            "eye": "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_eye.xml",
            "nose": "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_mcs_nose.xml"
        }

    def readImage(self,url):
        img = urllib.urlopen(url)
        image_path = os.path.basename(url)
        localfile = open("assets/"+image_path, 'wb')
        localfile.write(img.read())
        img.close()
        localfile.close()

        return cv2.imread("assets/"+image_path)

    def convertToGrayScale(self, image):
        return cv2.cvtColor(image, cv2.cv.CV_BGR2GRAY)

    def recognition(self,url):
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

        print "\nface rect/ "+str(facerect_len)
        print "eye rect/ "+str(eyerect_len)
        print "nose rect/ "+str(noserect_len)

        return int(facerect_len) + int(eyerect_len) + int(noserect_len) > 10 if True else False

faceDetection = FaceDetection()
