# fish.py

import os
import time


os.system("cls")

Data = [12, 45, 7, 23, 89, 34, 56, 78, 90, 11]  # Example data set with random numbers

print("Data set:", Data)

print("Linear search:")

try:
    user_input = int(input("Enter a number to search for: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
else:
    found = False
    for num in Data:
        if num == user_input:
            found = True
            break

    if found:
        print(f"{user_input} is in the data set.")
    else:
        print(f"{user_input} is NOT in the data set.")



print("Binary search:")



        # Binary search implementation
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Sort the data for binary search
sorted_data = sorted(Data)
print("Sorted data set for binary search:", sorted_data)

try:
    user_input_bs = int(input("Enter a number to search for using binary search: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
else:
    if binary_search(sorted_data, user_input_bs):
        print(f"{user_input_bs} is in the data set (binary search).")
    else:
        print(f"{user_input_bs} is NOT in the data set (binary search).")

time.sleep(3)
os.system("cls")


print("Bubble sort:")

Sorting = [64, 34, 25, 12, 22, 11, 90]

print("Original Sorting data set:", Sorting)

# Bubble sort implementation
n = len(Sorting)
for i in range(n):
    for j in range(0, n - i - 1):
        if Sorting[j] > Sorting[j + 1]:
            Sorting[j], Sorting[j + 1] = Sorting[j + 1], Sorting[j]

print("Sorted Sorting data set (Bubble sort):", Sorting)


print("insertion sort:")

# Insertion sort implementation
InsertionSorting = [64, 34, 25, 12, 22, 11, 90]
print("Original InsertionSorting data set:", InsertionSorting)

for i in range(1, len(InsertionSorting)):
    key = InsertionSorting[i]
    j = i - 1
    while j >= 0 and InsertionSorting[j] > key:
        InsertionSorting[j + 1] = InsertionSorting[j]
        j -= 1
    InsertionSorting[j + 1] = key

print("Sorted InsertionSorting data set (Insertion sort):", InsertionSorting)


print("Merge sort:")

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Merge the temp arrays back into arr
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Check if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Make a copy of Sorting to preserve the original
SortingForMerge = Sorting.copy()
print("Original Sorting data set for merge sort:", SortingForMerge)
merge_sort(SortingForMerge)
print("Sorted Sorting data set (Merge sort):", SortingForMerge)
