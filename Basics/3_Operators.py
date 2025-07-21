a = 15
b = 4
# Addition
print("Addition:", a + b)  # Addition: 19
# Subtraction
print("Subtraction:", a - b)  # Subtraction: 11
# Multiplication
print("Multiplication:", a * b)  # Multiplication: 60
# Division
print("Division:", a / b) # Division: 3.75
# Floor Division
print("Floor Division:", a // b)  # Floor Division: 3
# Modulus
print("Modulus:", a % b) # Modulus: 3
# Exponentiation
print("Exponentiation:", a ** b) # Exponentiation: 50625

a = 13
b = 33
print(a > b) # False
print(a < b) # True
print(a == b) # False
print(a != b) # True
print(a >= b) # False
print(a <= b) # True

a = True
b = False
print(a and b) # False
print(a or b) # True
print(not a) # False

a = 10
b = 4
print(a & b) # Bitwise AND
print(a | b) # Bitwise OR
print(~a) # Bitwise NOT
print(a ^ b) # Bitwise XOR
print(a >> 2) # Bitwise Right Shift
print(a << 2) # Bitwise Left Shift
# 0
# 14
# -11
# 14
# 2
# 40

a = 10
b = a
print(b) # 10
b += a
print(b) # 20
b -= a
print(b) # 10
b *= a
print(b) # 100
b <<= a
print(b) # 102400

a = 10
b = 20
c = a
print(a is not b) # True
print(a is c) # True

x = 24
y = 20
list = [10, 20, 30, 40, 50]
if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")
if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")
# x is NOT present in given list
# y is present in given list
# Ternary Operator in Python

a, b = 10, 20
min = a if a < b else b
print(min) # 10

expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0
if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")

# 610
# Hello! Welcome.

print(100 / 10 * 10) # 100.0
print(5 - 2 + 3) # 6
print(5 - (2 + 3)) # 0
print(2 ** 3 ** 2) # 512

#--
num1 = "5"
num2 = 3
result = num1 * num2
print(result) # "555"

x = float(input()) # 2
print(x) # 2.0
