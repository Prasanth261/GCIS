from calculation import *
def test_add():
    x,y=5,6
    addition = add(x,y)
    assert addition==11
def test_multiply():
    x,y=5,6
    multiply = multiple(x,y)
    assert multiply==30
def test_subraction():
    x,y=5,6
    subraction = subtract(x,y)
    assert subraction==-1
