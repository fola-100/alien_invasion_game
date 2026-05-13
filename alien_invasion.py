import game_functions as gf
import pygame
import controls
from ship import SpaceShip
from pygame.sprite import Group


def run_game():
    pygame.init()
    try:
        ship_image = pygame.image.load("assests/images/spaceship.png")
    except FileNotFoundError:
            print("File not found ensure correct file path is entered")
            return None
#-----Ship_image-----
    smooth_image=pygame.transform.smoothscale(ship_image,(90,90))
    rotated_image = pygame.transform.rotate(smooth_image, 120)

#-----Getting_Color_Control----
    color=controls.ScreenColor()

#------Getting_Screen_Control -----
    display=controls.DisplaySize()
    display_value=display.values()

# ----Getting_Ship_controls----
    ship=controls.ShipSize()
    ship_rect_x= ship.x
    ship_rect_y = ship.y

#-----Bullet_Controls----
    bullet_char=controls.BulletNature()

# ------Creating Ship------
    craft = SpaceShip(ship_rect_x, ship_rect_y, rotated_image)

#------Storage Bullets_Created-----
    bullets_fired=Group()

#------Creating Screen and Title
    screen = pygame.display.set_mode(display_value)
    pygame.display.set_caption("Alien_invasion")

    while True:
          gf.check_event(craft,bullets_fired,bullet_char,screen)
          gf.update_game(craft, color)
          bullets_fired.update()
          gf.update_screen(color,craft,rotated_image,screen,bullets_fired)
          gf.delete_bullet(bullets_fired,screen)


run_game()

