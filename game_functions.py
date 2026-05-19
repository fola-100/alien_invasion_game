import pygame
import sys
from bullet import Bullet

def check_event(craft,bullets,bullet_chars,screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # -----FIRE BULLET------
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
              if len(bullets)<bullet_chars.bullet_allowed:
                ammo = Bullet(bullet_chars, craft, screen)
                bullets.add(ammo)



def update_game(craft, color):
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

def get_alien_number(screen_size, ship_height):
    # ------Number of ship to create----
    available_alien_space = screen_size.height - (2 * ship_height)
    number_of_ship = int(available_alien_space / (2 * ship_height))
    return number_of_ship

def get_fleet_number(screen_size, alien_width, space_craft):

    available_flit_space=screen_size.width- (3 * alien_width + space_craft.rect.width)
    number_of_flit=int(available_flit_space/(2 *alien_width))
    return number_of_flit

def create_ships(number_of_ship, screen, image, alien_vessel, alien_height, created_vessel, alien_width, row_number, screen_width,settings):
    # -----Creating Ship For Display-----
    for alien_number in range(number_of_ship):
        craft = alien_vessel(image, screen,settings)
        craft.y = alien_height + 2 * alien_height * alien_number
        craft.x = screen_width - alien_width -( 2 * alien_width * row_number)
        craft.rect.y = craft.y
        craft.rect.x=craft.x
        created_vessel.add(craft)

def create_alien_fleet(alien_vessel, image, screen, aliens, space_craft, alien_settings):
    #----- Creating-Alien-Ship-----
    screen_size = screen.get_rect()
    craft = alien_vessel(image, screen,alien_settings)
    alien_height = craft.rect.height
    alien_width=craft.rect.width

    number_of_ship=get_alien_number(screen_size, alien_height)

    number_of_fleet = get_fleet_number(screen_size, alien_width, space_craft)

    for row_number in range(number_of_fleet):
     create_ships(number_of_ship, screen, image, alien_vessel, alien_height, aliens, alien_width, row_number, screen_size.width, alien_settings)

def change_fleet_direction(aliens,settings):
    for each_ship in aliens:
        each_ship.x+=settings.speed * settings.horizontal_direction
        each_ship.rect.x=each_ship.x
    settings.vertical_direction *= -1

def check_fleet_edge(alien_fleet,ship_control):
   for each_ship in alien_fleet:
       if each_ship.check_edge():
         change_fleet_direction(alien_fleet,ship_control)
         break

def check_collisions(bullets, aliens, aliens_settings, alien_vessel, image, screen, space_craft):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens)==0:
        bullets.empty()
        aliens_settings.speed+=0.5
        create_alien_fleet(alien_vessel,image,screen,aliens,space_craft,aliens_settings)


def update_alien_crafts(alien_ships, ship_control):
    check_fleet_edge(alien_ships, ship_control)
    alien_ships.update()


def update_screen(color, spaceship, ship_image, screen, bullet_fired, alien_ships, alien_ship_image):
    red = color.red
    green = color.green
    blue = color.blue
# -----Drawing On Screen------
    screen.fill((red, green, blue))
    rect = spaceship.rect
    screen.blit(ship_image, rect)
#-----Drawing Alien_Craft On Screen----
    for alien_craft in alien_ships:
      alien_rect=alien_craft.rect
      screen.blit(alien_ship_image,alien_rect)
#-----Drawing Bullet On Screen-----
    for bullet in bullet_fired:
        bullet.draw_bullet()

    pygame.display.flip()


def delete_bullet(bullet_fired,screen):
   screen_size=screen.get_rect()
   for each_bullet in  bullet_fired.copy():
       if each_bullet.rect.x> screen_size.right:
           each_bullet.kill()










