# -*- coding: utf-8 -*-
from utils.faceDetection import faceDetection as fd
import sys, urllib
import os.path
import json

if __name__ == "__main__":
  f = open("./images.txt","r")
  jsonData = {}

  for line in f:
    url = str.strip(line)
    path = os.path.basename(url)
    isFace = fd.recognition(url)

    jsonData[path] = isFace

    if not(isFace):
      os.remove("assets/"+path)

  f.close()

  f = open("assets.json","w")
  json.dump(jsonData,f)
  f.close()

  print "complete!"