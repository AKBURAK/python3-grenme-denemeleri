import turtle
turtle.pensize(3)
turtle.bgcolor("red")
turtle.pencolor("white")
for x in range(36):
    turtle.home()
    turtle.left(x*10)
    turtle.circle(100)
