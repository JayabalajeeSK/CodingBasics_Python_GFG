name = input("Enter your name: ")
print("Hello,", name, "! Welcome!") #Hello, jayabalajee ! Welcome!

name = "jaya"
age = 22
print(name) # jaya
print(name, age) # jaya 22

x, y, z = input("Enter three values: ").split() #Enter three values: 5 6 8
print("Total number of students: ", x) #Total number of students:  5
print("Number of boys is : ", y) #Number of boys is :  6
print("Number of girls is : ", z) #Number of girls is :  8

n = int(input("How many roses?: "))
print(n) # 88
price = float(input("Price of each rose?: ")) # 50.90
print(price) # 50.9

a = "Hello World"
b = 10
c = 11.22
d = ("Geeks", "for", "Geeks")
e = ["Geeks", "for", "Geeks"]
f = {"Geeks": 1, "for":2, "Geeks":3}

print(type(a)) #<class 'str'>
print(type(b)) #<class 'int'>
print(type(c)) #<class 'float'>
print(type(d)) #<class 'tuple'>
print(type(e)) #<class 'list'>
print(type(f)) #<class 'dict'>

# format()
amount = 150.75
print("Amount: ${:.2f}".format(amount)) # Amount: $150.75

# end Parameter with '@'
print("Python", end='@') 
print("GeeksforGeeks") # Python@GeeksforGeeks

# Seprating with Comma
print('G', 'F', 'G', sep='') # GFG

# for formatting a date
print('09', '12', '2016', sep='-') # 09-12-2016

# another example
print('jaya', 'geeksforgeeks', sep='@') # jaya@geeksforgeeks

#Using f-string
name = 'Jaya'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.") # Hello, My name is Jaya and I'm 23 years old.

num = int(input("Enter a value: ")) # 50
add = num + 5
print("The sum is %d" %add) # The sum is 55

# val1 = raw_input("Enter the name: ")
# print(type(val1))
# print(val1)

# val2 = raw_input("Enter the number: ")
# print(type(val2))
# val2 = int(val2)
# print(type(val2))
# print(val2)