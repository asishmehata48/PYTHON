# For loop to print numbers from 1 to 10
print("For Loop - Numbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print("\n")  # New line for separation

# While loop to calculate the factorial of a number
number = 5  # Change this number to calculate a different factorial
factorial = 1
counter = number

print(f"While Loop - Factorial of {number}:")
while counter > 0:
    factorial *= counter
    counter -= 1
print(f"Factorial of {number} is {factorial}\n")

# Nested loop to create a pattern
rows = 5  # Change this to modify the number of rows
print("Nested Loop - Pattern:")
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()  # New line after each row
    