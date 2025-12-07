"""This file contains the functions that draws the game window"""

import pygame

from characters.character import Apple
from characters.enemies import Fly
import settings
from shop.items import Cocktailpick,Flyswater,Bugspray


def draw_window(apple, enemy):
    """Draw the charcter and the background on the screen."""
    settings.WINDOW.blit(settings.BG_IMAGE, (0, 0))  # inserts the BG_Image to the WINDOW
    apple.draw_apple(settings.WINDOW)  # calls the draw function from character.py
    enemy.draw_enemy(settings.WINDOW) # calls the draw function from enemies.py
   
    apple.cocktailpick.draw(settings.WINDOW)
    apple.flyswater.draw(settings.WINDOW)
    apple.bugspray.draw(settings.WINDOW)

    pygame.display.update()
