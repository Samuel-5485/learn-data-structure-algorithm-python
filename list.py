#List
b = [2, 4, "word", True]
print(b)

a = list((1, 4, 3.2, 'banana', 5))
print(a)
b = list('STC')
print(b)
# Creating list with repeated elements
# we can use * for repeated items
a = [3] * 3
print(a)

# Accessing list elements
# elements in a list are accessed using indexing.
#  Python indexes start at 0
a = [12,13,15,18]
print(a[0])
print(a[1])
print(a[2])
print(a[1:-1])

# Adding elements into list
"""we can add elements to a list using the following methods:
append(): add at the end of the list
extend(): adds multiple elements to the end of the list
insert(): adds at a specific position
clear(): removes all items"""
x = []
x.append(15)
x.append(2)
x.append(3)
print("After append:", x)

x.insert(0, 1)
print("After insert", x)

x.extend([4, "list", True])
print("After extend", x)

x.clear()
print("After clear:", x)

# Updating elements into list
"""since list are mutable, we can update elements by accessing them via their index"""
a = [2, 4, 5, 6]
a[0] = 3
print("After update", a)

# Removing elements from list
"""We can remove elements from a list using:
   remove():removes the first occurrence of an element
   pop():removes the element at a specific index or the last elements if no index is specified
   del statement:deletes an element at a specified index"""
a.remove(4)
print("After removed:", a)

popped_val = a.pop(1) #by index if not the end value will remove
print("Popped element", popped_val)
print("After pop", a)

del a[0]
print("After del:", a)

# Iterating over list
# we can iterate over lists using loops, 
a = ['apple', 'banana', 'cherry']
for item in a:
    print(item)


# Nested list
"""A nested list is a list within  another list, which is useful for representing
    matrices or tables. we can access nested elements by chaining indexes"""
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[1][2])
print(matrix[2][1])
print(matrix[0][0])
print(matrix[2][2])

#List comprehension
""" is a concise and powerful way to create new lists by
applying an expression to each item in an existing iterable(like a list, tuple, or range).range
it helps you write clean, readable and efficient code compared to traditional loops"""
#suppose you want to square every num in a list
a = [1, 2, 4, 5]
res = [val ** 2 for val in a]
print(res)

#Explanation:res = [val ** 2 for val in a] use list comprehension to create a new list by squaring each number in a.
"""Syntax [expression for item in iterable if condition] 

Parameters:
    expression: operation or value to include in the new list.
    item: current element from the iterable.
    iterable: sequence like a list, tuple or range.
    if condition (optional): filter to include only items that satisfy the condition.
"""

#Why use list comprehension?
""" 
    cleaner code:Combines looping, filterng and transformation in one line 
    more readable:avoids verbose loops and temporary variables
    faster execution:often faster than equivalent for-loops"""
a = [1, 3, 5, 2]
res = []
for val in a:
    res.append(val * 2)
print(res)

#Conditional statements in list comprehension
a = [2, 3, 4, 5]
res = [val for val in a if val%2==0] #selects only even num
print(res)

#Examples of list comprehension
#1. Creating a list from a range
a = [i for i in range(4)]
print(a)
#2.using nested loops
c = [(x, y, z) for x in range(5) for y in range(3) for z in range(2)]
print(c)
#3.flattening a list of lists
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [val for row in mat for val in row]
print(res)
""" Explanation:

mat is a list of lists (a 3x3 matrix).
[val for row in mat for val in row] goes through each sublist (row) and then each value (val) inside it.
It collects all values into a single flat list"""


#Python list comprehension using if-else
a = [1, 4, 3, 2]
#Add Even for even numbers otherwise Odd
result = ['Even' if n % 2==0  else 'Odd' for n in a]
print(result)

res = [n for n in a if n%2==0]
print(res)

#Nested if-else in list comprehension
a = [3, 4, 5, 6]
# Categorize numbers based on divisibility
result = ["Divisible by 2" if n % 2 == 0 else "Divisible by 3" if n % 3 == 0 else "Other" for n in a]
print(result)

