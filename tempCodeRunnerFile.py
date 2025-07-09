a = [1, 2, 3]
b = a # c = a[:]
c = a[:]
print(a is b) # Output: True
print(a is c) # Output: False 
print(a == c) # Output: True  