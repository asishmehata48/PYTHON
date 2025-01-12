def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Example usage:
number = 7
if is_even(number):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
