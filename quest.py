# Take a string input and print it in reverse without using slicing

a="hello"
print(''.join(reversed(a)))

rev=""
for i in a:
    rev=i+rev
print(rev)

# Write a program to merge two sorted lists into one sorted list.
l=[1,2,3,4]
m=[5,6,7,8]
m=l+m
print(m)

# Count how many times each character appears in a string.
s="kirankumar"
character=input("enter a character:")
count=0
for i in s:
    if i in character:
        count+=1
print(count)
s="kirankumar"
count=0
for i in s:
    if i.isalpha():
        count+=1
print(count)

count=[i for i in s if i.isalpha()]
print(len(count))


# Print all numbers between 1 and 50 that are divisible by both 3 and 5
for i in range(1,50):
    if i%3==0 and i%5==0:
        print(i)
    else:
        print("no")

# Take a list of numbers and remove all duplicates, then print the unique list.
l=[2,3,5,3,46,3,3,4,3,4,34,3]
a=list(set(l))
print(a)
b=list(dict.fromkeys(l))
print(b)
unique=[]
for i in l:
    if i not in unique:
        unique.append(i)
print(unique)

# Check if a given string is a palindrome without using string slicing.
a="madam"
if a ==''.join(reversed(a)):
    print("palindrome")
else:
    print("not a palindrome")


# 1
# 12
# 123
# 1234
# 12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()


# Even Numbers in a List
l=[23,2354,4,64,43,2,3,46,7,8,96,5,3,2]
for i in l:
    if i%2==0:
        print(i)

# Count how many times a specific number occurs in a list
l=[2,2,3,45,4,3,3,3,5,6]
specific=int(input("enter a number:"))
count=0
for i in l:
    if i==specific:
        count+=1
print(count)

# Reverse a List Without Using .reverse() or [::-1]
# Input: [10, 20, 30, 40] → Output: [40, 30, 20, 10]
l = [10, 20, 30, 40]
reversed_list = []
for i in l:
    reversed_list.insert(0, i)  # Insert each element at the beginning
print(reversed_list)


# Find the Largest Number in a List
# Input: [10, 20, 30, 40] → Output: 40
l = [10, 20, 30, 40]
largest = l[0] # Initialize to negative infinity
for i in l:
    if i > largest:
        largest = i
print(largest)  # Output: 40

# s = [100,2000,3,10, 20, 30, 40]
smallest = s[0] # Initialize to positive infinity
for i in s:
    if i < smallest:
        smallest = i
print(smallest)  
        
# Find the Second Largest Number in a List
# Input: [1, 2, 3, 4, 5] → Output: 4

m = [1, 2, 3, 4, 5]
first = second = m[0]  # Initialize to negative infinity
for i in m:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i
print(second)  # Output: 4  


# Second Largest Number in a List
# Find the second largest number from a list of integers.
l=[1,2,6,9,8,3,4,5,9] 
l.sort()
print(l[-2])  # Output: 8  
first=second=l[0]
for i in l:
    if i>first:
        first=i
    elif i >second and i!=first:
        second=i
print(second)
