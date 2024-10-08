#method 1
def print_lines(filename):
    with open(filename) as f:
        for line in f:
            print(line.strip())
        f.close()
print_lines(r"C:\Users\Spras\OneDrive\Desktop\RIT Dubai- Python\Week 4\testing.txt")

#method 2