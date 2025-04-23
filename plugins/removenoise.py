from PIL import Image, ImageFilter, ImageOps, ImageEnhance


class Main:
    name = "removenoise".lower()
    def __init__(self, img, args={"size":3}):
        self.processd = img.filter(ImageFilter.MedianFilter(size=args["size"]))

    @property
    def raw(self):
        return self.processd