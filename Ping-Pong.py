from pygame import *

#ігрове вікно

#ширина і висота
wdth = 600
height = 500

fon = (200, 255, 255)

window = display.set_mode((win_width win_height))
window.fill(fon)

#годиннки для оновленення екрану
clock = time.Clock()
#кількість фпс
FPS = 120

game = True
finish = False

#цикл гри
while game:
    for e event.get():
        if e.type == QUIT:
            game False:
    display.update()
    clock.tick(FPS)
