from turtle import Turtle

# the positions can be placed up here as constants (caps)
# I.e. POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]

    def make_snake(self):
        positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in positions:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move_snake_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def snake_moving(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def grow(self):
        x_co = self.segments[len(self.segments)-1].xcor()
        y_co = self.segments[len(self.segments)-1].ycor()
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(x_co, y_co)
        self.segments.append(new_segment)


