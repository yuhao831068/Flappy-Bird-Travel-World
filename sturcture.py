import pygame
from bird import Bird
from building import Building
from obstacle import Obstacle
import random

pygame.init()

def randint_exclude(start, end, exclude):
    while True:
        num = random.randint(start, end)
        if num != exclude:
            return num


def generate_buildings(last_building_time, building_frequency, building_sprite):
    now = pygame.time.get_ticks()
    if now - last_building_time > building_frequency:
        building_images = [building1_img, building2_img, building3_img, building4_img, building5_img, building6_img, building7_img, building8_img]
        new_buildings = []
        for img in building_images:
            while True:
                x = random.randint(1000, 3000)
                if img == building2_img:
                    new_building = Building(img=img, x=x, y=480)
                elif img == building3_img:
                    new_building = Building(img=img, x=x, y=525)
                elif img == building5_img:
                    new_building = Building(img=img, x=x, y=515)
                else:
                    new_building = Building(img=img, x=x, y=525)
                if all(not new_building.rect.colliderect(b.rect) for b in building_sprite):
                    new_buildings.append(new_building)
                    break

        for building in new_buildings:
            building_sprite.add(building)

        return now
    return last_building_time


def generate_obstacles(last_obstacle_time, obstacel_frequency, obstacle_sprite):
    now = pygame.time.get_ticks()
    if now - last_obstacle_time > obstacel_frequency:
        obstacle_images = [ufo_img, astrounut_img]
        new_obstacles = []
        for img in obstacle_images:
            while True:
                x = random.randint(1000, 3000)
                y = random.randint(30,200)
                new_obstacle = Obstacle(img=img, x=x, y=y)
                new_obstacles.append(new_obstacle)
                break

        for obstacle in new_obstacles:
            obstacle_sprite.add(obstacle)

        return now
    return last_obstacle_time


def draw_second():
    second_text = second_font.render(str(second), True, (0,0,0))
    window.blit(second_text, (20, 20))

FPS = 80
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('world travel')
clock = pygame.time.Clock()

# import img
bg_img = pygame.image.load('img/bg.png')
bg_img = pygame.transform.scale(bg_img,(1000,700))

floor_img = pygame.image.load('img/floor.png')
floor_img = pygame.transform.scale(floor_img,(1200,50))
building1_img = pygame.image.load('img/building1.png')
building1_img = pygame.transform.scale(building1_img,(200,250))
building2_img = pygame.image.load('img/building2.png')
building2_img = pygame.transform.scale(building2_img,(100,350))
building3_img = pygame.image.load('img/building3.png')
building3_img = pygame.transform.scale(building3_img,(100,250))
building4_img = pygame.image.load('img/building4.png')
building4_img = pygame.transform.scale(building4_img,(100,250))
building5_img = pygame.image.load('img/building5.png')
building5_img = pygame.transform.scale(building5_img,(100,280))
building6_img = pygame.image.load('img/building6.png')
building6_img = pygame.transform.scale(building6_img,(100,400))
building7_img = pygame.image.load('img/building7.png')
building7_img = pygame.transform.scale(building7_img,(100,500))
building8_img = pygame.image.load('img/building8.png')
building8_img = pygame.transform.scale(building8_img,(100,380))




ufo_img = pygame.image.load('img/UFO.png')
ufo_img = pygame.transform.scale(ufo_img,(51,36))
astrounut_img = pygame.image.load('img/Astrounut.png')
astrounut_img = pygame.transform.scale(astrounut_img,(51,36))

bird_imgs = []
for i in range(1,3):
    bird_imgs.append(pygame.image.load(f'img/bird{i}.png'))
pygame.display.set_icon(bird_imgs[0])

# import font
second_font = pygame.font.SysFont('comicsansms', 60)
hit_font = pygame.font.SysFont('comicsansms', 30)
game_over_font = pygame.font.SysFont('comicsansms', 50)


#variables
ground_speed = 3
ground_x = 0
floor_top = SCREEN_HEIGHT - 50



