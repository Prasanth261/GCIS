import turtle

def draw_centered_circle(x,y,radius,fill_color):
    turt=turtle.Turtle()
    turt.speed(0)#0,1-10

    turt.penup()
    turt.goto(x,y-radius)
    turt.pendown()


    turt.fillcolor(fill_color)
    turt.begin_fill()
    turt.circle(radius)
    turt.end_fill()

    turt.hideturtle()

def main():
    turtle.Screen()
    draw_centered_circle(0,0,150,"yellow")
    draw_centered_circle(0,0,20,"pink")
    turtle.exitonclick()

main()
