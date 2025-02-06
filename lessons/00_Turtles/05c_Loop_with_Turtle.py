import turtle
turtle.setup(width=550, height=625)

tina = turtle.Turtle()
tina.shape('triangle')
tina.speed(0)

def square_grid():
    def square(left_right):
        if left_right:
            for i in range(4):
                tina.forward(100)
                tina.left(90)
        else:
            for i in range(4):
                tina.forward(100)
                tina.right(90)

    tina.pendown()

    square(True)

    tina.penup()
    tina.forward(150)
    tina.pendown()

    square(True)

    tina.penup()
    tina.right(180)
    tina.forward(200)

    tina.pendown()

    square(False)

    tina.penup()
    tina.left(90)
    tina.forward(50)

    tina.pendown()

    square(False)

    tina.left(90)
    tina.penup()
    tina.forward(50)
    tina.pendown()

    square(False)

    tina.penup()
    tina.forward(150)
    tina.pendown()

    square(False)

    tina.left(90)
    tina.penup()
    tina.forward(200)
    tina.pendown()

    square(False)

    tina.left(90)
    tina.penup()
    tina.forward(50)
    tina.pendown()

    square(False)

    tina.penup()
    tina.forward(150)
    tina.pendown()

    square(False)

    tina.penup()
    tina.forward(250)
    tina.right(90)
    tina.pendown()

    square(False)

    tina.penup()
    tina.right(180)
    tina.forward(50)
    tina.pendown()

    square(True)
    tina.forward(100)

    tina.penup()
    tina.forward(50)
    tina.pendown()

    square(True)

    tina.penup()
    tina.forward(150)
    tina.pendown()

    square(True)

    tina.penup()
    tina.left(90)
    tina.forward(250)
    tina.right(90)
    tina.pendown()

    square(False)

    tina.penup()
    tina.left(90)
    tina.forward(50)
    tina.pendown()

    square(False)

    tina.penup()
    tina.forward(150)
    tina.pendown()

    square(False)

square_grid()

turtle.exitonclick()