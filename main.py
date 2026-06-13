from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.uix.widget import Widget


class Game(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ball_y = 0
        self.vel = 0
        self.gravity = 0.3

        with self.canvas:
            Color(0.68, 0.85, 0.90)
            self.bg = Rectangle()

            Color(1, 1, 0)
            self.sun = Ellipse(size=(100, 100))

            Color(1, 0.65, 0)
            self.ball = Ellipse(size=(60, 60))

            Color(0.49, 0.99, 0)
            self.ground = Rectangle()

        self.bind(size=self.update_layout)
        self.bind(pos=self.update_layout)

        Clock.schedule_once(self.start_game)
        Clock.schedule_interval(self.update, 1 / 60)

    def start_game(self, dt):
        self.ball_y = self.height / 2

    def update_layout(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

        self.sun.pos = (self.width - 120, self.height - 120)

        self.ground.pos = (0, 0)
        self.ground.size = (self.width, 20)

    def update(self, dt):
        self.vel += self.gravity
        self.ball_y -= self.vel

        if self.ball_y <= 20:
            self.ball_y = 20
            self.vel *= -0.8

            if abs(self.vel) < 1:
                self.vel = 0

        self.ball.pos = (self.width / 2 - 30, self.ball_y)


class MyApp(App):
    def build(self):
        return Game()


MyApp().run()
