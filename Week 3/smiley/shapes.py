import turtle

def draw_without_tracer():
    turtle.speed(10)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.tracer(False)

    for i in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.tracer(True)

    turtle.penup()
    turtle.goto(200,200)
    turtle.pendown()

    for i in range(2):
        turtle.forward(150)
        turtle.left(90)
        turtle.forward(75)
        turtle.left(90)
    turtle.hideturtle()

def main():
    turtle.Screen()
    draw_without_tracer()
    turtle.exitonclick()

main()
