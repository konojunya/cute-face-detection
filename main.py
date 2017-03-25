# -*- coding: utf-8 -*-
from utils.faceDetection import faceDetection as fd
import sys, urllib
import os.path

if __name__ == "__main__":
  f = open("./images.txt","r")

  for line in f:
    url = str.strip(line)
    isFace = fd.recognition(url)
    
    if not(isFace):
      os.remove("assets/"+os.path.basename(url))

  f.close()