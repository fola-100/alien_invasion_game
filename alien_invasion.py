import game_functions as gf
import pygame
import controls
from ship import SpaceShip
from pygame.sprite import Group
from alien_ship import AlienCraft
from game_stats import GameStats
from button import Button

def run_game():
    pygame.init()
    try:
        ship_image = pygame.image.load("assests/images/spaceship.png")
        alien_vessel_image=pygame.image.load("assests/images/alien_space_craft.png")
    except FileNotFoundError:
            print("File not found ensure correct file path is entered")
            return None
#-----Ship_image-----
    smooth_image=pygame.transform.smoothscale(ship_image,(90,90))
    rotated_image = pygame.transform.rotate(smooth_image, 120)
    smooth_alien_image=pygame.transform.smoothscale(alien_vessel_image,(70,70))

#-----Getting_Color_Control----
    color=controls.ScreenColor()

#------Getting_Screen_Control -----
    display=controls.DisplaySize()
    display_value=display.values()

#-----Bullet_Controls----
    bullet_char=controls.BulletNature()

#-----Alien_Ship_Controls-----
    alien_controls=controls.AlienShip()

# -----Object_speed_Controls------
    speed = controls.DynamicSettings()

# -----Game_Controls-----
    game_control = GameStats(alien_controls)

#------Storage Bullets_Created-----
    bullets_fired=Group()

#-----STORE ALIEN_VESSEL-----
    aliens= Group()

#------Creating Screen and Title
    screen = pygame.display.set_mode(display_value)
    pygame.display.set_caption("Alien_invasion")

# -----Creating Start button-----
    play_button=Button(screen, "PLAY")

# ------Creating Rocket_Ship------
    craft = SpaceShip(rotated_image, screen)

# -----Creating Alien-SpaceCraft------
    gf.create_alien_fleet(AlienCraft, smooth_alien_image, screen, aliens, craft,alien_controls,speed)


    while True:
        gf.check_event(craft, bullets_fired, bullet_char, screen, play_button, game_control, aliens, AlienCraft,
                       smooth_alien_image, alien_controls,speed)

        if game_control.game_active:
          gf.update_game(craft, color,game_control)
          bullets_fired.update()
          gf.collisions(bullets_fired, aliens, alien_controls, AlienCraft, smooth_alien_image, screen, craft,game_control,speed)
          gf.update_alien_crafts(aliens, alien_controls, game_control,speed)
          gf.delete_bullet(bullets_fired, screen)

        gf.update_screen(color, craft, rotated_image, screen, bullets_fired, aliens, smooth_alien_image, play_button,
                         game_control)
run_game()

