from PIL import Image, ImageFilter

import sys,os

class Main:
    name = "unsharpmask".lower()
    def __init__(self, img, args={"radius" : 2,"percent" : 200,"threshold" : 3}):
        self.processd = img.filter(ImageFilter.UnsharpMask(radius=args["radius"], percent=args['percent'], threshold=args['threshold']))

    @property
    def raw(self):
        return self.processd