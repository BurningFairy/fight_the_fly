import pygame

class Apple: 
    def __init__(apple, image, x, y):
        apple.width = 100
        apple.height = 100

        unscaled_image = pygame.image.load(image)
        apple.image = pygame.transform.smoothscale(unscaled_image, (apple.width, apple.height))
        apple.x = x
        apple.y = y
        apple.movespeed = 5

    def draw_apple(apple, window):
        window.blit(apple.image, (apple.x, apple.y))

    def handle_apple_movement(apple, keys):
        if keys[pygame.K_UP]:
            apple.y -= apple.movespeed
        if keys[pygame.K_DOWN]:
            apple.y += apple.movespeed
        if keys[pygame.K_LEFT]:
            apple.x -= apple.movespeed
        if keys[pygame.K_RIGHT]:
            apple.x += apple.movespeed

        if keys[pygame.K_w]:
            apple.y -= apple.movespeed
        if keys[pygame.K_s]:
            apple.y += apple.movespeed
        if keys[pygame.K_a]:
            apple.x -= apple.movespeed
        if keys[pygame.K_d]:
            apple.x += apple.movespeed
