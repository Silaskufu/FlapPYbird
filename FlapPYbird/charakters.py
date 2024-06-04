import pygame
from settings import import_sprite

class Bird(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.frameIndex = 0
        self.animationDelay = 3
        self.jumpMove = -10
        self.birdImg = import_sprite(r"C:\Users\hhseugs1\Documents\Coding\Python\FlapPYbird\assets\bird")
        self.image = self.birdImg[self.frameIndex]
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft = pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.direction = pygame.math.Vector2(0,0)
        self.score = 0

    def _animate(self):
        sprites = self.birdImg
        spriteIndex = (self.frameIndex // self.animationDelay) % len(sprites)
        self.image = sprites[spriteIndex]
        self.frameIndex += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
        if self.frameIndex // self.animationDelay > len(sprites):
            self.frameIndex = 0
    
    def _jump(self):
        self.direction.y = self.jumpMove
    
    def update(self, isJump):
        if isJump:
            self._jump()
        self._animate()


class Plane(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.frameIndex = 0
        self.animationDelay = 3
        self.jumpMove = -10
        self.planeImg = import_sprite(r"C:\Users\hhseugs1\Documents\Coding\Python\FlapPYbird\assets\plane")
        self.image = self.planeImg[self.frameIndex]
        self.image = pygame.transform.scale(self.image, (size, size))
        self.blank_image = pygame.image.load("assets/terrain/clear.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.direction = pygame.math.Vector2(0,0)
        self.score = 0

    def remove_image(self):
        self.image = self.blank_image

    def _animate(self):
        sprites = self.planeImg
        spriteIndex = (self.frameIndex // self.animationDelay) % len(sprites)
        self.image = sprites[spriteIndex]
        self.frameIndex += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
        if self.frameIndex // self.animationDelay > len(sprites):
            self.frameIndex = 0
    
    def _jump(self):
        self.direction.y = self.jumpMove
    
    def update(self, isJump):
        if isJump:
            self._jump()
        self._animate()

class Mexbird(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.frameIndex = 0
        self.animationDelay = 3
        self.jumpMove = -10
        self.mexBirdImg = import_sprite(r"C:\Users\hhseugs1\Documents\Coding\Python\FlapPYbird\assets\mex-bird")
        self.blank_image = pygame.image.load("assets/terrain/clear.png")
        self.image = self.mexBirdImg[self.frameIndex]
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft = pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.direction = pygame.math.Vector2(0,0)
        self.score = 0
        
    
    def remove_image(self):
        self.image = self.blank_image


    def _animate(self):
        sprites = self.mexBirdImg
        spriteIndex = (self.frameIndex // self.animationDelay) % len(sprites)
        self.image = sprites[spriteIndex]
        self.frameIndex += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
        if self.frameIndex // self.animationDelay > len(sprites):
            self.frameIndex = 0
    
    def _jump(self):
        self.direction.y = self.jumpMove
    
    def update(self, isJump):
        if isJump:
            self._jump()
        self._animate()




