arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14]
ratio = 0.5  # 70-30 split

split_index = int(len(arr) * ratio)
first_part = arr[:split_index]
second_part = arr[split_index:]
print(first_part)
print(second_part)