# -*- coding: utf-8 -*-
import os
import urllib2
import urllib


class DetectFaceProxy(object):

    def __init__(self, mode=0, force=1):
        self.detect_face_url = 'http://detectface.com/api/detect?m={m}&f={f}'.format(
            m=mode, f=force)
        self.data = ''

    def fetch_feature(self, image_file_path):
        path, type = os.path.splitext(image_file_path)
        content_type = type[1:]
        if content_type == "jpg":
            content_type = "jpeg"

        data = self._read_image_binary(image_file_path)
        request = urllib2.Request(self.detect_face_url)

        request.add_header('Content-Type', 'image/{t}'.format(t=content_type))
        request.add_data(data)
        opener = urllib2.build_opener()
        self.data = opener.open(request).read()
        return self.data

    def _read_image_binary(self, file_path):
        return open(file_path, "r").read()


detectface = DetectFaceProxy()
