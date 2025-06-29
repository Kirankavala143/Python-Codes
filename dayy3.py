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
def palindrome(s):
    return s==s[::-1]
s=input("enter a string:")
if palindrome(s):
    print("palindrome")
else:
    print("Not Palindrome")

# Calculate factorial using recursion.
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
    
# n=int(input("enter a number: "))
# print(fact(n))  # Output: Factorial of n

# # Find the nth Fibonacci number using recursion.
# def fibonacci(n):
#     a,b=0,1
#     for _ in range(n):
#         a, b = b, a + b
#     return a
# # Example usage
# n = int(input("Enter the position of Fibonacci number: "))
# print(f"The {n}th Fibonacci number is: {fibonacci(n)}")  # Output: Fibonacci number at position n
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# n = int(input("Enter the position of Fibonacci number: "))
# print(f"The {n}th Fibonacci number is: {fibonacci(n)}")  #  

# Reverse a string using recursion.
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])
s = input("Enter a string to reverse: ")
print(f"Reversed string: {reverse_string(s)}")  # Output: Reversed

# string of s
# s = input("Enter a string to reverse: ")
# print(f"Reversed string: {reverse_string(s)}")
