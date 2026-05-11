import pygame
import sys
from bullet import Bullet

def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_game(craft, color, bullets, bullet_image):
    keys = pygame.key.get_pressed()
    # ----LEFT AND RIGHT MOVEMENT---------
    if keys[pygame.K_f]:
        craft.move_left()
    if keys[pygame.K_j]:
        craft.move_right()
    # ----UP AND DOWN MOVEMENT-----
    if keys[pygame.K_y]:
        craft.move_up()
    if keys[pygame.K_b]:
        craft.move_down()
    # ----CHANGE_BACKGROUND_COLOR------
    if keys[pygame.K_r]:
        color.color_change()
    # -----FIRE BULLET------
    if keys[pygame.K_SPACE]:
        ammo =Bullet(1, bullet_image, craft)
        bullets.add(ammo)

    # -----LEFT AND RIGHT BOUNDARY------
    if 0 > craft.rect.x:
        craft.rect.x = 1

    elif craft.rect.x > 1090:
        craft.rect.x = 1090

    # -----UP AND DOWN BOUNDARY-----
    if 0 > craft.rect.y:
        craft.rect.y = 1

    elif craft.rect.y > 720:
        craft.rect.y = 720

def update_screen(color,spaceship,ship_image,screen,bullet_image,bullet_fired):
    red = color.red
    green = color.green
    blue = color.blue
    # -----------Drawing On Screen------
    screen.fill((red, green, blue))
    rect = spaceship.rect
    screen.blit(ship_image, rect)
    for bullet in bullet_fired:
        screen.blit(bullet_image,bullet.rect)
    pygame.display.flip()


def delete_bullet(bullet_fired,screen):
   for each_bullet in  bullet_fired:
       if each_bullet.rect.x> screen.










