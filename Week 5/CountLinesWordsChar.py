"""This Python Code will read a text file
counts its lines
counts its words
and then counts its total characters"""
def count_lines_words_Chars(filePath):
    #open file for reading
    with open(filePath) as f:
        # lines=f.readlines()
        count=0
        count_words=0
        for line in f:
            count+=1
            print(line.strip())
            count_words=count_words+len(line.split())


        print(f"Number of lines:{count}")
        print(f"Number of words:{count_words}")
    
def main():
    filePath="Week 5\\sample.txt"
    count_lines_words_Chars(filePath)



if __name__=="__main__":
    main()
