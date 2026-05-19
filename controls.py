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


class BulletNature:
    def __init__(self):
        self.x=15
        self.y=300
        self.speed=3
        self.color=(60,60,60)
        self.bullet_allowed=5


class AlienShip:
    def __init__(self):
        self.speed = 1
        self.horizontal_direction=-1
        self.vertical_direction=-1
