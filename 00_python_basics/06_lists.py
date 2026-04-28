import random

list = random.sample(range(10),5)
print(list)
print(f"Start at index 2 {list[2:]}") # start at index 2
print(f"Stop at index 3 {list[:3]}") # stop at index 3
list.append(5)
list.append(6)
list.append(7)
list.append(8)
print(list)
list_a = list[-1] # get last index
print(list_a)

