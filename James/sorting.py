import random

arr = random.sample(range(100), 7)
print(f"Unsorted list: ", arr)

def bubble_sort(arr):
    for i in range(len(arr) - 1):        
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

        print()
    return arr

def selection_sort(arr):
    for i in range(len(arr) - 1):
        minimun_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimun_index]:
                minimun_index = j

        temp = arr[i]
        arr[i] = arr[minimun_index]
        arr[minimun_index] = temp
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
       current = arr[i]
       previous_index = i - 1

       while previous_index > -1 and arr[previous_index] > current:
           arr[previous_index + 1] = arr[previous_index]
           previous_index -= 1
       arr[previous_index + 1] = current

    return arr

def insertion_sort1(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]

        while arr[i - 1] > current_value and i > -1:
            temp = arr[i - 1]
            arr[i - 1] = current_value
            arr[i] = temp
            i -= 1
    
    return arr




print(f"Sorted list: ", insertion_sort1(arr))