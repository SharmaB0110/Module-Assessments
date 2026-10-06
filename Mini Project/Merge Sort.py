# Merge Sort Function
from py_compile import main


def merge_sort(arr):
 if len(arr) > 1:
  mid = len(arr) // 2

# Divide the array into two halves
  left_half = arr[:mid]
  right_half = arr[mid:]

# Recursively sort both halves
  merge_sort(left_half)
  merge_sort(right_half)
  i = j = k = 0

# Merge the sorted halves
  while i < len(left_half) and j < len(right_half):
 
   if left_half[i] < right_half[j]:
    arr[k] = left_half[i]
  i += 1
 else:
  arr[k] = right_half[j]
  j += 1
  k += 1

# Copy remaining elements of left_half
 while i < len(left_half):
  arr[k] = left_half[i]
  i += 1
  k += 1

# Copy remaining elements of right_half
 while j < len(right_half):
  arr[k] = right_half[j]
  j += 1
  k += 1

# Step 1: Create a random list of numbers
 numbers = [random.randint(1, 100) for _ in range(10)]

 print("Original List:")
 print(numbers)

# Step 2: Apply Merge Sort
 merge_sort(numbers)

# Step 3: Print the sorted list
 print("\nSorted List:")
 print(numbers)

main()
