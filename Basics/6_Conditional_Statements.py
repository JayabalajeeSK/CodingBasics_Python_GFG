age = 20
if age >= 18:
    print("Eligible to vote.") # Eligible to vote.

age = 19
if age > 18: print("Eligible to Vote.") # Eligible to vote.

age = 10
if age <= 12:
    print("Travel for free.") # Travel for free.
else:
    print("Pay for ticket.")
marks = 45
res = "Pass" if marks >= 40 else "Fail"
print(f"Result: {res}")

age = 22
if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.") # Young adult.
else:
    print("Adult.")

age = 70
is_member = True
if age >= 60:
    if is_member:
        print("30% senior discount!") # 30% senior discount!
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")

# Assign a value based on a condition
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s) # Adult

number = 2
match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three") # Two or Three
    case _:
        print("Other number")

x = 10
if x > 5:
   print("Greater than 5") # Greater than 5
elif x > 8:
   print("Greater than 8")
else:
   print("Less than or equal to 5")