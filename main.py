# -*- coding: utf-8 -*-
from utils.faceDetection import faceDetection as fd
import sys, urllib
import os.path
import json

if __name__ == "__main__":

  print "\nstarting face detection!\n\n"

  f = open("./images.txt","r")
  jsonData = {}

  for line in f:
    url = str.strip(line)
    path = os.path.basename(url)
    jsonData[path] = fd.recognition(url)

  f.close()

  f = open("assets.json","w")
  json.dump(jsonData,f)
  f.close()

  print "complete!"