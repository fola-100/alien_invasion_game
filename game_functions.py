import pygame
import sys
from time import sleep
from bullet import Bullet
def check_event(space_rocket, bullets, bullet_chars, screen,play_button,game_stat,aliens,alien_vessel,image,aliens_settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # -----FIRE BULLET------
        if  event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
              if len(bullets)<bullet_chars.bullet_allowed:
                ammo = Bullet(bullet_chars, space_rocket, screen)
                bullets.add(ammo)
        #------Start game-----
        if event.type==pygame.MOUSEBUTTONDOWN:
           mouse_x, mouse_y=pygame.mouse.get_pos()
           check_play_button(play_button,game_stat,mouse_x,mouse_y,bullets,aliens,alien_vessel,image,screen,space_rocket,aliens_settings)

def check_play_button(play_button,game_stat,mouse_x, mouse_y,bullets,aliens,alien_vessel,image,screen,space_rocket,aliens_settings):
    if play_button.rect.collidepoint(mouse_x,mouse_y):

        game_stat.game_active = True
        game_stat.reset()

        bullets.empty()
        aliens.empty()

        create_alien_fleet(alien_vessel, image, screen, aliens, space_rocket, aliens_settings)
        space_rocket.reset_position()




def update_game(space_rocket, color,game_stat):
  if game_stat.game_active:
    keys = pygame.key.get_pressed()
    # ----LEFT AND RIGHT MOVEMENT---------
    if keys[pygame.K_f]:
        space_rocket.move_left()
    if keys[pygame.K_j]:
        space_rocket.move_right()
    # ----UP AND DOWN MOVEMENT-----
    if keys[pygame.K_y]:
        space_rocket.move_up()
    if keys[pygame.K_b]:
        space_rocket.move_down()
    # ----CHANGE_BACKGROUND_COLOR------
    if keys[pygame.K_r]:
        color.color_change()

    # -----LEFT AND RIGHT BOUNDARY------
    if 0 > space_rocket.rect.x:
        space_rocket.rect.x = 1

    elif space_rocket.rect.x > 1090:
        space_rocket.rect.x = 1090

    # -----UP AND DOWN BOUNDARY-----
    if 0 > space_rocket.rect.y:
        space_rocket.rect.y = 1

    elif space_rocket.rect.y > 720:
        space_rocket.rect.y = 720

def get_alien_number(screen_size, ship_height):
    # ------Number of ship to create----
    available_alien_space = screen_size.height - (2 * ship_height)
    number_of_ship = int(available_alien_space / (2 * ship_height))
    return number_of_ship

def get_fleet_number(screen_size, alien_width, space_rocket):

    available_flit_space=screen_size.width- (3 * alien_width + space_rocket.rect.width)
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

def create_alien_fleet(alien_vessel, image, screen, aliens, space_rocket, alien_settings):
    #----- Creating-Alien-Ship-----
    screen_size = screen.get_rect()
    craft = alien_vessel(image, screen,alien_settings)
    alien_height = craft.rect.height
    alien_width=craft.rect.width

    number_of_ship=get_alien_number(screen_size, alien_height)

    number_of_fleet = get_fleet_number(screen_size, alien_width, space_rocket)

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

def bullet_collision(bullets,aliens,aliens_settings, alien_vessel, image, screen, space_rocket):
    alien_collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens)==0:
        bullets.empty()
        aliens_settings.speed+=0.5
        create_alien_fleet(alien_vessel, image, screen, aliens, space_rocket, aliens_settings)

def live_left(game_stats):
    if game_stats.ship_left<=0:
        game_stats.game_active=False

def ship_hit(aliens_settings,bullets,aliens,alien_vessel,image,screen,space_rocket,game_stats):
    if pygame.sprite.spritecollide(space_rocket, aliens, True):
        sleep(0.5)
        game_stats.ship_left -= 1

        live_left(game_stats)

        if game_stats.game_active:
            bullets.empty()
            aliens.empty()

            create_alien_fleet(alien_vessel, image, screen, aliens, space_rocket, aliens_settings)

            space_rocket.reset_position()


def check_alien_bottom(aliens,screen,alien_vessel,image,space_rocket,aliens_settings,game_stats,bullets):
    screen_size=screen.get_rect()

    for alien in aliens:
        if screen_size.left >= alien.rect.left:
           sleep(0.5)

           game_stats.ship_left -= 1

           live_left(game_stats)
           if game_stats.game_active:
               bullets.empty()
               aliens.empty()

               create_alien_fleet(alien_vessel, image, screen, aliens, space_rocket, aliens_settings)
               space_rocket.reset_position()
               break



def collisions(bullets, aliens, aliens_settings, alien_vessel, image, screen, space_rocket, game_stats):

    bullet_collision(bullets,aliens,aliens_settings, alien_vessel, image, screen, space_rocket)

    ship_hit(aliens_settings,bullets,aliens,alien_vessel,image,screen,space_rocket,game_stats)

    check_alien_bottom(aliens,screen,alien_vessel,image,space_rocket,aliens_settings,game_stats,bullets)





def update_alien_crafts(alien_ships, ship_control,game_control):
   if game_control.game_active:
    check_fleet_edge(alien_ships, ship_control)
    alien_ships.update()


def update_screen(color, space_rocket, ship_image, screen, bullet_fired, alien_ships, alien_ship_image,button,game_stat):
    red = color.red
    green = color.green
    blue = color.blue
# -----Drawing On Screen------
    screen.fill((red, green, blue))
    rect = space_rocket.rect
    screen.blit(ship_image, rect)
#-----Drawing Alien_Craft On Screen----
    for alien_craft in alien_ships:
      alien_rect=alien_craft.rect
      screen.blit(alien_ship_image,alien_rect)
#-----Drawing Bullet On Screen-----
    for bullet in bullet_fired:
        bullet.draw_bullet()

# ------Start Button-----
    if not game_stat.game_active:
            button.draw_button()

    pygame.display.flip()


def delete_bullet(bullet_fired,screen):
   screen_size=screen.get_rect()
   for each_bullet in  bullet_fired.copy():
       if each_bullet.rect.x> screen_size.right:
           each_bullet.kill()










