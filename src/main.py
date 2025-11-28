"""This file includes the main function."""
import pygame

from characters.character import Apple
from screens import gameWindow
import settings

# creates an Object from the "Apple" Class
apple = Apple("assets/char_apple/Apple_back_cropped.png", 100, 100)

def update_game():
    keys = pygame.key.get_pressed()
    apple.handle_apple_movement(keys, settings.WIN_WIDTH, settings.WIN_HEIGHT)

def main():
    """Define the main function of the game."""
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(settings.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        update_game()
        gameWindow.draw_window(apple)


if __name__ == "__main__":
    main()
