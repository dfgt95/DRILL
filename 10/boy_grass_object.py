from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 800, 600
# Game object class here

class ball:
    def __init__(self):
        self.n = random.randint(1,2)
        if self.n == 1:
            self.image = load_image ('ball21x21.png')
        elif self.n == 2:
            self.image = load_image ('ball41x41.png')
        self.speed = random.randint(1, 5)
        self.x = random.randint(0, 800)
        self.y = 599
    def draw(self):
        self.image.draw(self.x, self.y)
    def update(self):
        if self.y < 69 and self.n == 1:
            self.speed = 0
        elif self.y < 79 and self.n == 2:
            self.speed = 0
        self.y -= self.speed


class ball41:
    def __init__(self):
        self.image = load_image ('ball41x41.png')
        self.speed = random.randint(1, 5)
        self.x = random.randint(0, 800)
        self.y = 599
    def draw(self):
        self.image.draw(self.x, self.y)
    def update(self):
        self.y -= self.speed

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas(KPU_WIDTH, KPU_HEIGHT)
grass = load_image('grass.png')
character = load_image('animation_sheet.png')
balls = [ball() for  i in range(20)]
running = True
# game main loop code
while running:
    clear_canvas()
    grass.draw(400, 30)
    update_canvas()
    for ball in balls:
        grass.draw(400,30)
        ball.draw()
        ball.update()
    update_canvas()
    handle_events()
    delay(0.02)

    update_canvas()

# finalization code