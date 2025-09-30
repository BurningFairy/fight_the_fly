import pygame
from character import Apple
pygame.init()
 
FPS = 60
WIN_WIDTH = 1500
WIN_HEIGHT = 800
WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

pygame.display.set_caption("Fight The Fly")

apple = Apple("assets/Apple_back.png", 100, 100)
BG = pygame.image.load("assets/BG_Test.png")

class colors:
    white = (255, 255, 255)
    black = (0, 0, 0)

def draw_window(background):
    WINDOW = pygame.Surface.blit(background)
    apple.draw_apple(WINDOW)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run: 
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        apple.handle_apple_movement(keys)

        draw_window(BG)

if __name__ == "__main__":
    main()