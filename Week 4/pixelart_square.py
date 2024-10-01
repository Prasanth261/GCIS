import turtle as t
def pixel(pixelsize=30):
    i=0
    while i<4:
        t.forward(pixelsize)
        t.right(90)
        i+=1
def column(column_no=20):
    i=0
    forward=0
    while i<column_no:
        pixel()
        forward+=30
        t.forward(30)
        i=i+1
    return forward
def grid(no_rows=2,column_no=2):
    i=0
    while i<no_rows:
        var=column(column_no)
        t.right(180)
        t.forward(var)
        t.left(90)
        t.forward(30)
        t.left(90)
        i+=1
def pixel_color(color='blue'):
    i=0
    t.fillcolor(color)
    t.begin_fill()
    while i<4:
        t.forward(30)
        t.left(90)
        i+=1
    t.end_fill()
    
def column_color(column_no=20):
    i=0
    forward=0
    while i<column_no:
        pixel_color()
        forward+=30
        t.forward(30)
        i=i+1
    return forward

def grid_color(no_rows=2,column_no=2):
    i=0
    while i<no_rows:
        var=column_color(column_no)
        t.right(180)
        t.forward(var)
        if i==no_rows-1:
            t.right(90)
            t.forward(var)
            t.right(90)
            break
        t.left(90)
        t.forward(30)
        t.left(90)
        i+=1

def square(column,row_no,size,grid_row):
    t.left(90)
    t.forward(row_no*30)
    t.right(90)
    t.forward(column*30)
    grid_color(size,size)
    t.right(180)
    t.penup()
    t.forward(column*30)
    t.left(90)
    t.forward(row_no*30)
    t.left(90)
    t.pendown()


def main():
    t.speed(0)
    t.penup()
    t.goto(-300,300)
    t.pendown()
    grid(6,6)
    grid_row=6
    square(3-1,grid_row-3,2,6)
    t.done()

if __name__=="__main__":
    main()