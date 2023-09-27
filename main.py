from turtle import Screen
import time
import snake
from food import Food
from scoreboard import ScoreBoard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = snake.Snake()
food = Food()
scoreboard = ScoreBoard()
scoreboard.score_write()

# Taking player's inputs
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update() # Update the screen to show every movement the snake makes
    time.sleep(.09) # Rapidly turn the screen off so that snake segments look connected the whole time
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.new_location()
        snake.extend()
        scoreboard.clear()
        scoreboard.update_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.clear()
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()
screen.exitonclick()
