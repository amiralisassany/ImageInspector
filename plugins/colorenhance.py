from PIL import Image, ImageEnhance


class Main:
    name = "colorenhance".lower()
    def __init__(self, img, args={"enhance":1.3}):
        color_enhancer = ImageEnhance.Color(img)
        image = color_enhancer.enhance(args["enhance"])
        self.processd = image

    @property
    def raw(self):
        return self.processd