"""This file includes the main function."""
import pygame

from characters.character import Apple
from characters.enemies import Fly
from screens import gameWindow
import screens.startMenu
import settings
from shop import items


# creates an Object from the "Apple" Class
apple = Apple("assets/char_apple/Apple_back_cropped.png", 400, 400)
flies=[Fly("assets/char_fly/Fly.png", 100, 100),
       Fly("assets/char_fly/Fly.png", 200, 200),
       Fly("assets/char_fly/Fly.png", 300, 500),
       Fly("assets/char_fly/Fly.png", 300, 600),
       Fly("assets/char_fly/Fly.png", 400, 300),
       Fly("assets/char_fly/Fly.png", 500, 300)]

def update_game():
    global flies
    keys = pygame.key.get_pressed()
    apple.handle_apple_movement(keys)
    apple.update_wapons(flies)
    for f in flies:
        f.handle_enemy_movement(apple)
    alive_flies=[]
    for f in flies:
        if not f.is_dead():
            alive_flies.append(f)
    flies=alive_flies

    
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

        pygame.display.update()


if __name__ == "__main__":
    main()