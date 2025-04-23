from PIL import Image, ImageFilter

import sys,os

class Main:
    name = "convolution".lower()
    def __init__(self, img, args={}):
        self.processd = img.filter(ImageFilter.Kernel((3, 3), (0, -1, 0, -1, 5, -1, 0, -1, 0)))

    @property
    def raw(self):
        return self.processd