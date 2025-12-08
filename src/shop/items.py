"""This file is for Items ."""
import pygame
import math


     #  function displayfor drawing item in slot

class Weapon:
     """Class for the basic functions for weapons."""
     def __init__(self, apple_position):
          self.apple_position = apple_position
     
     def update_position(self,apple_position):
          self.apple_position = apple_position

     def use(self, direction):#platzhalter methode
          raise NotImplementedError
           
class Cocktailpick(Weapon):
     """Class for the functions of Cocktailpic ."""
     def __init__(self, apple_position,length=30, damage=100):
          super().__init__(apple_position)
          self.length = length
          self.damage = damage
          self.angle = 0

     def use(self, direction):
          self.angle = math.degrees(math.atan2(direction[1], direction[0]))
          # da noch schaden übergeben für gegner bei hit
     
     def change_direction(self, direction):# damit s gelich in die richtige richtung schaut
          self.angle =   math.degrees(math.atan2(direction[1], direction[0]))

     def draw (self, window):
          end_x = self.apple_position[0]+math.cos(math.radians(self.angle)) * self.length
          end_y = self.apple_position[1]+math.sin(math.radians(self.angle)) * self.length

          pygame.draw.line(window,(255,0,0), self.apple_position, (end_x, end_y),10) #todo durch bild erstzen

class Flyswater(Weapon):
     """Class for the functions of Flyswater ."""
     def __init__(self, apple_position,length=60, damage=123):
          super().__init__(apple_position)
          self.length = length
          self.damage = damage
          self.angle = 0

     def use(self, direction):
          self.angle = math.degrees(math.atan2(direction[1], direction[0]))
          # da noch schaden übergeben für gegner bei hit
     
     def change_direction(self, direction):# damit s gelich in die richtige richtung schaut
          self.angle =   math.degrees(math.atan2(direction[1], direction[0]))

     def draw (self, window):
          end_x = self.apple_position[0]+math.cos(math.radians(self.angle)) * self.length
          end_y = self.apple_position[1]+math.sin(math.radians(self.angle)) * self.length
          
          pygame.draw.line(window,(255,255,0), self.apple_position, (end_x, end_y),6) #todo durch bild erstzen


class Bugspray(Weapon):
     """Class for the  functions of Bugspray."""
     def __init__(self, apple_position,projectile_speed = 8, damage=60):
          super().__init__(apple_position)
          self.projectile_speed = projectile_speed 
          self.projectiles =[]

     def use( self, direction):
          velocity = (direction [0]* self.projectile_speed,
                      direction [1]* self.projectile_speed)
          self.projectiles.append({
               "pos": list(self.apple_position) ,
               "vel": velocity
          })
       # da noch schaden übergeben für gegner bei hit
     
     def update(self):
          for p in self.projectiles:
               p["pos"][0] += p["vel"][0]
               p["pos"][1] += p["vel"][1]

     def draw(self, window) :
          for p in self.projectiles:
               pygame.draw.circle(window, (0, 255, 0),
                                  (int(p["pos"][0]), int(p["pos"][1])),5)
                              
     def change_direction(self, direction):# damit s gelich in die richtige richtung schaut
          self.angle =   math.degrees(math.atan2(direction[1], direction[0]))

class Accessories():
     """Class for the basic functions for Accessories ."""
     pass