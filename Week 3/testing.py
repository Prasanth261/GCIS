def cube(x):
    cube=x**3
    return cube
def multiply(x,y):
    return x+y
def test_cube():
    assert cube(2)==8
def test_multiply():
    assert multiply(2,3) == 6
def main():
    test_cube()
    test_multiply()
main()

#test
