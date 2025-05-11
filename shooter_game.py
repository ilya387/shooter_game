from pygame import *
from random import randint
window = display.set_mode((700, 500))
display.set_caption("космическая игра")
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
fire_sound =mixer.Sound("fire.ogg")
clock = time.Clock()
FPS = 60
game = True
font.init()
font1 = font.Font(None, 80)
win = font1.render("YOU WIN!", True, (255,255,255))
font2 = font.Font(None, 36)
lose = font2.render("YOU LOSE!", True, (180,0,0))

score = 0
lost = 0
max_lost = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,saysx,saysy, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (saysx, saysy))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700 - 80:
            self.rect.x += self.speed    
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)
lost = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 700:
            self.rect.x = randint(80, 700 - 80)
            self.rect.y = 0 
            lost = lost + 1
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self .speed
        if self.rect.y < 0:
            self.kill()

class Asteroid(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                space.fire()

        if not finish:
            window.blit(background,(0,0))
            space.reset()
            asteroid.draw.window()
            space.update()
            monsters.draw(window)
            monsters.update()
            bullets.draw(window)    
            bullets.update()
            text = font2.render("Счёт: "+ str(lost), 1,(255, 255, 255))
            window.blit(text, (10, 20))
            text_lose = font2.render("Пропущено: "+ str(lost), 1,(255, 255, 255))
            window.blit(text_lose, (10, 50))

        window.blit(background,(0,0))
        text = font2.render("Счёт: "+ str(lost), 1,(255, 255, 255))
        window.blit(text, (10, 20))
        text_lose = font2.render("Пропущено: "+ str(lost), 1,(255, 255, 255))
        window.blit(text_lose, (10, 50))
asteroid.spriteGroup
    for c  in collides:
        score += 1
        monster = Enemy(img_enemy, randint(80, win_width -80), -40,80,50)
        monsters.add(monster)
    if score >= 10:
        finish = True
        window.blit(win(200, 200))
    if sprite.groupcollide(ship,monster,False)>=3:
        finish = True
        score = 0
        lose = 0
        for b in bullets:
            b.kill()
        for b in monsters:
            b.kill()
        clock.tick(FPS)
    for i in range(1,6):
        monster = Enemy(img_enemy, randint(80, win_width -80), -40,80,50)
        monsters.add(monster) 

    if sprite.spritecollide(ship, monsters, False) or sprite.spritecollide(ship, asteroids,False)
    finish = True
    window.blit(lose, (200, 200))

  
    display.update()
clock.tick(FPS)
