import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turns off the screen updates

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("blue")  # Paddle color set to blue
paddle.shapesize(stretch_wid=1, stretch_len=6)  # Adjusted paddle size to match the image
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("square")  # Square shape to match the classic look
ball.color("white")  # Ball color set to white
ball.penup()
ball.goto(0, -230)
ball.dx = 0.8  # Increased speed even more
ball.dy = 0.8  # Increased speed even more

# Bricks
bricks = []

colors = ["red", "orange", "yellow", "green"]

brick_height = 20
rows = 4
cols = 13  # Number of bricks per row to match the width
brick_width = (800 - (cols + 1) * 5) / cols  # Adjusted to ensure bricks cover the width

for y in range(rows):
    for x in range(cols):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[y])
        brick.shapesize(stretch_wid=brick_height / 20, stretch_len=brick_width / 20)
        brick.penup()
        start_x = -390 + brick_width / 2 + 5
        brick.goto(start_x + x * (brick_width + 5), 250 - y * (brick_height + 5))
        bricks.append(brick)

# Paddle movement
def paddle_right():
    x = paddle.xcor()
    if x < 350:
        x += 40
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    if x > -350:
        x -= 40
    paddle.setx(x)

# Keyboard bindings
screen.listen()
screen.onkeypress(paddle_right, "Right")
screen.onkeypress(paddle_left, "Left")

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collision (top)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # Border collision (left and right)
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.setx(ball.xcor())
        ball.dx *= -1

    # Ball and paddle collision
    if ball.ycor() > -240 and ball.ycor() < -230 and (ball.xcor() > paddle.xcor() - 60 and ball.xcor() < paddle.xcor() + 60):
        ball.sety(-230)
        ball.dy *= -1

    # Ball and brick collision
    for brick in bricks:
        if ball.distance(brick) < (brick_width / 2 + 10):
            ball.dy *= -1
            brick.goto(1000, 1000)  # Move the brick off screen
            bricks.remove(brick)
            break

    # Bottom border collision
    if ball.ycor() < -290:
        ball.goto(0, -230)
        ball.dy *= -1
        # You can add a 'Game Over' condition here

    # Win condition
    if not bricks:
        print("You win!")
        break

screen.mainloop()
