import arcade

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball('мячик.png', 0.1)
        self.ball.center_x = 300
        self.ball.center_y = 300
        self.ball.change_x = 2

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color((60, 179, 113))
        self.ball.draw()

    def on_update(self, delta_time: float):
        self.ball.update()


class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x


window = GameWindow(600, 600, 'Ping-Pong')
arcade.run()