from PIL import Image, ImageFilter

import sys,os

class Main:
    name = "detail".lower()
    def __init__(self, img, args={}):
        self.processd = img.filter(ImageFilter.DETAIL)

    @property
    def raw(self):
        return self.processd