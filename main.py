# -*- coding: utf-8 -*-
from utils.faceDetection import faceDetection as fd
import sys
import urllib
import os.path
import json

if __name__ == "__main__":

    print "starting face detection!"

    f = open("./test.txt", "r")
    jsonData = {}

    for line in f:
        url = str.strip(line)
        path = os.path.basename(url)
        jsonData[path] = fd.recognition(url)

    f.close()

    f = open("test.json", "w")
    json.dump(jsonData, f)
    f.close()

    print "complete!"
