# Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# Comparison Operators
print("\nComparison Operators:")
print("Equal to:", a == b)
print("Not equal to:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than or equal to:", a >= b)
print("Less than or equal to:", a <= b)

# Logical Operators
x = True
y = False
print("\nLogical Operators:")
print("AND:", x and y)
print("OR:", x or y)
print("NOT:", not x)

# Bitwise Operators
m = 5  # Binary: 0101
n = 3  # Binary: 0011
print("\nBitwise Operators:")
print("Bitwise AND:", m & n)
print("Bitwise OR:", m | n)
print("Bitwise XOR:", m ^ n)
print("Bitwise NOT (~m):", ~m)
print("Left Shift (m << 1):", m << 1)
print("Right Shift (m >> 1):", m >> 1)

# Assignment Operators
print("\nAssignment Operators:")
c = 10
print("c =", c)
c += 5
print("c += 5:", c)
c -= 3
print("c -= 3:", c)
c *= 2
print("c *= 2:", c)
c /= 4
print("c /= 4:", c)
c %= 3
print("c %= 3:", c)
c **= 2
print("c **= 2:", c)
c //= 2
print("c //= 2:", c)

# Identity Operators
print("\nIdentity Operators:")
print("a is b:", a is b)
print("a is not b:", a is not b)

# Membership Operators
text = "Hello, Python!"
print("\nMembership Operators:")
print("'H' in text:", 'H' in text)
print("'Python' in text:", 'Python' in text)
print("'world' not in text:", 'world' not in text)