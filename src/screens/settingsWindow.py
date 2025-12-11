"""
    This file contains the settings menu
"""

import pygame
import settings
import screens.startMenu
pygame.init()



def draw_settingsmenu(events):
    settings.WINDOW.blit(settings.BG_IMAGE, (0, 0))

    testButton = screens.startMenu.draw_button("TEST", 50, 50, (255, 255, 255),
        settings.WIN_WIDTH // 2 + 100, settings.WIN_HEIGHT // 2 - 100)
    closeButton = screens.startMenu.draw_button("CLOSE", 50, 50, (255, 255, 255), 
        settings.WIN_WIDTH // 2  - 100, settings.WIN_HEIGHT // 2 - 100)

    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if closeButton.collidepoint(event.pos):
                return "MENU"

    return "SETTINGS"
