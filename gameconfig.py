class GameConfig:
    def __init__(self):
        self.default_pixel_size = 20   # This comes from Turtle
        self.scale_for_turtles = .5
        self.current_pixel_size = self.default_pixel_size * self.scale_for_turtles
