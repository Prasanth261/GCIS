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
def main():
    t.speed(0)
    t.penup()
    t.goto(-300,300)
    t.pendown()
    grid(4,7)
    t.done()

if __name__=="__main__":
    main()
