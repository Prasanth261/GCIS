import csv
def ReadCSV(filepath):
    with open(filepath,'r') as f:
        CSVReader=csv.reader(f)
        #to remove the header
        next(CSVReader)
        total=0
        for line in CSVReader:
            total=total+int(line[2])
        avg=total/3
        return avg

def main():
    filepath="marks.csv"
    print(f"Avg Marks:{ReadCSV(filepath)}")

if __name__=="__main__":
    main()