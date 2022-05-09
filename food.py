import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.default_pixel_size = 20  # this is turtle library default
        self.fragment_body_size = .5
        self.current_pixel_size = self.default_pixel_size * self.fragment_body_size
        self.screen = screen
        self.shape("circle")
        self.color("blue")
        self.shapesize(.5)
        self.penup()
        self.speed("fastest")
        self.half_screen_x = screen.window_width() / 2
        self.half_screen_y = screen.window_height() / 2
        # Following tuples define the space to place food 0 for negative 1 for positive
        self.space_x = (-self.half_screen_x + self.current_pixel_size, self.half_screen_x - self.current_pixel_size)
        self.space_y = (-self.half_screen_y + self.current_pixel_size, self.half_screen_y - self.current_pixel_size)
        self.place_in_random_spot()

    def place_in_random_spot(self):
        rand_x = random.randint(self.space_x[0], self.space_x[1])
        rand_y = random.randint(self.space_y[0], self.space_y[1])
        self.goto(rand_x, rand_y)
