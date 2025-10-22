"""This file includes the main function."""
import pygame
from character import Apple
from enemies import Fly
import settings

# creates an Object from the "Apple" Class
apple = Apple("assets/char_apple/Apple_back_cropped.png", 100, 100)
enemy = Fly("assets/char_fly/Fly.png", 100, 100)


def draw_window():
    """Draw the charcter and the background on the screen."""
    settings.WINDOW.blit(settings.BG_IMAGE, (0, 0))  # inserts the BG_Image to the WINDOW
    apple.draw_apple(settings.WINDOW)  # calls the draw function from character.py
    enemy.draw_enemy(settings.WINDOW)
    pygame.display.update()


def main():
    """Define the main function of the game."""
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(settings.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        apple.handle_apple_movement(pygame.key.get_pressed(),
                                    settings.WIN_WIDTH, settings.WIN_HEIGHT)

        draw_window()


if __name__ == "__main__":
    main()
