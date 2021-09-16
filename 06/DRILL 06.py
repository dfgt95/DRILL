from pico2d import *
import math

open_canvas()

grass = load_image('D:/2DGP2021/DRILL/06/grass.png')
character = load_image('D:/2DGP2021/DRILL/06/character.png')
is_square = 0
rad = 0
x = 400
y = 90
while(True):
    if (x < 780 and y <= 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        if(is_square == 4 and x == 400):
            for rad in range(1,360+1):
                clear_canvas_now()
                grass.draw_now(400,30)
                circle_x = 400 + math.sin(rad/360*2*math.pi)*200
                circle_y = 290 - math.cos(rad/360*2*math.pi)*200
                character.draw_now(circle_x,circle_y)
                delay(0.02)
        x += 2
        if(x == 780 and y == 90): is_square = 1
        delay(0.01)
       
    elif (x >= 780 and y < 550):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 2
        if(x == 780 and y == 550): is_square = 2
        delay(0.01)
        
    elif (x > 20 and y >= 550):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 2
        if(x == 20 and y == 550):  is_square = 3
        delay(0.01)

    elif (x <= 20 and y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= 2
        if(x == 20 and y == 90): is_square = 4
        delay(0.01)