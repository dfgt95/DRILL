import random
from pico2d import *
import game_world
import game_framework

TIME_PER_ACTION = 0.5                           # 액션당 0.5초
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION         # 시간당 액션 횟수
FRAMES_PER_ACTION = 14                          # 액션당 사용 프레임

PIXEL_PER_METER = (10.0 / 0.3)                      # 10 pixel 30 cm
FLY_SPEED_KMPH = 30.0                               # Km / Hour
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

class Bird:
    image = None

    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.x, self.y, self.speed, self.frame = random.randint(50, 1600-50), random.randint(50, 600 - 50), FLY_SPEED_PPS, 0

    def get_bb(self):
        # fill here
        return 0,0,0,0

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y, 30, 30)                # 새의 크기는 90cm로 설정
        # fill here for draw

    def update(self):
        if self.x >= 1600 - 50 or self.x < 10:
            self.speed *= -1
        self.x += self.speed * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time ) % 14

    #fill here for def stop

