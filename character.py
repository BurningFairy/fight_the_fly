import pygame

class Apple: 
    def __init__(apple, image, x, y):
        apple.image = pygame.image.load(image)
        apple.x = x
        apple.y = y

    def draw_apple(apple, window):
        window.blit(apple.image, (apple.x, apple.y))
