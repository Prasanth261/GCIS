import turtle
def turtle_drive():
    t = turtle.Turtle()
    t.forward(100)
    t.left(86)
    t.setheading(127)
    t.down()
    t.goto(50,50)
    t.home()
    t.circle(25)
    input("Please enter to continue")

def main():
    turtle_drive()

main()