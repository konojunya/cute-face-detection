# -*- coding: utf-8 -*-
from utils.faceDetection import faceDetection as fd
import sys
import urllib
import os.path
import json
import glob

if __name__ == "__main__":

    print "\nstarting face detection!\n"

    for file in glob.glob('datasets/*'):
        fd.file_recognition(file)

    # f = open("./images.txt", "r")

    # for line in f:
    #     fd.recognition(line)
    # f.close()

    print "complete!"
