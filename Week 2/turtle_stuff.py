import turtle
angle=76

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

def turtle_state():
    t = turtle.Turtle()
    print(t.isdown())
    print(t.heading())
    print(t.xcor())
    print(t.ycor())
    
def square():
    t = turtle.Turtle()
    angle=65
    t.left(angle)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    input("Enter to continue: ")

def param_square(size=10):
    t = turtle.Turtle()
    for i in range(3):
        t.forward(size)
        t.right(90)
    t.forward(size)
    input("Enter to continue: ")

def main():
    turtle_state()
    # turtle_drive()
    square()
    # param_square(100)
    # param_square(250)
    # param_square(500)
    turtle_state()

main()