import random

def linear_search(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1

def binary_search(values, target, low, high):
    mid = (low + high) // 2

    if low > high:
        print(f"{low} {mid} {high}")
        return -1
    if values[mid] == target:
        print(f"{low} {mid} {high}")
        return mid
    elif values[mid] > target:
        print(f"{low} {mid} {high}")
        return binary_search(values, target, low, mid - 1)
    else:
        print(f"{low} {mid} {high}")
        return binary_search(values, target, mid + 1, high)
        
def get_values():
    values = random.sample(range(20), k=10)
    #target = input("Enter value to searach: ")
    values = sorted(values)
    print(f"Values: {values}")
    target = int(input("Enter value to searach: "))
    result = binary_search(values, target, 0, len(values) - 1)

    if result == -1:
        print(f"{target} not found")
    else:
        print(f"{target} is at index {result}")

get_values()

student = {
    "name": "John Doe",
    "age": 21,
    "grades": [56,78,91]
}
student["major"] = "Computer Science"
student["age"] = 20

del student["grades"]

for key, value in student.items():
    print(f"{key}: {value}")
    
#print(student)