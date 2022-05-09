import math
import random
import time

from turtle import Turtle, Screen
from snake import Snake
from food import Food
from gameconfig import GameConfig
from scoreboard import ScoreBoard

# Screen configuration
width = 600
height = 600

screen = Screen()
screen.setup(width=width, height=height)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
game_config = GameConfig()

# Snake Config
snake = Snake(screen, game_config)

# Control bindings
screen.onkeypress(key="Up", fun=snake.move_up)
screen.onkeypress(key="Down", fun=snake.move_down)
screen.onkeypress(key="Left", fun=snake.move_left)
screen.onkeypress(key="Right", fun=snake.move_right)



# Create Food Item
food = Food(screen)


# Score Turtle
score_board = ScoreBoard((0, height / 2 - 30), game_config)


screen_width = screen.window_width() / 2
screen_height = screen.window_height() / 2


def check_wall_collisions():
    if snake.head().xcor() >= screen_width - game_config.current_pixel_size \
            or snake.head().xcor() <= -screen_width + game_config.current_pixel_size:
        return True
    if snake.head().ycor() >= screen_height - game_config.current_pixel_size \
            or snake.head().ycor() <= -screen_height + game_config.current_pixel_size:
        return True


# Game Loop
def game_loop():
    screen.listen()
    in_game = True
    score_board.reset()
    screen.update()
    while in_game:
        time.sleep(.05)
        snake.move()
        if snake.head().distance(food) < 15:
            food.place_in_random_spot()
            snake.increase_size()
            score_board.add_points(10)
        if check_wall_collisions() or snake.check_collision_with_body():
            in_game = False
            screen.update()

        screen.update()

    play_again = screen.textinput(title="Game Over", prompt=f"You\'r score is: {score_board.score}\n Play again? y/n")
    if play_again is not None and play_again.lower() == "y":
        snake.setup()
        game_loop()
    else:
        screen.bye()


game_loop()


