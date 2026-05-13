class DisplaySize:
    def __init__(self):
        self.width=1200
        self.height=800

    def values(self):
        return self.width,self.height


class ScreenColor:
    def __init__(self):
        self.red=100
        self.green=100
        self.blue=100
    def color_change(self):
        self.red += 5
        self.green += 2
        self.blue += 13
        if self. red > 255 or self.green > 255 or self.blue > 255:
            self.red = self.green = self.blue = 0


class ShipSize:
    def __init__(self):
        self.x=400
        self.y=400


class BulletNature:
    def __init__(self):
        self.x=15
        self.y=5
        self.speed=1
        self.color=(60,60,60)
        self.bullet_allowed=5
