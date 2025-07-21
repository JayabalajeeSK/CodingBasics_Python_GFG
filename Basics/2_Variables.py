x = 5
name = "Samantha"  
print(x) # 5
print(name) # Samantha

#Valid
age = 21
_colour = "lilac" 
total_score = 90

# #Invalid
# 1name = "Error"  # Starts with a digit
# class = 10       # 'class' is a reserved keyword
# user-name = "Doe"  # Contains a hyphen

x = 5
y = 3.14
z = "Hi"

x = 10
x = "Now a string" #Lastest value of x

a = b = c = 100
print(a, b, c) # 100 100 100

s = "10"  # Initially a string
n = int(s)  # Cast string to integer
cnt = 5
f = float(cnt)  # Cast integer to float
age = 25
s2 = str(age)  # Cast integer to string

print(n)  # 10
print(f)  # 5.0
print(s2) # 25

n = 42
print(type(n))   # <class 'int'>
f = 3.14
print(type(f))   # <class 'float'>
s = "Hello, World!"
print(type(s))   # <class 'str'>
li = [1, 2, 3]
print(type(li))  # <class 'list'>
d = {'key': 'value'}
print(type(d))   # <class 'dict'>
bool = True
print(type(bool))# <class 'bool'>

x = 10
print(x) # 10
del x # Trying to print x after deletion will raise an error
# print(x)  # Uncommenting this line will raise NameError: name 'x' is not defined

a, b = 5, 10
print(a, b) # 5 10
a, b = b, a # a=b b=a
print(a, b) # 10 5

word = "Python"
length = len(word)
print("Length of the word:", length) # Length of the word: 6