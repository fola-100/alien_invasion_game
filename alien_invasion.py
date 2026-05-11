import game_functions as gf
import pygame
import controls
from ship import SpaceShip
from pygame.sprite import Group


def run_game():
    pygame.init()
    try:
        ship_image = pygame.image.load("assests/images/spaceship.png")
        bullet_image = pygame.image.load("assests/images/bullet.png")
    except FileNotFoundError:
            print("File not found ensure correct file path is entered")
            return None
#-----Ship_image-----
    smooth_image=pygame.transform.smoothscale(ship_image,(90,90))
    rotated_image=pygame.transform.rotate(smooth_image,120)

#------bullet_image----
    smooth_bullet_image=pygame.transform.smoothscale(bullet_image,(25,25))

#-----Color_Variable----
    color=controls.ScreenColor(100,100,100)

#------ SCREEN SIZE-----
    display=controls.DisplaySize(1200,800)
    display_value=display.values()

# ----Ship_Size----
    ship_rect_x = 400
    ship_rect_y = 400

# ------Creating Ship------
    craft = SpaceShip(ship_rect_x, ship_rect_y, rotated_image)

#------Storage area for bullet-----
    bullets_fired=Group()


    screen = pygame.display.set_mode(display_value)
    pygame.display.set_caption("Alien_invasion")

    while True:
          gf.check_event()
          gf.update_game(craft, color,bullets_fired,smooth_bullet_image)
          bullets_fired.update()
          gf.update_screen(color,craft,rotated_image,screen,smooth_bullet_image,bullets_fired)


run_game()

