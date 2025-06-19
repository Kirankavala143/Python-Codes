# Take a list of numbers and print all even numbers.
l=[1,32456,68,54,3,1,246,89,65]
for i in l:
    if i%2==0:
        print(i)

# Take a list and print the maximum and minimum.
l=[1,32456,68,54,3,1,246,89,65]
print(max(l))
print(min(l))

# Count how many times a number occurs in a list.
l=[1,32456,68,54,3,1,246,89,65,1]
print(l.count(1))

# Remove all duplicates from a list and print the unique list.
l=[7,2,3,77,28,17,2,7,3,3,4,30]
s=list(set(l))
print(s)
unique=list(dict.fromkeys(l))
print(unique)
unique=[]
for i in l:
    if i not in unique:
        unique.append(i)
print(unique)

# Reverse a list without using .reverse().
l=[1,2,3,4,5,6]
reversed_list=[]
l.reverse()  
print(l)
a=l[::-1]
print(a)
reversed=list(reversed(l))
print(reversed)

# Write a program to merge two sorted lists into one sorted list.
a=[1,4,56,67,4]
b=[24,564,35,77]
a.sort()
b.sort()
print(a+b)

# Find the second largest number in a list.
l=[2,43,54,3,24,65,7,90]
l.sort()
print(l[-2])
first=second=1
for i in l:
    if i>first:
        second=first
        first=i
    elif i>second and i !=first:
        second=i
print(second)

# Find all pairs in a list that sum to a given number.


# Rotate a list by k positions (left or right).