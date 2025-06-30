# # FUNCTIONS
# # Write a function to check if a number is even or odd.
# def even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# # Example usage
# s=int(input("enter a number: "))
# print(even_odd(s))  # Output: Even

# # Create a function that finds the maximum of three numbers.
# def max(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
# # Example usage
# a=int(input("enter a number: "))
# b=int(input("enter a number: "))
# c=int(input("enter a number: "))
# print(max(a,b,c))

# Write a function to check if a string is a palindrome.
# def palindrome(s):
#     return s==s[::-1]
# s=input("enter a string:")
# if palindrome(s):
#     print("palindrome")
# else:
#     print("Not Palindrome")

# # Calculate factorial using recursion.
# # def fact(n):
# #     if n==0 or n==1:
# #         return 1
# #     else:
# #         return n*fact(n-1)
    
# # n=int(input("enter a number: "))
# # print(fact(n))  # Output: Factorial of n

# # # Find the nth Fibonacci number using recursion.
# # def fibonacci(n):
# #     a,b=0,1
# #     for _ in range(n):
# #         a, b = b, a + b
# #     return a
# # # Example usage
# # n = int(input("Enter the position of Fibonacci number: "))
# # print(f"The {n}th Fibonacci number is: {fibonacci(n)}")  # Output: Fibonacci number at position n
# # def fibonacci(n):
# #     if n <= 0:
# #         return 0
# #     elif n == 1:
# #         return 1
# #     else:
# #         return fibonacci(n-1) + fibonacci(n-2)
# # n = int(input("Enter the position of Fibonacci number: "))
# # print(f"The {n}th Fibonacci number is: {fibonacci(n)}")  #  

# # Reverse a string using recursion.
# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     else:
#         return s[-1] + reverse_string(s[:-1])
# s = input("Enter a string to reverse: ")
# print(f"Reversed string: {reverse_string(s)}")  # Output: Reversed

# # string of s
# # s = input("Enter a string to reverse: ")
# # print(f"Reversed string: {reverse_string(s)}")


# # LISTS
# # Create a function to find the sum of all elements in a list.
# def sum_of_list(list):
#     count=0
#     for i in list:
#         count+=i
#     return count

# list=list(map(int, input("Enter numbers separated by space: ").split()))
# print(f"Sum of the list: {sum_of_list(list)}")  # Output: Sum of all elements in the list


# Add an element to a list and remove an existing one.

# def add_remove_element(lst, add_element, remove_element):
#     lst.append(add_element)  # Add new element
#     if remove_element in lst:
#         lst.remove(remove_element)  # Remove existing element
#     return lst
# # Example usage 
# # lst = list(map(int, input("Enter numbers separated by space: ").split()))
# lst=[1,2,3,4,5]
# add_element = int(input("Enter an element to add: "))
# remove_element = int(input("Enter an element to remove: "))
# print(add_remove_element(lst,add_element,remove_element))



# Count the frequency of each element in a list.
def hello(l):
    s={}
    for i in l:
        if i in s:
            s[i]+=1
        else:
            s[i]=1
    return s

l=[2,3,4,2,3,1,3,2,4]
print(hello(l))


# Add an element to a list and remove an existing one.
l=[7,8,9,5,3,2]
l.append(4)
l.remove(3)
print(l)

# Sort a list in ascending and descending order.
s=[1,2,3,4,5]
s.sort()
print(s)
s.sort(reverse=True)
print(s)

# Create a tuple and access its elements.
t=(1,2,3,4,5)
print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])

# Unpack a tuple into variables.
a,b,c,d,e=t
print(a)
print(b)
print(c)
print(d)
print(e)

# Convert a list to a tuple and vice versa.
l=[1,2,3,4,5]
t=tuple(l)
print(t)
l=list(t)
print(l)

# Create a list of tuples and sort it based on the second element.
l=[(1,2),(3,4),(5,6)]
l.sort(key=lambda x: x[1])
print(l)

# Write a function that takes a tuple and returns a reversed tuple.
def reverse_tuple(t):
    return tuple(reversed(t))
t=(1,2,3,4,5)
print(reverse_tuple(t))

