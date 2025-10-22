"""This file cretes the enym class."""
import pygame

class Fly:
    """Represents the enemy character."""

    def __init__(self, image, x, y, height = 100, width = 100):
        """Constructs an Object of Enemy"""
        self.width = width
        self.height = height

        unscaled_image = pygame.image.load(image)
        self.image = pygame.transform.smoothscale(
            unscaled_image, (self.width, self.height))
        self.x = x
        self.y = y
        self.movespeed = 4
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw_enemy(self, window):
        """Draw the enemy onto the WINDOW surface."""
        window.blit(self.image, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def handle_enemy_movement(self, width, height, player_pos):
        """Handles the automatic movement of the enemy."""
        pass