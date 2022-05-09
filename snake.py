import random
from enum import Enum
from turtle import Turtle


class Direction(Enum):
    Right = 1,
    Left = 2
    Up = 3,
    Down = 4


class Snake:

    def __init__(self, screen, game_config):
        # snake properties
        self.game_config = game_config
        self.starting_fragments = 3
        self.screen = screen
        self.facing_direction = Direction.Right
        self.fragments = []
        self.current_direction = Direction.Right

        self.setup()

    def create_fragment(self):
        fragment = Turtle("square")
        fragment.color("white")
        fragment.penup()
        fragment.shapesize(self.game_config.scale_for_turtles)
        return fragment

    def move(self):
        index = len(self.fragments) - 1
        while index > 0:
            prev_index = index - 1
            self.fragments[index].goto(self.fragments[prev_index].xcor(), self.fragments[prev_index].ycor())
            index -= 1

        self.fragments[0].forward(self.game_config.current_pixel_size)

# Standard mode 0 east, 90 north, 180 west, 270 south - setheading
    def move_up(self):
        if self.current_direction == Direction.Up or self.current_direction == Direction.Down:
            return

        self.current_direction = Direction.Up
        self.fragments[0].setheading(90)

    def move_down(self):
        if self.current_direction == Direction.Up or self.current_direction == Direction.Down:
            return

        self.current_direction = Direction.Down
        self.fragments[0].setheading(270)

    def move_right(self):
        if self.current_direction == Direction.Right or self.current_direction == Direction.Left:
            return

        self.current_direction = Direction.Right
        self.fragments[0].setheading(0)

    def move_left(self):
        if self.current_direction == Direction.Right or self.current_direction == Direction.Left:
            return

        self.current_direction = Direction.Left
        self.fragments[0].setheading(180)

    def head(self):
        return self.fragments[0]

    def increase_size(self):
        fragment = self.create_fragment()
        fragment.setposition(self.fragments[-1].pos())
        self.fragments.append(fragment)

    def check_collision_with_body(self):
        head = self.fragments[0]
        for fragment in self.fragments[1:]:
            if head.distance(fragment) < 1:
                fragment.color("red")
                return True

        return False

    def setup(self):
        self.current_direction = Direction.Right
        if len(self.fragments) > 0:
            for fragment in self.fragments:
                fragment.reset()

            self.fragments.clear()

        create_index = 0
        while create_index < self.starting_fragments:
            fragment = self.create_fragment()
            fragment.goto(-(self.game_config.current_pixel_size * create_index), 0)
            self.fragments.append(fragment)
            create_index += 1

