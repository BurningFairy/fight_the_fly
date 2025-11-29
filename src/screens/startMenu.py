"""This file contains the functions that draws the start menu"""

import pygame
pygame.init()

import settings

def draw_startMenu():
    button = pygame.Rect((settings.WIN_WIDTH/2 + 50, settings.WIN_HEIGHT/2 + 25), (100, 50))
    
    font = pygame.font.Font(None, 20)
    textSurface = font.render("START", True, (255, 255, 255))
    textRect = textSurface.get_rect(center = button.center)

    settings.WINDOW.blit(settings.BG_IMAGE, (0, 0))

    mousePosition = pygame.mouse.get_pos()

    if button.collidepoint(mousePosition):
        color = (70, 70, 70)
    else:
        color = (40, 40, 40)

    pygame.draw.rect(settings.WINDOW, color, button)
    settings.WINDOW.blit(textSurface, textRect)

    pygame.display.flip()


def update_startMenu(events):
    mousePosition = pygame.mouse.get_pos()

    button = pygame.Rect((settings.WIN_WIDTH/2 + 50, settings.WIN_HEIGHT/2 + 25), (100, 50))

    for event in events: 
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button.collidepoint(mousePosition):
                return "START"
