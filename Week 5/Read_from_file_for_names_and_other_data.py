
# #Dirty Data not working program
# def print_data(filepath):
#     with open(filepath) as f:
#         next(f)
#         for i in f:
#             words=i.split(",")
#             print(f"Name:<{words[0]}>,Address:<{words[1]}>")
# # print_data('grades.csv')

# import csv
# #By using CSV module to deal with dirty data
# def print_data_csv(filepath):
#     with open(filepath) as f:
#         read=csv.reader(f)
#         next(read)
#         for i in read:
#             print(f"Name:<{i[0]}>,Address:<{i[1]}>")
# print_data_csv('grades.csv')

import csv
def read_csv(filepath):
    try:
        with open(filepath) as f:
            read=csv.reader(f)
            next(read)
            next(read)
            next(read)
            for i in read:
                print(i)
    except FileNotFoundError:
        print("Invalid FILE PATH")
read_csv('grades.csv')