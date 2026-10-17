
import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Drawing")

board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()
colours = ["red", "orange", "green", "cyan", "yellow", "purple", "blue", "pink", "brown", "gray"]
for i in range(80):
    board.color(colours[i % len(colours)])
    board.width(2)
    board.forward(i * 2)
    board.right(91)
board.penup()
board.goto(0, -60)
board.setheading(90)
board.pendown()
board.color("gold", "yellow")
board.begin_fill() 
for i in range(5):
    board.forward(120)
    board.right(144)
board.end_fill()    

board.penup()
board.goto(0, 0)
board.pendown
petal_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(36):
    board.color(petal_colors[i % len(petal_colors)]),
    petal_colors[(i + 2) % len(petal_colors)]
    board.begin_fill()
    for j in range(4):
        board.forward(55)
        board.right(90)
    board.end_fill()
    board.right(10)
    turtle.done()
