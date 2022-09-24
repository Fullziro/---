from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height, ):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height) )
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y) )

class Player(GameSprite):
    def update_r(self): #right racket
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y > 420:
            self.rect.y -= self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.x > 5:
            self.rect.x += self.speed
        if keys [K_s] and self.rect.x > 420:
            self.rect.x += self.speed
        
#ігрове вікно

#ширина і висота
wdth = 600
height = 500

#колір  фону
fon = (200, 255, 255)

window = display.set_mode((win_width win_height))
window.fill(fon)

#годиннки для оновленення екрану
clock = time.Clock()
#кількість фпс
FPS = 120

#створення ракеток і м'яча
ball = GameSprite("tennis_ball.png", 200,200, 4, 50, 50)
racket1 = Player("racket1.png" 30, 200, 4, 50, 150)
racket2 = Player("racket2.png" 520, 200, 4, 50, 150)

game = True
finish = False

speed_x = 3
speed_y = 3

font.init()
font = font.Font(None, 35)
win2 = font.Render("Player Right Win!", True, (180, 0, 0) )
win1 = font.Render("Player Left Win!", True, (180, 0, 0) )
#цикл гри
while game:
    for e event.get():
        if e.type == QUIT:
            game False
    if finish != True:
        windiw.fill(fon)
        racket1.update_l()
        rakcet2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= -1
        if ball.rect.y < 0 or ball.rect.y > 450:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(win2, (200, 200) )
            game = True
        if ball.rect.x > 600:
            finish = True
            window.blit(win1, (200, 200) )
            game = True
        racket1 = reset()
        racket2 = reset()
        ball = reset()
    display.update()
    clock.tick(FPS)
