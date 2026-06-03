class DisplaySize:
    def __init__(self):
        self.width=1200
        self.height=800

    def values(self):
        return self.width,self.height


class ScreenColor:
    def __init__(self):
        self.red=160
        self.green=120
        self.blue=100
    def color_change(self):
        self.red += 5
        self.green += 2
        self.blue += 13
        if self. red > 255 or self.green > 255 or self.blue > 255:
            self.red = self.green = self.blue = 0


class BulletNature:
    def __init__(self):
        self.x=40
        self.y=15
        self.color=(60,60,60)
        self.bullet_allowed=3


class AlienShip:
    def __init__(self):
        self.horizontal_direction=-1
        self.vertical_direction=-1
        self.ship_left=3


class DynamicSettings:
    def __init__(self):
        self.set_speed()

    def set_speed(self):
        self.bullet_speed = 3
        self.alien_speed = 1
        self.speedup_scale = 1.3

    def increase_speed(self):
        self.bullet_speed*=self.speedup_scale
        self.alien_speed*=self.speedup_scale
