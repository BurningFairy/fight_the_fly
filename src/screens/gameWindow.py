"""This file contains the functions that draws the game window"""

import pygame

from characters.character import Apple
from characters.enemies import Fly
import settings
#from shop.items import Cocktailpick,Flyswater,Bugspray

def draw_timer(timerStart):
    """
    Function that will draw the timer and make it count up endlessly
    """
    elapsedMs = pygame.time.get_ticks() - timerStart
    elapsedSec = elapsedMs // 1000

    minutes = elapsedSec // 60
    seconds = elapsedSec % 60

    timeText = f"{minutes:02}:{seconds:02}"
    font = pygame.font.Font(None, 40)
    textImage = font.render(timeText, True, "black")
    textRect = textImage.get_rect(center = (0, 0))

    settings.WINDOW.blit(textImage, (20, 20))

def draw_window(apple, enemy, timerStart):
    """Draw the charcter and the background on the screen."""
    settings.WINDOW.blit(settings.BG_IMAGE, (0, 0))  # inserts the BG_Image to the WINDOW
    apple.draw_apple(settings.WINDOW)  # calls the draw function from character.py

    draw_timer(timerStart)
    
    for en in enemy:
        en.draw_enemy(settings.WINDOW) # calls the draw function from enemies.py
   
    for weapon in apple.weapon_slots:
        if weapon:
            weapon.draw(settings.WINDOW)
    

    pygame.display.update()
