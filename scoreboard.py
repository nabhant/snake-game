from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self._score = 0
        self._high_score = 0

    # Using turtle.Write() to keep track of the score
    def score_write(self):
        self.write(f"Score:{self._score}", align="center", font=("Verdana", 15, "normal"))

    # Add one to the score
    def update_score(self):
        self._score += 1
        self.clear()
        self.write(f"Score:{self._score}", align="center", font=("Verdana", 15, "normal"))

    # Show "GAME OVER" in the center of the screen when snake collides with wall or itself
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER. CLICK WINDOW TO EXIT.", align="center", font=("Verdana", 15, "normal"))

    # Updates high score after game finishes
    def update_high_score(self):
        if self._score > self._high_score:
            self._high_score = self._score
        self.goto(0, -30)
        self.write(f"HIGH SCORE: {self._high_score}", align="center", font=("Verdana", 15, "normal"))

