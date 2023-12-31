import turtle

# Coordinates to have every segment line up
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, color):
        self.segments = []
        self.create_snake(color)
        self.head = self.segments[0]

    # Creates a snake with 3 segments
    def create_snake(self, color):
        for position in STARTING_POSITIONS:
            self.add_segment(position, color)

    # Add a segment when the snake eats food
    def add_segment(self, position, color):
        new_segment = turtle.Turtle("square")
        new_segment.penup()
        new_segment.color(color)
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Player picks color of their snake

    # Add segments to the snake
    def extend(self):
        self.add_segment(self.segments[-1].position())

    """
    Moves all the segments one at a time, used in main with sleep() so that the player does not see when the
    snake segments are disconnected
    """

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            snake_position = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(snake_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
