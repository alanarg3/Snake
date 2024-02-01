from turtle import Screen,Turtle
import snake
import food
import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)
snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    snake.move()

    #detect collision w/ food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # if collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            game_over()

    def game_over():
        end_title = Turtle()
        end_title.hideturtle()
        end_title.color("white")
        end_title.write("Game Over", False, "center", ("Courier", 14, "normal"))




screen.exitonclick()
