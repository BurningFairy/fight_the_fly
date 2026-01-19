"""This file is for the playable character."""
from resource_path import resource_path
import pygame
import math
import settings
from shop.items import RangedWeapon,Cocktailpick,Flyswater,Bugspray, FastGun,StrongGun, MeleeWeapon

class Apple:
    """Represents the playable character."""

    def __init__(self, image, x, y, height=100, width=100):
        """Construct an Object of Apple."""
        self.width = height
        self.height = width

        unscaled_image = pygame.image.load(resource_path(image))
        self.image = pygame.transform.smoothscale(
            unscaled_image, (self.width, self.height))
        self.x = x
        self.y = y
        self.movespeed = 5
        self.hitbox = (self.x, self.y, self.width, self.height)

        self.position = [self.x, self.y]

        #waffen slots
        self.weapon_slots = [None, None]
        self.weapon_slots[0] = Flyswater(self.position)
        self.weapon_slots[1] = Bugspray(self.position)
        

        
      

        #shootingdirection
        self.last_direction=[1,0]

    def draw_apple(self, window):
        """Draw the char onto the WINDOW surface."""
        window.blit(self.image, (self.x, self.y))
        self.hitbox = (self.x + 15, self.y + 28, self.width -32, self.height- 40)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def handle_apple_movement(self, keys):
        """Handle the movement of the character."""
    
        change_x=0#startposition
        change_y=0
        speed=self.movespeed

        up=(keys[pygame.K_UP] or keys[pygame.K_w])
        down=(keys[pygame.K_DOWN] or keys[pygame.K_s])
        left=(keys[pygame.K_LEFT] or keys[pygame.K_a])
        right=(keys[pygame.K_RIGHT] or keys[pygame.K_d])

        if (up or down) and (right or left):
            speed *=0.6

        # move up + restriction
        if (self.y - speed > 0
                and up):
            self.y -= speed
           
            change_y=-1
        
        # move down + restriction
        if (self.y + speed + self.height < settings.WIN_HEIGHT
                and down):
            self.y += speed
           
            change_y=1
          
        # move left + restriction
        if (self.x - speed > 0
                and left):
            self.x -= speed
            
            change_x=-1
           
        # move right + restriction
        if (self.x + speed + self.width < settings.WIN_WIDTH
                and right):
            self.x += speed
           
            change_x=1
            
        
        self.position=[self.x + self.width//2, self.y + self.height//2]
        
      
        for weapon in self.weapon_slots: # Waffenposition aktualisieren
            if weapon:
                weapon.update_position(self.position)

        if change_x !=0 or change_y != 0: # Letzte Bewegungsrichtung speichern
            self.last_direction=[change_x,change_y]
            
            for weapon in self.weapon_slots:# Waffen in Blickrichtung drehen (nur Melee)
                if weapon and isinstance(weapon,MeleeWeapon):
                    weapon.use(self.last_direction)

   
    def update_weapons(self,enemies):
        current_direction=self.last_direction
        for weapon in self.weapon_slots:
            if weapon is None:
                continue

            # Nahkampfwaffen Schaden prüfen
            if isinstance(weapon,MeleeWeapon):
                weapon.check_hit(enemies)
                
            # Automatisches Schießen für Fernkampfwaffen
            if isinstance(weapon,RangedWeapon):#, ob ein Objekt eine Instanz einer bestimmten Klasse
                weapon.auto_fire(current_direction)
                
             # Projektile oder Treffer aktualisieren
            if hasattr(weapon,"update"):#überprüft, ob ein Objekt ein bestimmtes Attribut (oder eine Methode) besitzt
                weapon.update(enemies)

      
      