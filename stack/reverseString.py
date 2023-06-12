"""
reverse a given string using stack
"""

import stack

string = "anurA htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()

# Your solution here.
for char in string:
    s.push(char)

while not s.is_empty():
    reversed_string += s.pop()

print(reversed_string)
