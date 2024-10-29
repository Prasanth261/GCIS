import turtle as t

angle=76

#2.3.3
def turtle_drive():
    t.forward(100)
    t.left(86)
    t.setheading(127)
    t.down()
    t.goto(50,50)
    t.home()
    t.circle(25)
    input("Please enter to continue")

#2.3.5
def turtle_state():
    print(t.isdown())
    print(t.heading())
    print(t.xcor())
    print(t.ycor())

#2.3.6-10   
def square(angle,size=10):
    t.pensize(4)
    t.pencolor("red")
    t.fillcolor("blue")
    t.begin_fill()
    t.left(angle)
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.right(180)
    t.end_fill()
    input("Enter to continue: ")



def main():
    # turtle_state()
    # turtle_drive()
    t.bgcolor('pink')
    square(140,100)
    square(120,80)
    square(100,50)
    turtle_state()

main()