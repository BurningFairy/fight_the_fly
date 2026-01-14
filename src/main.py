"""This file includes the main function."""

    

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


# creates an Object from the "Apple" Class
apple = Apple("assets/char_apple/Apple_back_cropped.png", 400, 400)

# creates random coordinates, that will be used to set the spawn-point of the enemies
ax= random.randint(0,600)
ay= random.randint(0,300)
bx= random.randint(600,1200)
by= random.randint(0,300)
cx= random.randint(0,600)
cy= random.randint(300,700)
dx= random.randint(600,1200)
dy= random.randint(300,700)
rx= random.randint(0,1200)
ry= random.randint(0,700)


def enemy_create(x, y):
    return Fly("assets/char_fly/Fly.png", x, y)

flies=[enemy_create(ax, ay),
    enemy_create(bx, by),
    enemy_create(cx, cy),
    enemy_create(dx, dy),
    enemy_create(rx, ry)]

def update_game():
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
    
    flies = alive_flies

    ax= random.randint(0,600)
    ay= random.randint(0,300)
    bx= random.randint(600,1200)
    by= random.randint(0,300)
    cx= random.randint(0,600)
    cy= random.randint(300,700)
    dx= random.randint(600,1200)
    dy= random.randint(300,700)
    rx= random.randint(0,1200)
    ry= random.randint(0,700)

    if flies == []:
        flies= [enemy_create(ax, ay),
    enemy_create(bx, by),
    enemy_create(cx, cy),
    enemy_create(dx, dy),
    enemy_create(rx, ry)]
    
def main():
    """Define the main function of the game."""
    clock = pygame.time.Clock()
    run = True

    gameState = "MENU"

    while run:
        clock.tick(settings.FPS)
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                run = False

        if gameState == "MENU":
            screens.startMenu.draw_startMenu(events)
            gameState = screens.startMenu.draw_startMenu(events)

        elif gameState == "GAME":
            update_game()
            gameWindow.draw_window(apple, flies)

        elif gameState == "QUIT":
            run = False
        
        elif gameState == "SETTINGS":
            screens.settingsWindow.draw_settingsmenu(events)
            
            gameState = screens.settingsWindow.draw_settingsmenu(events)


        pygame.display.update()


if __name__ == "__main__":
    main()