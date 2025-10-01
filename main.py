import pygame
from character import Apple
pygame.init()
 
FPS = 60
WIN_WIDTH = 1500
WIN_HEIGHT = 800
WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

pygame.display.set_caption("Fight The Fly")

# creates an Object from the "Apple" Class 
apple = Apple("assets/apple_back_cropped.png", 100, 100)

# sets path and scales the BG-image to the WINDOW size
BG_IMAGE = pygame.transform.smoothscale(pygame.image.load("assets/BG_Test.png"), (WIN_WIDTH, WIN_HEIGHT))

class colors:
    white = (255, 255, 255)
    black = (0, 0, 0)

def draw_window():
    WINDOW.blit(BG_IMAGE, (0,0)) # inserts the BG_Image to the WINDOW
    apple.draw_apple(WINDOW) # calls the draw function from character.py
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run: 
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        apple.handle_apple_movement(pygame.key.get_pressed(), WIN_WIDTH, WIN_HEIGHT)

        draw_window()

if __name__ == "__main__":
    main()