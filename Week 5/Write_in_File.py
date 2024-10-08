"""This is a python code will line some text content
in a text file
1-Don't forget to write the 'w' mode
2-Even if you don't create the file in path, it will create a new file for you"""
def write_in_File(filePath,multilines):
    with open(filePath,'w') as f:
        for i in multilines:
            f.write(i+"\n")
def main():
    filePath="File25.txt"
    multiLines=["My name is MAK","I am in GCIS123","This is section 601"]
    write_in_File(filePath,multiLines)

if __name__=="__main__":
    main()

