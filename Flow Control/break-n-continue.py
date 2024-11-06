numbers = [10, -5, 20, 15, -3, 55, 30, 40]

for num in numbers:
    if num < 0:
        # Skip the current iteration if the number is negative
        continue
    
    if num > 50:
        # Exit the loop if the number is greater than 50
        print("Found a number greater than 50:", num)
        break
    
    print("Processing number:", num)
