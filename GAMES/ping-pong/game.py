import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
IMAGE_BALL = 'мячик.png'
BALL_SCALE = 0.05
SPEED_X = 5
SPEED_Y = 3

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball(IMAGE_BALL, BALL_SCALE)

    def setup(self):
        self.ball.center_x = SCREEN_WIDTH/2
        self.ball.center_y = SCREEN_HEIGHT/2
        self.ball.change_x = SPEED_X
        self.ball.change_y = SPEED_Y
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color((60, 179, 113))
        self.ball.draw()

    def on_update(self, delta_time: float):
        self.ball.update()


class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right > SCREEN_WIDTH or self.left < 0:
            self.change_x = -self.change_x
        self.center_y += self.change_y
        if self.top > SCREEN_HEIGHT or self.bottom < 0:
            self.change_y = -self.change_y

window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, 'Ping-Pong')
window.setup()
arcade.run()