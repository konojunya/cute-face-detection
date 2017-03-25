# -*- coding: utf-8 -*-
import cv2
import os.path

class FaceDetection(object):

  def __init__(self):
    self.image_path = "./girl.jpg"
    self.cascade_path = {
      "face": "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml",
      "eye": "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_eye.xml",
      "nose": "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_mcs_nose.xml"
    }

  def readImage(self):
    return cv2.imread(self.image_path)

  def convertToGrayScale(self,image):
    return cv2.cvtColor(image,cv2.cv.CV_BGR2GRAY)

  def recognition(self):
    image = self.readImage()
    image_gray = self.convertToGrayScale(image)

    face_cascade = cv2.CascadeClassifier(self.cascade_path["face"])
    facerect = face_cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
    
    if len(facerect) > 0:
      eye_cascade = cv2.CascadeClassifier(self.cascade_path["eye"])
      eyerect = eye_cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
      nose_cascade = cv2.CascadeClassifier(self.cascade_path["nose"])
      noserect = nose_cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

    facerect_len = len(facerect)
    eyerect_len = len(eyerect)
    noserect_len = len(noserect)

    return int(facerect_len)+int(eyerect_len)+int(noserect_len) > 10 if True else False


  def checkFaceDetection(self):
    isFace = self.recognition()

    if isFace:
      print "This image is face!"
    else:
      print "This image is not face!"

  def exportDetectedImage(self,rects):
    img = self.readImage()
    for rect in rects:
      cv2.rectangle(img, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), (0,0,0), thickness=2)
      cv2.imwrite("detected.jpg", img)


faceDetection = FaceDetection()