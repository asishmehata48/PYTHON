# Take user input
number = int(input("Enter a number: "))

# Top-level if-elif-else structure
if number > 0:
    print("The number is positive.")
    
    # Nested conditionals for even and odd
    if number % 2 == 0:
        print("The number is also even.")
    else:
        print("The number is odd.")
        
elif number < 0:
    print("The number is negative.")
    
    # Nested conditional to check if the number is divisible by 5
    if number % 5 == 0:
        print("The number is also divisible by 5.")
    else:
        print("The number is not divisible by 5.")
        
else:
    print("The number is zero, which is neither positive nor negative.")

    # Nested conditional for zero-specific message
    if number == 0:
        print("Zero is neither even nor odd.")