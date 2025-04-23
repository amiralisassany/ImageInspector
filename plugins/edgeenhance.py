from PIL import Image, ImageFilter


class Main:
    name = "edgeenhance".lower()
    def __init__(self, img, args={}):
        self.processd = img.filter(ImageFilter.EDGE_ENHANCE)

    @property
    def raw(self):
        return self.processd