from enum import Enum
import pygame as pg

class Anchor(Enum):
    TOP_LEFT = 0, 
    MID_LEFT = 1,
    BOTTOM_LEFT = 2, 
    TOP_CENTER = 3,
    MID_CENTER = 4,      
    BOTTOM_CENTER = 5, 
    TOP_RIGHT = 6,
    MID_RIGHT = 7,
    BOTTOM_RIGHT = 8
    
class SpriteRenderer (pg.sprite.Sprite):
    def __init__(self, 
                 screen,
                 image_path : str, 
                 position : tuple = (0, 0), 
                 scale : tuple = (1, 1), 
                 scale_factor : float = 1, 
                 anchor : Anchor = Anchor.TOP_LEFT):
        super().__init__()
        self.screen = screen
        self.base_scale = scale 
        self.scale_factor = scale_factor
        self.scale = (self.base_scale[0] * scale_factor, self.base_scale[1] * self.scale_factor)
        self.image = pg.image.load(image_path).convert_alpha()
        self.position = position
        self.ScaleImage(self.base_scale, self.scale_factor)
        if anchor == Anchor.TOP_LEFT:
            self.rect = self.image.get_rect(topleft = position)
        elif anchor == Anchor.MID_LEFT:
            self.rect = self.image.get_rect(midleft = position)
        elif anchor == Anchor.BOTTOM_LEFT:
            self.rect = self.image.get_rect(bottomleft = position)
        elif anchor == Anchor.TOP_CENTER:
            self.rect = self.image.get_rect(midtop = position)
        elif anchor == Anchor.MID_CENTER:
            self.rect = self.image.get_rect(center = position)
        elif anchor == Anchor.BOTTOM_CENTER:
            self.rect = self.image.get_rect(midbottom = position)
        elif anchor == Anchor.TOP_RIGHT:
            self.rect = self.image.get_rect(topright = position)
        elif anchor == Anchor.MID_RIGHT:
            self.rect = self.image.get_rect(midright = position)
        elif anchor == Anchor.BOTTOM_RIGHT:
            self.rect = self.image.get_rect(bottomright = position)
    def GatherInput(self):
        pass
    
    def ScaleImage(self, base_scale : tuple, scale_factor : float):
        self.image = pg.transform.scale(self.image, (base_scale[0] * scale_factor, base_scale[1] * scale_factor))
    
    def ApplyGravity(self):
        pass
    
    def PlayerAnimation(self):
        pass
    
    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.image, self.rect)