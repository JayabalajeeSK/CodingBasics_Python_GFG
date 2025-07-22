s = ["Geeks", "for", "Geeks"]
# using for loop with string
for i in s:
    print(i)
# Geeks
# for
# Geeks

s = "Geeks"
for i in s:
    print(i)
# G
# e
# e
# k
# s

for i in range(0, 10, 2):
    print(i)
# 0
# 2
# 4
# 6
# 8

# Prints all letters except 'e' and 's'

for i in 'geeksforgeeks':
    if i == 'e' or i == 's':
        continue
    print(i)
# g
# k
# f
# o
# r
# g
# k
#-----------------------
for i in 'geeksforgeeks':
    # break the loop as soon it sees 'e'
    # or 's'
    if i == 'e' or i == 's':
        break
print(i)
# e
#-----------------------
# An empty loop
for i in 'geeksforgeeks':
    pass
print(i)
# s

for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("No Break\n")
# 1
# 2
# 3
# No Break

li = ["eat", "sleep", "repeat"]
for i, j in enumerate(li):
    print (i, j)
# 0 eat
# 1 sleep
# 2 repeat

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3

a = ["shirt", "sock", "pants", "sock", "towel"]
b = []
for i in a:
    if i == "sock":
        continue
    else:
        print(f"Washing {i}")
b.append("socks")
print(f"Washing {b}")
# Washing shirt
# Washing pants
# Washing towel
# Washing ['socks']

for i in range(1, 8):
    d = 3 + (i - 1) * 0.5
    print(f"Day {i}: Run {d:.1f} miles")
# Day 1: Run 3.0 miles
# Day 2: Run 3.5 miles
# Day 3: Run 4.0 miles
# Day 4: Run 4.5 miles
# Day 5: Run 5.0 miles
# Day 6: Run 5.5 miles
# Day 7: Run 6.0 miles

i = 1
while i <= 3:
    print(i)
    i += 1
# 1
# 2
# 3

i = 1
while True:
    print(i)
    i += 1
    if i > 3:
        break
# 1
# 2
# 3

for i in range(2):         # Outer loop
    for j in range(3):     # Inner loop
        print(f"i={i}, j={j}")
# i=0, j=0
# i=0, j=1
# i=0, j=2
# i=1, j=0
# i=1, j=1
# i=1, j=2
#------------------------------
i = 1
while i <= 2:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1
# i=1, j=1
# i=1, j=2
# i=1, j=3
# i=2, j=1
# i=2, j=2
# i=2, j=3
#---------------------------------
for i in range(1, 4):     # Rows
    for j in range(1, i+1):  # Columns
        print("*", end=" ")
    print()
# *
# * *
# * * *

# ⚠️ Be Careful: Reset inner loop counters properly.
# Avoid infinite loops in while inside while.

numbers = [3, 7, 2, 8, 5]
for i, num in enumerate(numbers):
   if i == num:
       break
   print(num, end=' ') # 3 7