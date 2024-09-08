from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #Bounce from wall
        ball.y_bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() == 330 or ball.distance(l_paddle) < 50 and ball.xcor() == -330:
        # Bounce from paddle
        ball.x_bounce()
    # Detect past R paddle
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # Detect past L paddle
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()



















screen.exitonclick()