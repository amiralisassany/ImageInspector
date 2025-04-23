from PIL import Image, ImageFilter, ImageEnhance
import io

import os,sys
sys.path.append(os.path.abspath("plugins/"))
plugins = list(map(lambda x: x.replace(".py", ""), os.listdir('plugins/')))


class Process:
    def export(self, format="png"):
        self.file = io.BytesIO()
        img = self.main.raw
        img.save(self.file, format=format)
        return self.file

    def show(self):
        return self.main.raw.show()

class Handler(Process):
    def __init__(self, pname, img, args={}):
        if args == {}: 
            self.main = __import__(pname).Main(img)
        else : 
            self.main = __import__(pname).Main(img,args)
