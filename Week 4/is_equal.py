def is_equal(a,b,c):
    if a==b and b==c and c==a:
        return "Yes"
    else:
        return "No"

def main():
    print(is_equal(10,10,10))
    print(is_equal(20,10,30))
main()