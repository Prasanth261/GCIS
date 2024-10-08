def wordsearch(file):
    f=open(file,"r")
    read=f.read()
    f.close()
    lines=read.split()
    word=input("Enter a word to be searched: ")
    detector=0
    for i in lines:
        if i==word:
            print("The word was found:",i)
            detector=1
    if detector==0:
        print("word was not found")

def longest_word(string):
   read=string.split()
   j=''
   count=0
   for i in read:
      if len(i)>count:
         j=i
         count=len(i)
   print("The longest word is:",j)
def longest_words(filename):
   f=open(filename,"r")
   read=f.readlines()
   f.close()
   for i in read:
      longest_word(i)


def main():
 wordsearch(r"C:\Users\Spras\OneDrive\Desktop\RIT Dubai- Python\Week 4\testing.txt")
 longest_words(r"C:\Users\Spras\OneDrive\Desktop\RIT Dubai- Python\Week 4\testing.txt")
 

if __name__=="__main__":
   main()
