import turtle

if __name__ == '__main__':
    # Click in the righthand window to make it active then use your arrow
  game = True
  screen = turtle.Screen()
# this assures that the size of the screen will always be 400x400 ...

  screen.setup(400, 400)
# ... which is the same size as our image
  screen.bgcolor("white")
  t = turtle.Turtle()
# Or, set the shape of a turtle
   # screen.addshape("turtle.png")
 #   turtle.shape("turtle.png")
  turtle.penup()
  t.penup()
  turtle.home()
  turtle.setx(-100)
  t.setx(100)
  t.sety(0)
  turtle.sety(0)
  while(game):
    turtle.penup()

    move_speed = 1
    turn_speed = 5


# these defs control the movement of our "turtle"
    def forward():
        turtle.forward(move_speed)

    def backward():
        turtle.backward(move_speed)

    def left():
        turtle.left(turn_speed)

    def right():
        turtle.right(turn_speed)

    turtle.penup()
    turtle.speed(0)


# now associate the defs from above with certain keyboard events
    screen.onkey(forward, "w")
    screen.onkey(backward, "s")
    screen.onkey(left, "a")
    screen.onkey(right, "d")
    screen.listen()


# Or, set the shape of a t
  #  screen.addshape("rocket.png")
  #  t.shape("rocket.png")

    move_speed = 1
    turn_speed = 5

# these defs control the movement of our "t"
    def forward():
        t.forward(move_speed)

    def backward():
        t.backward(move_speed)

    def left():
        t.left(turn_speed)

    def right():
        t.right(turn_speed)

    t.penup()
    t.speed(0)
#t.home()

# now associate the defs from above with certain keyboard events
    screen.onkey(forward, "Up")
    screen.onkey(backward, "Down")
    screen.onkey(left, "Left")
    screen.onkey(right, "Right")
    screen.listen()
   
    if ((turtle.xcor()-8)< t.xcor() and t.xcor()<(turtle.xcor()+8)):
      if ((turtle.ycor()-8)< t.ycor() and t.ycor()<(turtle.ycor()+8)):
        print("game over player 1")
        t.hideturtle()
        turtle.hideturtle()
        game=False