"""Create a text file in your filesystem
Add all numbers within the file using exception handling
"""
def file_sum(filepath):
    try:
        with open(filepath) as f:
            try:
                sum1=0
                for i in f:
                    each_number=i.split()
                    print(each_number)
                    for y in each_number:
                     sum1=sum1+int(y)
                print(sum1)
            except ValueError:
                print("File Has other than integers")
            except TypeError:
                print("File has invalid data type or missing type casting")
    except FileNotFoundError:
        print("INVALID FILE PATH")
def main():
    filepath="Week 5\\number.txt"
    file_sum(filepath)

if __name__=="__main__":
    main()
