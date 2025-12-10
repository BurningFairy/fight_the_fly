import pygame
pygame.init()

import settings

def draw_button(text, width, height, textcolor, centerX, centerY):

    button = pygame.Rect((0, 0), (width, height))
    button.center = ((centerX, centerY))

    mousePosition = pygame.mouse.get_pos()

    if button.collidepoint(mousePosition):
        color = (90, 90, 90)
    else:
        color = (50, 50, 50)

    pygame.draw.rect(settings.WINDOW, color, button)
    font = pygame.font.Font(None, 20)
    textImage = font.render(text, True, textcolor)
    textCenter = textImage.get_rect(center = button.center)
    settings.WINDOW.blit(textImage, textCenter)

    return button


def draw_startMenu(events):
    settings.WINDOW.blit(settings.BG_IMAGE, (0, 0))

    startButton = draw_button("START", 100, 50, (255, 255, 255), settings.WIN_WIDTH // 2, settings.WIN_HEIGHT // 2 - 100)
    quitButton = draw_button("QUIT", 100, 50, (255, 255, 255), settings.WIN_WIDTH // 2, settings.WIN_HEIGHT // 2 - 25)


    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if startButton.collidepoint(event.pos):
                return "GAME"
            if quitButton.collidepoint(event.pos):
                return "QUIT"
    
    return "MENU"
    
    