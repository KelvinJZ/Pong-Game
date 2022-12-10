import turtle as t

# Step 1 - create two paddles

# Step 2 - create the ball

# Step 3 - linking paddles with mouse events (keyboard binding)

# Step 4 - linking players

t.bgcolor("black")
r = t.Turtle()
r.speed(0)
l = t.Turtle()
l.speed(0)
b = t.Turtle()
b.speed(0)
w = t.Turtle()
w.speed(0)
s = t.Turtle()
s.speed(0)

# creating the border/wall and center line of the game
w.color('white')
w.penup()
w.goto(-130, -125)
w.pendown()
w.goto(130, -125)
w.goto(130, 125)
w.goto(-130, 125)
w.goto(-130, -125)
w.goto(0, -125)
w.goto(0, 125)

# creating scoreboard
s.color('white')
s.penup()
s.goto(-23, 95)
s.write("0 : 0", font=("Arial", 15, 'normal', 'bold'))
rs = 0
ls = 0

# creating left paddle
l.color('white')
l.penup()
l.goto(-110, -40)
l.shape("square")
l.shapesize(stretch_wid=0.6, stretch_len=3)

l.lt(90)
l.fd(40)

# creating right paddle
r.color('white')
r.penup()
r.goto(110, -40)
r.shape("square")
r.shapesize(stretch_wid=0.6, stretch_len=3)
r.lt(90)
r.fd(40)

# Creating ball
b.color('white')
b.shape('circle')
b.shapesize(stretch_wid=0.75, stretch_len=0.75)
b.penup()
b.goto(0, 0)
b.dx = 5
b.dy = -5


# Move Paddles Vertically Up and down
def right_paddle_up():
  y = r.ycor()
  r.sety(y + 20)


def right_paddle_down():
  y = r.ycor()
  r.sety(y - 20)


def left_paddle_up():
  y = l.ycor()
  l.sety(y + 20)


def left_paddle_down():
  y = l.ycor()
  l.sety(y - 20)


# Keybindings of paddles
window = t.Screen()
window.listen()
window.onkeypress(right_paddle_up, "Up")
window.onkeypress(right_paddle_down, "Down")
window.onkeypress(left_paddle_up, "w")
window.onkeypress(left_paddle_down, "s")

for i in range(9999):
  window.update()
  b.setx(b.xcor() + b.dx)
  b.sety(b.ycor() + b.dy)

  # Check borders
  if b.ycor() < -120:
    b.sety(-120)
    b.dy *= -1

  if b.ycor() > 120:
    b.sety(120)
    b.dy *= -1

  # making scoreboard go up as somebody scores
  if b.xcor() > 130:
    b.goto(0, 0)
    b.dy *= -1
    ls += 1
    s.clear()
    s.write("{} : {}".format(ls, rs), font=("Arial", 15, 'normal', 'bold'))

  if b.xcor() < -130:
    b.goto(0, 0)
    b.dy *= -1
    rs += 1
    s.clear()
    s.write("{} : {}".format(ls, rs), font=("Arial", 15, 'normal', 'bold'))

  # Making sure that ball hits the paddle
  if (b.xcor() > 100 and b.xcor() < 110) and (b.ycor() < r.ycor() + 40
                                              and b.ycor() > r.ycor() - 40):
    b.setx(100)
    b.dx *= -1

  if (b.xcor() < -100 and b.xcor() > -110) and (b.ycor() < l.ycor() + 40 and
                                                  b.ycor() > l.ycor() - 40):
    b.setx(-100)
    b.dx *= -1


  # make sure that paddle doesn't go off the screen
  if r.ycor() + 40 > 125:
   r.goto(r.xcor(), 95.5)

  if r.ycor() - 40 < -125:
   r.goto(r.xcor(), -95)

  if l.ycor() + 40 > 125:
   l.goto(l.xcor(), 95.5)

  if l.ycor() - 40 < -125:
   l.goto(l.xcor(), -95)

  # Making the game stop when a player hits 15
  if rs == 15 or ls == 15:
    break

# Clearing the screen and saying game over
window.clear()
t.bgcolor("black")
t.pencolor("white")
t.penup()
t.goto(-120, -50)
t.write("Game\n Over", font=("Arial", 50, 'normal', 'bold'))

# Stating the player who won
if ls == 15:
  t.goto(-120, -80)
  t.write("Left player won!", font=("Arial", 18, 'normal', 'bold'))
elif rs == 15:
  t.goto(-120, -80)
  t.write("Right player won!", font=("Arial", 18, 'normal', 'bold'))