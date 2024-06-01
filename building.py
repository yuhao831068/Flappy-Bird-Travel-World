import pygame

class Building(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speedx = 3

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.right < 0:
            self.kill()