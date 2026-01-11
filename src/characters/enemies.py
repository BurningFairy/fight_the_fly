"""This file cretes the enym class."""
import pygame

import settings


class Fly:
    """Represents the enemy character."""

    def __init__(self, image, x, y, height = 100, width = 100, health=100):
        """Constructs an Object of Enemy"""
        self.width = width
        self.height = height
        self.health=health
        
        unscaled_image = pygame.image.load(image)
        self.image = pygame.transform.smoothscale(
            unscaled_image, (self.width, self.height))
        self.x = x
        self.y = y
        

        self.movespeed = 1
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_enemy(self, window):
        """Draw the enemy onto the WINDOW surface."""
        window.blit(self.image, (self.x, self.y))
        self.hitbox.update(self.x + 27, self.y + 37, self.width - 50, self.height - 65)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def handle_enemy_movement(self, player):
        """Handles the automatic movement of the enemy."""
        #while collision is FALSE:

         # up movement + restriction
        if (player.y < self.y
                and self.y - self.movespeed > 0):
            self.y -= self.movespeed

        # down movement
        if (player.y > self.y
                and self.y + self.height < settings.WIN_HEIGHT):
            self.y += self.movespeed

        # left movement
        if (player.x < self.x
                and self.x - self.movespeed > 0):
            self.x -= self.movespeed

        # right movement
        if (player.x > self.x 
                and self.x + self.movespeed + self.width < settings.WIN_WIDTH):
            self.x += self.movespeed

    def take_damage(self,damage):
        self.health-= damage

    def is_dead(self):
        return self.health <=0