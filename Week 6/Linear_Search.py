import array as a 

an_array=a.array("i",[0]*10)
def while_file(an_array):
    for i in range(len(an_array)):
        an_array[i]=i

while_file(an_array)

def search(an_array,x):
    for i in range(len(an_array)):
        if an_array[i]==x:
            print(f"Index value is {i}")
            break
search(an_array,8)