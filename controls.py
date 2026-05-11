class DisplaySize:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def values(self):
        return self.width,self.height


class ScreenColor:
    def __init__(self,red,green,blue):
        self.red=red
        self.green=green
        self.blue=blue
    def color_change(self):
        self.red += 5
        self.green += 2
        self.blue += 13
        if self. red > 255 or self.green > 255 or self.blue > 255:
            self.red = self.green = self.blue = 0


