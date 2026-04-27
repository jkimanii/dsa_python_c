import random

def max_min(numbers):
    minimum = numbers[0]
    maximum = numbers[-1]
    for num in numbers:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return minimum, maximum

def get_values():
    list = random.sample(range(100), k=10)
    
    return list, max_min(list)

list, (minimum, maximum) = get_values()

print(f"Random sample: {list}")
print(f"Minimum number: {minimum}\nMaximum number: {maximum}")
