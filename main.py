import pygame
pygame.init()
 
FPS = 60
WIN_WIDTH = 1500
WIN_HEIGHT = 900
WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

pygame.display.set_caption("Fight The Fly")

class colors:
    white = (255, 255, 255)
    black = (0, 0, 0)

def draw_window():
    pass

def main():
    clock = pygame.time.Clock()
    run = True
    while run: 
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

    draw_window()

if __name__ == "__main__":
    main()