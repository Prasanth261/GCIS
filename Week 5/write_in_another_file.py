"""
1.Create a text file with atleast 5 lines
2- Read the file
3- In the same program, write the text which you are reading from the previous file, in a new file"""

with open("File25.txt") as f:
    read=f.read()





















    with open("File25_New.txt",'w') as g:
        g.write(read)