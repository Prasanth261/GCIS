import arrays

def making_arrays():
    print(arrays.Array(5))
    print(arrays.Array(1,0))
    print(arrays.Array(10,""))
    print(arrays.Array(20,True))
    # count=0
    # array_a=arrays.Array(20,False)
    # while count<len(array_a):
    #    print(array_a[count])
    #    count+=1
                          
def for_fill(a):
   for i in range(len(a)):
      a[i]=i
def print_odds_rec(b,index):
   if index>=len(b):
      print(print_odds_rec.__name__)
      return 1
   
   if b[index]%2==0:
      print(f"even at {index} and number is {b[index]}")
   print_odds_rec(b,index+1)
def countdown(n):
   if n<0:
      return 0
   else:
      print(n)
      return n + countdown(n-1)

def factorial(n):
   if n<0:
      return "Undefined"
   if n==0 or n==1:
      return 1
   else:
      return n*factorial(n-1)
def countup(n):
   if n<0:
      return 0
   elif n==0:
      print(n)
   else:
      print(n) 
   countup(n-1)

def main():
   # array_b=arrays.Array(10,2)
   # #making_arrays()
   # #for_fill(array_b)
   # print(array_b)
   # print(print_odds_rec(array_b,0))
   # print(f"sum:{countdown(100000)}")
   # print(f"factorial:{factorial(100)}")
   countup(10)
   ...




if __name__=="__main__":
   main()
