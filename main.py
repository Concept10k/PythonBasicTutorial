# Using "in" to Check for Conditional Statements

# Check if 'i' is in the string 'Dynamic Concept'
if 'i' in 'Dynamic Concept':
    print("i is part of Dynamic Concept")  # Output: "i is part of Dynamic Concept"
else:
    print("i is not part of Dynamic Concept")

# Using "in" to Loop Through a String
for i in 'Dynamic Concept':
    print(i, end=" ")  # Output: "D y n a m i c   C o n c e p t " (each character of the string separated by a space)

print("\r")

# Using "is" to Check Object Identity

# Check if two empty dictionaries are identical (they aren't)
print({} is {})  # Output: False

# Check if two spaces are identical (they are, as spaces are immutable)
print(print('' == ''))  # Output: True

"""
The comments explain the purpose of each line in the code. 
It demonstrates the usage of "in" for conditional checks, looping through a string with "in," 
and checking object identity using "is."
"""