from turtle  import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time

new_snake = Snake()
food = Food()

my_screen = Screen()
my_screen.setup(width=600, height=650)
my_screen.bgcolor("black")
my_screen.title("my snake Game")
my_screen.tracer(0)

my_screen.listen()
my_screen.onkey(new_snake.up,"Up")
my_screen.onkey(new_snake.down,"Down")
my_screen.onkey(new_snake.right,"Right")
my_screen.onkey(new_snake.left,"Left")

score = ScoreBoard()
is_game_on = True
while is_game_on:
    my_screen.update()
    time.sleep(0.1)
    new_snake.snake_move()

    if new_snake.snake_head.distance(food) < 15:
        food.refresh()
        new_snake.extend()
        score.inc_score()

    if new_snake.snake_head.xcor() > 280 or new_snake.snake_head.xcor() < -280 or new_snake.snake_head.ycor() > 280 or new_snake.snake_head.ycor() < -280:
        is_game_on = False
        score.game_over()

    for part in new_snake.snake_part[1:]:
        if new_snake.snake_head.distance(part) < 10:
            is_game_on = False
            score.game_over()


my_screen.exitonclick()
