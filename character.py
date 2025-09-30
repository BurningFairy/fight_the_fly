import pygame

class Apple: 
    def __init__(apple, image, x, y, height = 100, width = 100):
        apple.width = height
        apple.height = width

        unscaled_image = pygame.image.load(image)
        apple.image = pygame.transform.smoothscale(unscaled_image, (apple.width, apple.height))
        apple.x = x
        apple.y = y
        apple.movespeed = 5

    def draw_apple(apple, window):
        window.blit(apple.image, (apple.x, apple.y)) # draws the char onto the WINDOW surface

    def handle_apple_movement(apple, keys, width, height):

        # move up + restriction
        if apple.y - apple.movespeed > 0 and (keys[pygame.K_UP] or keys[pygame.K_w]):
            apple.y -= apple.movespeed

        # move down + restriction
        if apple.y + apple.movespeed + apple.height < height and (keys[pygame.K_DOWN] or keys[pygame.K_s]):
            apple.y += apple.movespeed

        # move left + restriction
        if apple.x - apple.movespeed > 0 and (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            apple.x -= apple.movespeed

        # move right + restriction
        if apple.x + apple.movespeed + apple.width < width and (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            apple.x += apple.movespeed

        
