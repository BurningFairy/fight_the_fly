"""This file includes the main function."""
from resource_path import resource_path

import pygame
import random

from characters.character import Apple
from characters.enemies import Fly
from screens import gameWindow
from screens import startMenu
from screens import settingsWindow
import screens.gameWindow
import screens.settingsWindow
import screens.startMenu
import settings
from shop import items

apple_image = resource_path("assets/char_apple/Apple_back_cropped.png")
# creates an Object from the "Apple" Class
apple = Apple(apple_image,400, 400)

def enemy_create(x, y):
    """Create a new enemy at the given position. """
    fly_image=resource_path("assets/char_fly/Fly.png")
    return Fly(fly_image, x, y)

flies=[enemy_create(random.randint(0,600), random.randint(0,300)),
    enemy_create(random.randint(600,1200), random.randint(0,300)),
    enemy_create(random.randint(0,600), random.randint(300,700)),
    enemy_create(random.randint(600,1200), random.randint(300,700)),
    enemy_create(random.randint(0,1200), random.randint(0,700))]

level= 1

def update_game():
    """ Update all game objecst"""
    global flies
    keys = pygame.key.get_pressed()

    apple.handle_apple_movement(keys)
    apple.update_weapons(flies)

    for f in flies:
        f.handle_enemy_movement(apple)
    alive_flies = []
    for f in flies:
        if not f.is_dead():
            alive_flies.append(f)
            
    for f in flies:
        if apple.check_collision(f):
            return False
    
    
    flies = alive_flies

    if flies == []:
        global level
        level += 1
        added_flies=0
        flies= [enemy_create(random.randint(0,600), random.randint(0,300)),
            enemy_create(random.randint(600,1200), random.randint(0,300)),
            enemy_create(random.randint(0,600), random.randint(300,700)),
            enemy_create(random.randint(600,1200), random.randint(300,700))]
        while added_flies < level:
            flies.append(enemy_create(random.randint(0,1200), random.randint(0,700)))
            added_flies += 1

    return True
    
    
def main():
    """Define the main game loop."""
    clock = pygame.time.Clock()
    run = True
    timerStart = None
    
    gameState = "MENU"

    while run:
        clock.tick(settings.FPS)
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                run = False

        if gameState == "MENU":
            timerStart = None
            gameState = screens.startMenu.draw_startMenu(events)

        elif gameState == "GAME":
            if timerStart == None:
                timerStart = pygame.time.get_ticks()
            if not update_game(): #update_game returns False if character collides with enemy
                gameState = "MENU"
                timerStart = None
            else:
                gameWindow.draw_window(apple, flies, timerStart)


        elif gameState == "QUIT":
            run = False
        
        elif gameState == "SETTINGS":
            gameState = screens.settingsWindow.draw_settingsmenu(events)


        pygame.display.update()


if __name__ == "__main__":
    main()