#building
last_building_time = pygame.time.get_ticks()
building_frequency = 4000
last_building_time = pygame.time.get_ticks() - building_frequency

game_over_text = game_over_font.render(str('Press Space to restart'), True, (226,226,226))
hit_building1_text = hit_font.render(str('You hit Colosseum'), True, (0,0,0))
hit_building2_text = hit_font.render(str('You hit Eiffel Tower'), True, (0,0,0))
hit_building3_text = hit_font.render(str('You hit Big Ben'), True, (0,0,0))
hit_building4_text = hit_font.render(str('You hit Statue of Liberal'), True, (0,0,0))
hit_building5_text = hit_font.render(str('You hit Sagrada Familia'), True, (0,0,0))
hit_building6_text = hit_font.render(str('You hit Taipei 101'), True, (0,0,0))
hit_building7_text = hit_font.render(str('You hit Burj Khalifa'), True, (0,0,0))
hit_building8_text = hit_font.render(str('You hit Shanghai World Financial Center'), True, (0,0,0))









#obstacle
last_obstacle_time = pygame.time.get_ticks()
obstacle_frequency = 2800
last_obstacle_time = pygame.time.get_ticks() - obstacle_frequency

game_over = False

bird = Bird(imgs = bird_imgs,x = 100,y = 300)
bird_sprite = pygame.sprite.Group()
bird_sprite.add(bird)


building_sprite = pygame.sprite.Group()
# building_images = [building1_img, building2_img, building3_img, building4_img, building5_img]

obstacle_sprite = pygame.sprite.Group()
# obstacles_images = [ufo_img,astrounut_img]




run = True
while run:

    clock.tick(FPS)


    #get imput
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not game_over:
                bird.jump()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                game_over = False
                second = 0
                building_sprite = pygame.sprite.Group()
                obstacle_sprite = pygame.sprite.Group()
                bird.reset()
                for building in building_sprite.sprites():
                    building.kill()
                for obstacle in obstacle_sprite.sprites():
                    obstacle.kill()

    #renew game
    bird_sprite.update(floor_top) # call all update methods in the group
    if not game_over:
        second = pygame.time.get_ticks()
        building_sprite.update()
        last_building_time = generate_buildings(last_building_time, building_frequency, building_sprite)
        obstacle_sprite.update()
        last_obstacle_time = generate_obstacles(last_obstacle_time,obstacle_frequency,obstacle_sprite)
        ground_x -= ground_speed
    if ground_x < -100:
        ground_x = 0

    # collision
    if (pygame.sprite.groupcollide(bird_sprite,building_sprite,False,False)
            or pygame.sprite.groupcollide(bird_sprite,obstacle_sprite,False,False)
            or bird.rect.top < 0
            or bird.rect.bottom >= floor_top):
            game_over = True
            bird.game_over()

    #display
    window.blit(bg_img,(0,0))
    bird_sprite.draw(window)
    building_sprite.draw(window)
    obstacle_sprite.draw(window)
    window.blit(floor_img,(ground_x,floor_top))
    draw_second()
    # check what you collide
    collided_building = pygame.sprite.spritecollideany(bird, building_sprite)
    if collided_building:
        if collided_building.image == building1_img:
            window.blit(hit_building1_text,(350,300))
        elif collided_building.image == building2_img:
            window.blit(hit_building2_text,(350,300))
        elif collided_building.image == building3_img:
            window.blit(hit_building3_text,(350,300))
        elif collided_building.image == building4_img:
            window.blit(hit_building4_text,(350,300))
        elif collided_building.image == building5_img:
            window.blit(hit_building5_text,(350,300))
        elif collided_building.image == building6_img:
            window.blit(hit_building6_text,(350,300))
        elif collided_building.image == building7_img:
            window.blit(hit_building7_text,(350,300))
        elif collided_building.image == building8_img:
            window.blit(hit_building8_text,(350,300))
    if game_over:
        window.blit(game_over_text, (250, 100))
    pygame.display.update()

pygame.quit()