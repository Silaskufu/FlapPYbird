import pygame

class Pipe(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, flip):
        super().__init__()
        self.width = width
        imgPath = r"C:\Users\hhseugs1\Documents\Coding\Python\FlapPYbird\assets\terrain\pipe-green.png"
        self.image = pygame.image.load(imgPath)
        self.image = pygame.transform.scale(self.image, (width, height))
        if flip:
            flippedImage = pygame.transform.flip(self.image, False, True)
            self.image = flippedImage
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift
        if self.rect.right < (-self.width):
            self.kill()

class Burrito(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, flip):
        super().__init__()
        self.width = width
        imgPath = r"C:\Users\hhseugs1\Documents\Coding\Python\FlapPYbird\assets\terrain\burrito.png"
        self.image = pygame.image.load(imgPath)
        self.image = pygame.transform.scale(self.image, (width, height))
        if flip:
            flippedImage = pygame.transform.flip(self.image, False, True)
            self.image = flippedImage
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift
        if self.rect.right < (-self.width):
            self.kill()

class Building(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, flip):
        super().__init__()
        self.width = width
        imgPath = r"C:\Users\hhseugs1\Documents\Coding\Python\FlapPYbird\assets\terrain\tower2.png"
        self.image = pygame.image.load(imgPath)
        self.image = pygame.transform.scale(self.image, (width, height))
        if flip:
            flippedImage = pygame.transform.flip(self.image, False, True)
            self.image = flippedImage
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift
        if self.rect.right < (-self.width):
            self.kill()