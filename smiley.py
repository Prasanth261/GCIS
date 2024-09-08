import turtle

def draw_circle(color='Red',x=0,y=0,rad=10):
    t=turtle.Turtle()
    t.fillcolor(color)
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.circle(rad)
    t.end_fill()
    print(t.xcor())
    print(t.ycor())
    input("Enter to continue: ")

def draw_smiley():
    radius=150
    draw_circle('yellow',0,0,radius)
    draw_circle('LightCoral',0,radius-10,10)

def main():
    # radius=150
    # draw_circle('red',0,0,radius)
    # draw_circle('red',0,radius-10,10)
    draw_smiley()
main()


