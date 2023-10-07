from turtle import Screen
import time
import snake
from food import Food
from scoreboard import ScoreBoard

# CONSTANTS FOR GAME SCREEN SETUP
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SLEEP_DURATION = 0.09


def color_pick():
    valid_colors = {1: "red", 2: "blue", 3: "orange", 4: "green"}
    while True:
        try:
            color_input = int(input(
                "What color would you like to make your turtle? Type '1' for red, '2' for blue, '3' for orange, and '4' for green. "))
            color = valid_colors[color_input]
            return color
        except KeyError:
            print("Invalid input. Please enter a valid number (1, 2, 3, or 4).")


color_chosen = color_pick()

print(color_chosen)

if color_chosen != "":
    print("success")
    # Screen setup
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = snake.Snake(color_chosen)
    food = Food()
    scoreboard = ScoreBoard()
    scoreboard.score_write()

    # Taking player's inputs
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_on = True
    while game_on:
        screen.update()  # Update the screen to show every movement the snake makes
        time.sleep(SLEEP_DURATION)  # Rapidly turn the screen off so that snake segments look connected the whole time
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
            scoreboard.update_high_score()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_on = False
                scoreboard.game_over()
                scoreboard.update_high_score()

    screen.exitonclick()
