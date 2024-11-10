# ten_zeros=[0 for i in range(10)]
# print(ten_zeros)

# divis_3_5=[n for n in range(50) if n%3==0 and n%5==0]

# print(divis_3_5)

#creating 2D dimensional list
table=[[row * col for col in range(4)] for row in range(4)]
print(table)

#Ragged 2D dimensional list
table2=[[col*row for col in range(row+2)] for row in range(4)]
print(table2)

