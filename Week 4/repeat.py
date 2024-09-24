def repeat_even(start,end):
    x=start
    while x<=end:
        if x%2==0:
         print(x)
        x+=1
def main():
    repeat_even(2,20)

if __name__=="__main__":
   main()

