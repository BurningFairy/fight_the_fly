"""This file is for the playable character."""
import pygame


class Apple:
    """Represents the playable character."""

    def __init__(self, image, x, y, height=100, width=100):
        """Construct an Object of Apple."""
        self.width = height
        self.height = width

        unscaled_image = pygame.image.load(image)
        self.image = pygame.transform.smoothscale(
            unscaled_image, (self.width, self.height))
        self.x = x
        self.y = y
        self.movespeed = 5

    def draw_apple(self, window):
        """Draw the char onto the WINDOW surface."""
        window.blit(self.image, (self.x, self.y))

    def handle_apple_movement(self, keys, width, height):
        """Handle the movement of the character."""
        # move up + restriction
        if (self.y - self.movespeed > 0
                and (keys[pygame.K_UP] or keys[pygame.K_w])):
            self.y -= self.movespeed

        # move down + restriction
        if (self.y + self.movespeed + self.height < height
                and (keys[pygame.K_DOWN] or keys[pygame.K_s])):
            self.y += self.movespeed

        # move left + restriction
        if (self.x - self.movespeed > 0
                and (keys[pygame.K_LEFT] or keys[pygame.K_a])):
            self.x -= self.movespeed

        # move right + restriction
        if (self.x + self.movespeed + self.width < width
                and (keys[pygame.K_RIGHT] or keys[pygame.K_d])):
            self.x += self.movespeed
