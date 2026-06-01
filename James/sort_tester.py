import random

arr = random.sample(range(100), 7)
# arr = [76, 84, 40, 27, 25, 19, 93]
# print(f"Unsorted list: ", arr)
# print()
# count = 1

# def bubble_sort(arr, count):
#     for i in range(len(arr) - 1):        
#         print(f"Outer loop: ", i)

#         for j in range(len(arr) - 1 - i):
#             print()
#             print(f"Step: ", count)

#             print(f"List: ", arr)
#             print(f"Inner loop: ", j)
#             print(f"Current index value: ", arr[j])
#             print(f"Next value: ", arr[j + 1]) 

#             if arr[j] > arr[j + 1]:
#                 temp = arr[j]
#                 arr[j] = arr[j + 1]
#                 arr[j + 1] = temp
#             print(f"Sorted ", j, " : ", arr)
#             count += 1

#         print()
#     return arr

# def selection_sort(arr, count):
#     for i in range(len(arr) - 1):
#         print(f"Outer loop: ", i)
#         minimun_index = i

#         for j in range(i + 1, len(arr)):
#             print()
#             print(f"Step: ", count)

#             print(f"Minimum index: ", minimun_index)
#             print(f"Minimum index value: ", arr[minimun_index])
#             print(f"Next value: ", arr[j])

#             if arr[j] < arr[minimun_index]:
#                 minimun_index = j
#             count += 1

#         temp = arr[i]
#         arr[i] = arr[minimun_index]
#         arr[minimun_index] = temp

#         print(f"Sorted ", i, " : ", arr)
#         print()
#     return arr

def insertion_sort(arr, count):
    for i in range(1, len(arr)):
       print(f"Value ", i + 1)
       current = arr[i]
       previous_index = i - 1      

       print() 
       print(f"Current value: ", current)
       print(f"Previous value: ", arr[previous_index])

       while arr[previous_index] > current and previous_index > -1:
           print()
           print(f"Step: ", count)
           print(f"Previous value: ", arr[previous_index])
           print(f"Previous index: ", previous_index)

           arr[previous_index + 1] = arr[previous_index]
           print(f"Loop list: ", arr)
           previous_index -= 1         

           count += 1
       arr[previous_index + 1] = current

       print(f"List: ", arr)
       print()

    return arr

print(f"Sorted list: ", insertion_sort(arr, count))