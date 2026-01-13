"""This file is for Items ."""
import pygame
import math


     #  function displayfor drawing item in slot

class Weapon:
     """Class for the basic functions for weapons."""
     def __init__(self, apple_position):
          self.apple_position = apple_position
     
     def update_position(self,apple_position):# damit waffen am Character
          self.apple_position = apple_position

     def use(self, direction):#platzhalter methode
          raise NotImplementedError

class MeleeWeapon(Weapon): 
     def __init__(self, apple_position,):
          super().__init__(apple_position)
          self.angle = 0

     def use(self, direction):
          self.angle = math.degrees(math.atan2(direction[1], direction[0]))#letzte beweguung in winkel berechnen
        
     def change_direction(self, direction):# damit s gleich in die richtige richtung schaut
          self.angle =   math.degrees(math.atan2(direction[1], direction[0]))

     def draw (self, window):
          end_x = self.apple_position[0]+math.cos(math.radians(self.angle)) * self.length
          end_y = self.apple_position[1]+math.sin(math.radians(self.angle)) * self.length

          pygame.draw.line(window,(0,255,255), self.apple_position, (end_x, end_y),10) #todo durch bild erstzen

     def check_hit(self, enemies):
          end_x = self.apple_position[0]+math.cos(math.radians(self.angle)) * self.length
          end_y = self.apple_position[1]+math.sin(math.radians(self.angle)) * self.length

          weapon_line= pygame.Rect(
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
          super().__init__(apple_position)
          self.length = length
          self.damage = damage
          self.angle = 0

     # def use(self, direction):
     #      self.angle = math.degrees(math.atan2(direction[1], direction[0]))#letzte beweguung in winkel berechnen
        
     # def change_direction(self, direction):# damit s gleich in die richtige richtung schaut
     #      self.angle =   math.degrees(math.atan2(direction[1], direction[0]))

     # def draw (self, window):
     #      end_x = self.apple_position[0]+math.cos(math.radians(self.angle)) * self.length
     #      end_y = self.apple_position[1]+math.sin(math.radians(self.angle)) * self.length

     #      pygame.draw.line(window,(255,0,0), self.apple_position, (end_x, end_y),10) #todo durch bild erstzen

     # def check_hit(self, enemies):
     #      end_x = self.apple_position[0]+math.cos(math.radians(self.angle)) * self.length
     #      end_y = self.apple_position[1]+math.sin(math.radians(self.angle)) * self.length

     #      weapon_line= pygame.Rect(
     #           min(self.apple_position[0], end_x),
     #           min(self.apple_position[1], end_y),
     #           abs(end_x-self.apple_position[0])+1,
     #           abs(end_y-self.apple_position[1])+1,
     #      )
     #      for enemy in enemies:
     #           if enemy.hitbox.colliderect(weapon_line):
     #                enemy.take_damage(self.damage)

class Flyswater(MeleeWeapon):
     """Class for the functions of Flyswater ."""
     def __init__(self, apple_position,length=60, damage=123):
          super().__init__(apple_position)
          self.length = length
          self.damage = damage
          self.angle = 0

     # def use(self, direction):
     #      self.angle = math.degrees(math.atan2(direction[1], direction[0]))
     #      # da noch schaden übergeben für gegner bei hit
     
     # def change_direction(self, direction):# damit s gelich in die richtige richtung schaut
     #      self.angle =   math.degrees(math.atan2(direction[1], direction[0]))

     # def draw (self, window):
     #      end_x = self.apple_position[0]+math.cos(math.radians(self.angle)) * self.length
     #      end_y = self.apple_position[1]+math.sin(math.radians(self.angle)) * self.length
          
     #      pygame.draw.line(window,(255,255,0), self.apple_position, (end_x, end_y),6) #todo durch bild erstzen
     
     # def check_hit(self, enemies):
     #      end_x = self.apple_position[0]+math.cos(math.radians(self.angle)) * self.length
     #      end_y = self.apple_position[1]+math.sin(math.radians(self.angle)) * self.length

     #      weapon_line= pygame.Rect(
     #           min(self.apple_position[0], end_x),
     #           min(self.apple_position[1], end_y),
     #           abs(end_x-self.apple_position[0])+1,
     #           abs(end_y-self.apple_position[1])+1,
     #      )
     #      for enemy in enemies:
     #           if enemy.hitbox.colliderect(weapon_line):
     #                enemy.take_damage(self.damage)


class RangedWeapon(Weapon):
      def __init__(self, apple_position,projectile_speed, damage,fire_intervall=1000):
          super().__init__(apple_position)
          self.projectile_speed = projectile_speed 
          self.damage=damage
          self.projectiles =[]    

          #Autfire:
          self.fire_intervall= fire_intervall    #
          self.last_shot_time=0

      def auto_fire(self,direction):
           current_time=pygame.time.get_ticks()
           if current_time -self.last_shot_time >=self.fire_intervall:
                self.use(direction)
                self.last_shot_time= current_time

      def use( self, direction):# erzeugt kugel an spielerposition
          velocity = (direction [0]* self.projectile_speed,
                      direction [1]* self.projectile_speed)
          self.projectiles.append({
               "pos": list(self.apple_position) ,
               "vel": velocity
          })          
      def update(self,enemies):# bewegung der kugel
          for p in self.projectiles:
               p["pos"][0] += p["vel"][0]
               p["pos"][1] += p["vel"][1]

               for enemy in enemies:
                    if enemy.hitbox.collidepoint(int(p["pos"][0]), int(p["pos"][1])):
                         enemy.take_damage(self.damage)
                         self.projectiles.remove(p)
                         break                    
      def draw(self, window):
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
          super().__init__(apple_position,projectile_speed = 10,damage=100)
          #self.projectile_speed = 8
          #self.damage=100
          
class FastGun(RangedWeapon):
       def __init__(self, apple_position,):
          super().__init__(apple_position,projectile_speed = 20,damage=50)
      

class StrongGun(RangedWeapon):
       def __init__(self, apple_position,):
          super().__init__(apple_position,projectile_speed = 5,damage=150)
             

class Accessories():
     """Class for the basic functions for Accessories ."""
     pass