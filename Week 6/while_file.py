import array as a

def while_file(an_array):
    print(f"Before: {an_array}")
    for i in range(len(an_array)):
        an_array[i]=i
    print(f"After: {an_array}")
def main():
    an_array=a.array("i",[0]*10)
    while_file(an_array)
main()
