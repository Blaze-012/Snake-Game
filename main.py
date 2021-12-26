import turtle as t
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Initialise Score-board
score = ScoreBoard()

# Creates Snake
snake = Snake()

# Creates Food
food = Food()

# Snake Controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Moves The Snake.
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with food using turtle method distance.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        # Updates the score_board
        score.increase_score()

    # Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detect Collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
screen.exitonclick()
