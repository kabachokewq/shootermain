from pygame import *
from random import randint
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound("fire.ogg")
wn = display.set_mode((700,500))
clock = time.Clock()
display.set_caption("Шутер")
background = transform.scale(image.load("galaxy.jpg"),(700,500))
FPS = 60
font.init()
font1 = font.Font(None,36)
score = 0
lose = 0
class GameSprite(sprite.Sprite):
    def __init__(self,pl_image,pl_x,pl_y,size_x,size_y,pl_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(pl_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
        self.speed = pl_speed
        self.size_x = size_x
    def reset(self):
        wn.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        #[K_a,K_k]
        #назва списку[номер елементу]
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 700 - self.size_x:
            self.rect.x += self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = -50
            self.rect.x = randint(80,620)
            self.speed = randint(1,5)
monsters = sprite.Group()
for i in range(3):
    monster = Enemy("ufo.png", randint(80,620),-50,80,50,randint(1,5))
    monsters.add(monster)
rocket = Player("rocket.png",305,400,80,100,10) 

asteroids = sprite.Group()
for i in range(3):
    asteroid = Enemy("asteroid.png", randint(80,620),-50,80,50,randint(1,5))
    asteroids.add(asteroid)
 

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        wn.blit(background,(0,0))
        text_score = font1.render("Рахунок: " + str(score),1,(255,255,255))
        wn.blit(text_score,(10,20))
        text_lose = font1.render("Пропущено: " + str(lose),1,(255,255,255))
        wn.blit(text_lose,(10,50))
        rocket.reset()
        rocket.update()
        monsters.draw(wn)
        monsters.update()
        asteroids.draw(wn)
        asteroids.update()
    clock.tick(FPS)
    display.update()