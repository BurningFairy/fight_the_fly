"""This file is for Items ."""
import pygame



     #  function displayfor drawing item in slot

class Weapon:
     """Class for the basic functions for weapons."""
     def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 4)
        self.speed = 8
     
     def update(self):
        self.rect.x += self.speed

     def draw(self, screen):
          pygame.draw.rect(screen, (255, 255, 0), self.rect) 
class Flyswater(Weapon):
     """Class for the functions of Flyswater ."""
     pass

class Cocktailpick(Weapon):
     """Class for the basic functions for Accessories ."""
     pass

class Bugspray(Weapon):
     """Class for the basic functions for Accessories ."""
     pass

class Accessories():
     """Class for the basic functions for Accessories ."""
     pass