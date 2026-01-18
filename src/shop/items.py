"""
items.py

This module contains all weapon and item classes for the game.
It includes melee weapons, ranged weapons, and accessories.
"""
import pygame
import math


     #  function displayfor drawing item in slot

class Weapon:
     """
    Base class for all weapons.

    Every weapon has a position and a use() method.
     """
     def __init__(self, apple_position):
          """create Weapon"""
          self.apple_position = apple_position
     
     def update_position(self,apple_position):# damit waffen am Character
          """ Update the weapon position.
        This keeps the weapon attached to the player. """
          self.apple_position = apple_position

     def use(self, direction):#platzhalter methode
          """placeholder-> implemented in Childclasses"""
          raise NotImplementedError

class MeleeWeapon(Weapon): 
     """
    Bass class for melee weapons.

    Melee weapons hit enemies in front of the player.
    """    
     def __init__(self, apple_position,):
          """  Constructs MeleeWeapon"""
          super().__init__(apple_position)
          self.angle = 0# Weapon direction in degrees

     def use(self, direction):
          """ Use the melee weapon.
          Converts movement direction into an angle. """
          self.angle = math.degrees(math.atan2(direction[1], direction[0]))#letzte beweguung in winkel berechnen
        
   
     def draw (self, window):
          """draw the the meleweapon """
          end_x = self.apple_position[0]+math.cos(math.radians(self.angle)) * self.length#
          end_y = self.apple_position[1]+math.sin(math.radians(self.angle)) * self.length

          pygame.draw.line(window,(0,255,255), self.apple_position, (end_x, end_y),10) #todo durch bild erstzen

     def check_hit(self, enemies):
          """check if eneny is hit by weapon"""
          end_x = self.apple_position[0]+math.cos(math.radians(self.angle)) * self.length#wo zeigt waffe hin länge + Winkel
          end_y = self.apple_position[1]+math.sin(math.radians(self.angle)) * self.length

          weapon_line= pygame.Rect(# Create a rectangle around the weapon line as hitbox
               min(self.apple_position[0], end_x),
               min(self.apple_position[1], end_y),
               abs(end_x-self.apple_position[0])+1,
               abs(end_y-self.apple_position[1])+1,
          )
          for enemy in enemies:
               if enemy.hitbox.colliderect(weapon_line):
                    enemy.take_damage(self.damage)

class Cocktailpick(MeleeWeapon):
     """Class for the functions of Cocktailpic ."""
     def __init__(self, apple_position,length=30, damage=100):
          """Constructs Cocktailpick"""         
          super().__init__(apple_position)
          self.length = length
          self.damage = damage
          self.angle = 0

 

class Flyswater(MeleeWeapon):
     """Class for the functions of Flyswater ."""
     def __init__(self, apple_position,length=60, damage=123):
          """Constructs Flyswater"""           
          super().__init__(apple_position)
          self.length = length
          self.damage = damage
          self.angle = 0


class RangedWeapon(Weapon):
      """Bass class for ranged Weapons"""
      def __init__(self, apple_position,projectile_speed, damage,fire_intervall=1000):
          """Constructs RangedWeapon"""
          super().__init__(apple_position)
          self.projectile_speed = projectile_speed 
          self.damage=damage
          self.projectiles =[]    

          #for Autfire:
          self.fire_intervall = fire_intervall    #
          self.last_shot_time = 0

      def auto_fire(self,direction):
           """shoot automatically after defined time"""
           current_time=pygame.time.get_ticks()
           if current_time -self.last_shot_time >= self.fire_intervall:
                self.use(direction)
                self.last_shot_time = current_time

      def use( self, direction):# erzeugt kugel an spielerposition
          """ctreate projectil at appleposition"""
          velocity = (direction [0]* self.projectile_speed,
                      direction [1]* self.projectile_speed)
          self.projectiles.append({
               "pos": list(self.apple_position) ,
               "vel": velocity
          })          
      def update(self,enemies):# bewegung der kugel
          """Update bulletmovment and check collisions"""
          for p in self.projectiles:
               p["pos"][0] += p["vel"][0]
               p["pos"][1] += p["vel"][1]

               for enemy in enemies:
                    if enemy.hitbox.collidepoint(int(p["pos"][0]), int(p["pos"][1])):
                         enemy.take_damage(self.damage)
                         self.projectiles.remove(p)
                         break             
                           
      def draw(self, window):
          """Draw all Bullets"""
          for p in self.projectiles:
               pygame.draw.circle(
                    window,
                    (0, 0, 255),
                    (int(p["pos"][0]), int(p["pos"][1])),
                    5  # feste Größe
               )                   
class Bugspray(RangedWeapon):
     """Class for the  functions of Bugspray."""
     def __init__(self, apple_position,):
          """Constructs Bugspray"""            
          super().__init__(apple_position,projectile_speed = 10,damage = 100)
        
          
class FastGun(RangedWeapon):
     """Class for the  functions of FastGun."""
     def __init__(self, apple_position,):
          """Constructs FAstgun"""               
          super().__init__(apple_position,projectile_speed = 20,damage = 50)
      

class StrongGun(RangedWeapon):
          """Class for the  functions of StrongGun."""
          def __init__(self, apple_position,):
               """Constructs Strongun"""
               super().__init__(apple_position,projectile_speed = 5,damage = 150)
             

class Accessories():
     """Class for the basic functions for Accessories ."""
     pass