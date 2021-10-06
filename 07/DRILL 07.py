from random import randint
from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 800, 600

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
x = 800 // 2
y = 600 // 2
hand_x, hand_y = randint(20, 780), randint(20, 580)
frame = 0
dir = 0
dx, dy = 0, 0

while running:
    print(dx, dy)
    clear_canvas()
    if dx == 0 and dy == 0: dx, dy = 400, 300
    if dx == hand_x and dy == hand_y:
        hand_x, hand_y = randint(20, 780), randint(20, 580)
    else:
        for i in range(0, 100 + 1, 2):
            kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
            hand.draw(hand_x, hand_y)
            t = i / 100
            dx = (1-t)*x + t*hand_x
            dy = (1-t)*y + t*hand_y
            if dx > hand_x:
                character.clip_draw(frame * 100, 0, 100, 100, dx, dy)
            elif dx < hand_x:
                character.clip_draw(frame * 100, 100, 100, 100, dx, dy)
            update_canvas()
            frame = (frame + 1) % 8
            handle_events()
            delay(0.02)
        x, y = hand_x, hand_y
    update_canvas()
    