import pygame

class Enemy:
    def __init__(enemy, image, x, y, height = 100, width = 100):
        enemy.width = width
        enemy.height = height

        unscaled_image = pygame.image.load(image)
        enemy.image = pygame.transform.smoothscale(unscaled_image, (enemy.width, enemy.height))
        enemy.x = x
        enemy.y = y