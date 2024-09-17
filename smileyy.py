import turtle
def draw_circle(x,y,radius,fill_color):
    turtle.goto(x,y)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def main():
    draw_circle(0,0,100,"blue")
    #draw_circle(10,10,50,"red")
    #draw_circle(20,20,100,"green")
    input("click to exit:")

main()