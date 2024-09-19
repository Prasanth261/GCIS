import turtle

def draw_circle(x,y,radius,fill_color):
    turtle.goto(x,y)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_centered_circle(x,y,radius,fill_color):
    
    # Select color for filling the color of the shape using a parameter.
    # Move the turtle to a specific set of coordinates using the parameters.
    # Lift the pen so that we're able to draw a perfect circle.
    # Move foward to the point of radius using a parameter.
    # Turn left to begin drawing the circle around the coordinates we have to go back to.
    # Drop the pen down in order to begin drawing the centered circle using the parameter.
    # Enter the command to begin filling the color in the shape we are about to draw.
    # Draw the circle using the parameter.
    # Enter the command to end filling the color of the circle.
    # Lift the pen up in order to move back to the center of the circle without drawing a line.
    # Turn left.
    # Move forward to the coordinates using parameters to the center of the circle.
    # Turn a certain amount to face the original position we started with.
    # Drop the pen back down.

    turtle.fillcolor(fill_color)
    turtle.goto(x,y)
    turtle.penup()
    turtle.forward(radius)
    turtle.left(90)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()
    turtle.left(90)
    turtle.forward(radius)
    turtle.left(180)
    turtle.pendown()

def main():
    draw_centered_circle(0,0,50,"red")
    input("Click enter to exit: ")

main()