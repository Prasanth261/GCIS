def square_area(length):
    area = length*length
    return area
def test_square_8():
    area= square_area(8)
    assert area ==64