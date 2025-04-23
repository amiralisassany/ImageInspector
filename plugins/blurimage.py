from PIL import Image, ImageFilter

import sys,os

class Main:
    name = "blurimage".lower()
    def __init__(self, img, args={"radius":3}):
        self.processd = img.filter(ImageFilter.BoxBlur(radius=args['radius']))

    @property
    def raw(self):
        return self.processd