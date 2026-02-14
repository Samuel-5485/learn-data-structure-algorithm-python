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