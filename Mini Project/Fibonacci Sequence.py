# Define required variables
n = int(input("Enter the number of Fibonacci terms: "))

first = 1
second = 1

print("Fibonacci Sequence:")

# Generate Fibonacci sequence
for i in range(n):
 print(first)

 next_num = first + second
 first = second
 second = next_num