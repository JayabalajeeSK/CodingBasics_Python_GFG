#  int, float, string, list and set
x = 50
x = 60.5
x = "Hello World"
x = ["geeks", "for", "geeks"]
x = ("geeks", "for", "geeks")
# Creating complex numbers
c1 = complex(3, 4)  
c2 = complex(5)     
c3 = complex()      
print(c1) # (3+4j)
print(c2) # (5+0j)
print(c3) # 0j
print(c1.real) # 3.0
print(c1.imag) # 4.0

a = 5
print(type(a)) # <class 'int'>
b = 5.0
print(type(b)) # <class 'float'>
c = 2 + 4j
print(type(c)) # <class 'complex'>

s = 'Welcome to the Geeks World'
print(s) # Welcome to the Geeks World
# check data type 
print(type(s)) # <class 'str'>
# access string with index
print(s[1]) # e
print(s[2]) # l
print(s[-1]) # d

# Empty list
a = []
# list with int values
a = [1, 2, 3]
print(a) # [1, 2, 3]
# list with mixed int and string
b = ["Geeks", "For", "Geeks", 4, 5]
print(b) # ['Geeks', 'For', 'Geeks', 4, 5]

a = ["Geeks", "For", "Geeks"]
print("Accessing element from the list")
print(a[0]) # Geeks
print(a[2]) # Geeks
print("Accessing element using negative indexing")
print(a[-1]) # Geeks
print(a[-3]) # Geeks

# initiate empty tuple
tup1 = ()
tup2 = ('Geeks', 'For')
print("\nTuple with the use of String: ", tup2) # Tuple with the use of String:  ('Geeks', 'For')
tup1 = tuple([1, 2, 3, 4, 5])
# access tuple items
print(tup1[0]) # 1
print(tup1[-1]) # 5
print(tup1[-3]) # 3

print(type(True)) # <class 'bool'>
print(type(False)) # <class 'bool'>
# print(type(true)) #NameError

# initializing empty set
s1 = set()
s1 = set("GeeksForGeeks")
print("Set with the use of String: ", s1) # Set with the use of String:  {'s', 'o', 'F', 'G', 'e', 'k', 'r'}
s2 = set(["Geeks", "For", "Geeks"])
print("Set with the use of List: ", s2) # Set with the use of List:  {'Geeks', 'For'}

set1 = set(["Geeks", "For", "Geeks"])
print(set1) # {'Geeks', 'For'}
# loop through set
for i in set1:
    print(i, end=" ")
# check if item exist in set    
print("Geeks" in set1) # Geeks For True

# initialize empty dictionary
d = {}
d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d) # {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1) # {1: 'Geeks', 2: 'For', 3: 'Geeks'}

d = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# Accessing an element using key
print(d['name']) # For
# Accessing a element using get
print(d.get(3)) # Geeks

fruits = ["apple", "banana", "orange"]
print(fruits) # ['apple', 'banana', 'orange']
fruits.append("grape") # at last
print(fruits) # ['apple', 'banana', 'orange', 'grape']
fruits.remove("orange")
print(fruits) # ['apple', 'banana', 'grape']

coordinates = (3, 5)
print(coordinates) # (3, 5)
print("X-coordinate:", coordinates[0])  # X-coordinate: 3
print("Y-coordinate:", coordinates[1])  # Y-coordinate: 5

s = set([1, 2, 3])
s.add(4)
s.remove(2)
print(s)  # Output: {1, 3, 4}
fs = frozenset([1, 2, 3])
# fs.add(4)  # ❌ Error: 'frozenset' object has no attribute 'add'
print(fs)    # Output: frozenset({1, 2, 3})

a = [1, 2, 3]
b = a         # No copy, just reference
b[0] = 100
print(a)      # Output: [100, 2, 3]
import copy
a = [[1, 2], [3, 4]]
b = copy.copy(a)     # Shallow copy
b[0][0] = 100
print(a)             # Output: [[100, 2], [3, 4]]
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)  # Deep copy
b[0][0] = 100
print(a)              # Output: [[1, 2], [3, 4]]

b = bytes([65, 66, 67])
print(b)         # Output: b'ABC'
print(b[0])      # Output: 65
# b[0] = 70     ❌ Error: 'bytes' object does not support item assignment

ba = bytearray([65, 66, 67])
ba[0] = 70
print(ba)        # Output: bytearray(b'FBC')

ba = bytearray([10, 20, 30, 40])
mv = memoryview(ba)
mv[1] = 99
print(ba)        # Output: bytearray(b'\ncc(')
print(mv[1])     # Output: 99