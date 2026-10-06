import random

def insertion_sort(arr):
  for i in range(1, len(arr)):
   key = arr[i] # Current element
   j = i - 1

# Move elements that are greater than key
# one position ahead of their current position
   while j >= 0 and arr[j] > key:
    arr[j + 1] = arr[j]
    j -= 1
    arr[j + 1] = key

# Step 1: Create a random list of numbers
numbers = [random.randint(1, 100) for _ in range(10)]

##numbers= [57, 78, 7, 88, 9, 9, 22, 55]

print("Original List:")
print(numbers)

# Step 2: Apply Insertion Sort
insertion_sort(numbers)

# Step 3: Print the sorted list
print("\nSorted List:")
print(numbers)