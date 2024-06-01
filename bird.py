import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, imgs):
        super().__init__()
        self.origin_x = x
        self.origin_y = y
        self.imgs = imgs
        self.img_index = 0
        self.image = self.imgs[self.img_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.last_pic_time = pygame.time.get_ticks()
        self.img_frequency = 100
        self.y_speed = 0
        self.fly = True

    def update(self,floor_top):
        #fly
        if self.fly:
            now = pygame.time.get_ticks()
            if now - self.last_pic_time > self.img_frequency:
                self.img_index += 1
                if self.img_index >= len(self.imgs):
                    self.img_index = 0
                self.image = pygame.transform.rotate(self.imgs[self.img_index], -self.y_speed*3)
                self.last_pic_time = now
        # gravity
        self.y_speed += 0.5
        if self.y_speed > 9:
            self.y_speed = 9
        self.rect.y += self.y_speed
        if self.rect.bottom > floor_top:
            self.rect.bottom = floor_top

    def jump(self):
        self.y_speed = -8

    def game_over(self):
        self.fly = False

    def reset(self):
        self.img_index = 0
        self.image = self.imgs[self.img_index]
        self.rect = self.image.get_rect()
        self.rect.center = (self.origin_x,self.origin_y)
        self.last_pic_time = pygame.time.get_ticks()
        self.y_speed = 0
        self.fly = True

