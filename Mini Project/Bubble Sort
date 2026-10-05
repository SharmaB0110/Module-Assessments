import random

# Create a random list of numbers
numbers = [random.randint(1, 100) for _ in range(10)]

print("Original list:", numbers)

# Bubble Sort
for i in range(len(numbers)):
 for j in range(len(numbers) - i - 1):
  if numbers[j] > numbers[j+1]:
    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Print the sorted list
print("Sorted list:", numbers)
