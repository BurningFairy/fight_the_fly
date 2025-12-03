"""This file includes the main function."""
import pygame

from characters.character import Apple
from characters.enemies import Fly
from screens import gameWindow
import screens.startMenu
import settings

# creates an Object from the "Apple" Class5
apple = Apple("assets/char_apple/Apple_back_cropped.png", 400, 400)
fly = Fly("assets/char_fly/Fly.png", 100, 100)

def update_game():
    keys = pygame.key.get_pressed()
    apple.handle_apple_movement(keys, settings.WIN_WIDTH, settings.WIN_HEIGHT)

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
            screens.startMenu.draw_startMenu()
            gameState = screens.startMenu.logic_startMenu(events)

        elif gameState == "GAME":
            update_game()
            gameWindow.draw_window(apple, fly)


if __name__ == "__main__":
    main()