from pygame import *
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
mixer.music.set_volume(0.1)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (70,70))
        self.rect = self.image.get_rect()
        self.speed = player_speed
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 430:
            self.rect.y += self.speed

class Wall(sprite.Sprite):
    def __init__(self, r, g, b, w, h, x, y):
        super().__init__()
        self.image = Surface((w,h))
        self.image.fill((r,g,b))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        

                 
class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 450:
            self.direction = 'right'
        if self.rect.x >= 620:
            self.direction = 'left'

        if self.direction == 'right':
            self.rect.x += self.speed 
        else:
            self.rect.x -= self.speed 

window = display.set_mode((700,500))
display.set_caption('Лабиринт')
background = transform.scale(image.load("background.jpg"),(700,500))

player = Player('hero.png', 5, 420, 4)
enemy = Enemy('cyborg.png', 400, 420, 3)
gold = GameSprite('treasure.png', 578, 420, 3)
w1 = Wall(150, 200, 50, 550, 10, 100, 20)
w2 = Wall(150, 200, 50, 465, 10, 100, 120)
w3 = Wall(150, 200, 50, 10, 450, 650, 20)
w4 = Wall(150, 200, 50, 10, 350, 555, 120)
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

font.init()
font = font.SysFont('Arial', 70)
win = font.render('You Win', True, (0,255,0))
lose = font.render('You Lose', True, (255,0,0))




game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
      
        window.blit(background, (0,0))
        player.reset()
        enemy.reset()
        gold.reset()
        enemy.update()
        player.update()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        
        if sprite.collide_rect(player, gold):
            window.blit(win, (200,200))
            finish = True
            money.play 
        if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, w1):
            window.blit(lose, (200,200))
            finish = True
            kick.play
        if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, w3):
            window.blit(lose, (200,200))
            finish = True
            kick.play 
        if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, w2):
            window.blit(lose, (200,200))
            finish = True
            kick.play
        if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, w4):
            window.blit(lose, (200,200))
            finish = True
            kick.play              
    display.update()
    time.delay(20)
    