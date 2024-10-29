import time

sum=0

#calculate the time it takes to sum the number till 1 milion 

begin=time.perf_counter()

for i in range(1000000):
    sum+=i

end=time.perf_counter()
elapsed=end-begin
print(elapsed)