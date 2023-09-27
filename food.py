from turtle import Turtle
import random

COLORS = ["red", "green", "blue", "purple", "turquoise", "orange", "white", "pink"]
class Food(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color(random.choice(COLORS))
        self.speed("fastest")
        x = random.randint(-200, 280)
        y = random.randint(-200, 200)
        self.goto(x, y)

    # Randomly places the food in a new location on the game screen
    def new_location(self):
        x = random.randint(-200, 280)
        y = random.randint(-200, 200)
        self.color(random.choice(COLORS))
        self.goto(x, y)