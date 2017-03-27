# -*- coding: utf-8 -*-
from utils.faceDetection import faceDetection as fd
import sys
import urllib
import os.path
import json

if __name__ == "__main__":

    print "\nstarting face detection!\n"

    f = open("./images.txt", "r")

    for line in f:
        fd.recognition(line)
    f.close()

    f = open("assets.json", "w")
    json.dump(fd.getJsonData(), f,indent=2,sort_keys=True,separators=(',', ': '))
    f.close()

    print "complete!"
