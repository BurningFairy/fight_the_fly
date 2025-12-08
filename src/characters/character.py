"""This file is for the playable character."""
import pygame
import math
import settings
from shop.items import Cocktailpick,Flyswater,Bugspray

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
        self.hitbox = (self.x, self.y, self.width, self.height)

        self.position = [self.x, self.y]
        #waffen ezeugen:
        self.cocktailpick= Cocktailpick(self.position)
        self.flyswater = Flyswater(self.position)
        self.bugspray =Bugspray(self.position)

        # autofiretimer:
        self.last_cocktailpick=0
        self.last_flyswater=0
        self.last_bugspray=0

        self.cocktailpick_interval=2000
        self.flyswater_interval=5000
        self.bugspray_interval=3000

        #shootingdirection
        self.last_direction=[1,0]

    def draw_apple(self, window):
        """Draw the char onto the WINDOW surface."""
        window.blit(self.image, (self.x, self.y))
        self.hitbox = (self.x + 15, self.y + 28, self.width -32, self.height- 40)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def handle_apple_movement(self, keys):
        """Handle the movement of the character."""
        moved= False
       
        change_x=0
        change_y=0
        # move up + restriction
        if (self.y - self.movespeed > 0
                and (keys[pygame.K_UP] or keys[pygame.K_w])):
            self.y -= self.movespeed
           
            change_y=-1
            moved= True
        # move down + restriction
        if (self.y + self.movespeed + self.height < settings.WIN_HEIGHT
                and (keys[pygame.K_DOWN] or keys[pygame.K_s])):
            self.y += self.movespeed
           
            change_y=1
            moved= True
        # move left + restriction
        if (self.x - self.movespeed > 0
                and (keys[pygame.K_LEFT] or keys[pygame.K_a])):
            self.x -= self.movespeed
            
            change_x=-1
            moved= True
        # move right + restriction
        if (self.x + self.movespeed + self.width < settings.WIN_WIDTH
                and (keys[pygame.K_RIGHT] or keys[pygame.K_d])):
            self.x += self.movespeed
           
            change_x=1
            moved= True
        
        self.position=[self.x + self.width//2, self.y + self.height//2]
        
        self.cocktailpick.update_position(self.position)
        self.flyswater.update_position(self.position)
        self.bugspray.update_position(self.position)

        if change_x !=0 or change_y != 0:
            self.last_direction=[change_x,change_y]
            self.cocktailpick.change_direction(self.last_direction)
            self.flyswater.change_direction(self.last_direction)

        

      
        
       
       
    def update_wapons(self,enemies):
        current=pygame.time.get_ticks()

        if current - self.last_cocktailpick>= self.cocktailpick_interval:
            self.cocktailpick.use(self.last_direction)
            self.cocktailpick.check_hit(enemies)
            self.last_cocktailpick =current
        
        if current - self.last_flyswater>= self.flyswater_interval:
            self.flyswater.use(self.last_direction)
            self.flyswater.check_hit(enemies)
            self.last_flyswater =current

        if current - self.last_bugspray>= self.bugspray_interval:
            self.bugspray.use(self.last_direction)
            
            self.last_bugspray =current

        #self.bugspray.update()

        self.bugspray.update(enemies)