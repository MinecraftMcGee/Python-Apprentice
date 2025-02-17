import turtle

if __name__ == '__main__':
    # Click in the righthand window to make it active then use your arrow
# keys to control the spaceship!
  game = True
  screen = turtle.Screen()
# this assures that the size of the screen will always be 400x400 ...

  screen.setup(400, 400)
# ... which is the same size as our image
# now set the background to our space image
 
  screen.bgcolor("white")
# Or, set the shape of a turtle
   # screen.addshape("turtle.png")
 #   turtle.shape("turtle.png")


  turtle.home
  turtle.sety(0)
  while(game):


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

    def penup():
        turtle.penup()

    def pendown():
        turtle.pendown()

    turtle.speed(0)

# now associate the defs from above with certain keyboard events
    screen.onkey(forward, "up")
    screen.onkey(backward, "down")
    screen.onkey(left, "left")
    screen.onkey(right, "right")
    screen.onkey(penup, "u")
    screen.onkey(pendown, "d")
    screen.listen()