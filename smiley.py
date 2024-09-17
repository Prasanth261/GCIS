import turtle

t=turtle

def draw_circle(color='Red',rad=10):
    t.fillcolor(color)
    t.up()
    t.forward(rad)
    t.left(90)
    t.down()
    t.begin_fill()
    t.circle(rad)
    t.end_fill()
    t.up()
    t.left(90)
    t.forward(rad)
    t.right(180)
    print(t.xcor())
    print(t.ycor())

def draw_smiley(color,radius):
    draw_circle('yellow',radius)
    draw_circle('LightCoral',radius/12)
    draw_eye(radius*0.35,radius*0.25,color,radius*0.25)
    draw_eye(-(radius*0.35),radius*0.25,color,radius*0.25)
    mouth(radius*0.35)
    input(" ENTER")

def draw_eye(x,y,color,radius):
    t.up()
    t.goto(x,y)
    t.down()
    draw_circle('white',radius)
    draw_circle(color,radius/2)
    draw_circle('black',radius/4)
    t.goto(x-radius,y-radius)


def tweak():
    t.speed(0)
    t.tracer(True)
    # t.hideturtle()

def mouth(radius):
    t.down()
    t.speed(1)
    t.right(180)
    t.forward(50)
    t.right(180)
    t.right(90)
    t.circle(radius,180)
    t.left(90)
    t.forward(50)
    


def main():
    tweak()
    draw_smiley('blue',150)

main()