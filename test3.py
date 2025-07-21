# # sum of numbers in a input
# n = int(input("Enter the number of elements: "))
# count=0
# word=str(n)
# for i in word:
#     count+=int(i)
# print("Sum of numbers is:", count)

# using sum function
# print("Sum of numbers is:", sum(map(int, input("Enter numbers separated by space: ").split())))


# sum of digits using recursion
# def sum_of_digits(n):
#     if n == 0:
#         return 0
#     else:
#         return (n % 10) + sum_of_digits(n // 10)

# # Example usage
# num = int(input("Enter a number: "))
# print("Sum of digits:", sum_of_digits(num))

# a to the power b
# def power(a, b):
#     if b == 0:
#         return 1
#     else:
#         return a **b

# #  Example usage
# base = int(input("Enter the base: "))
# exponent = int(input("Enter the exponent: "))
# print(f"{base} raised to the power of {exponent} is: {power(base, exponent)}")


# Recursive power function: power(a, b) = a^b

# def power(a, b):
#     if b == 0:
#         return 1
#     else:
#         return a * power(a, b - 1)
# a = int(input("Enter the base: "))
# b = int(input("Enter the exponent: "))
# print("Result:", power(a, b))

# anothwer way to find power
# def power(a, b):
#     return a ** b 
# # Example usage
# base = int(input("Enter the base: "))
# exponent = int(input("Enter the exponent: ")) 
# print(f"{base} raised to the power of {exponent} is: {power(base, exponent)}")

# reverse a integer
# n=123
# a=str(n)
# rev=a[::-1]
# print(rev)

# recursive reverse of a number
# def reverse_number(n, rev=0):
#     if n == 0:
#         return rev
#     else:
#         return reverse_number(n // 10, rev * 10 + n % 10)

# # Example usage
# n = int(input("Enter a number: "))
# print("Reversed number:", reverse_number(n))

# reverse a integer using recursion strings
# def reverse_string(n):
#     if len(n) == 0:
#         return n
#     else:
#         return n[-1] + reverse_string(n[:-1])

# # Example usage
# n= input("Enter a string: ")
# n=str(n)  # Ensure n is a string
# print("Reversed string:", reverse_string(n))

# find first repeated character in a string and its second occurrence
# def first_repeated_char(s):
#     seen = {}
#     for index, char in enumerate(s):
#         if char in seen:
#             print(f"First repeated character: '{char}'")
#             print(f"Second occurrence at index: {index}")
#             return
#         else:
#             seen[char] = index
#     print("No repeated characters found.")

# # Example usage:
# s = "abcaadb"
# first_repeated_char(s)

# def first_repeated_char(s):
#     seen = set()  # Step 1
#     for i in range(len(s)):  # Step 2
#         if s[i] in seen:  # Step 3
#             print("First repeated character:", s[i])  # Step 4
#             print("Second occurrence at index:", i)  # Step 5
#             return  # Step 6
#         seen.add(s[i])  # Step 7
#     print("No repeated characters found.")  # Step 8

# s = "abcaadb"
# first_repeated_char(s)

# fibnacci series
# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b   

# n = int(input("Enter the number of terms: "))
# for num in fibonacci(n):
#     print(num, end=" ")   

def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Example usage:
n= int(input("Enter the number of terms: "))
fibonacci_series(n)

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Print first n Fibonacci numbers
n = 10
for i in range(n):
    print(fibonacci_recursive(i), end=' ')

#Lambda function
'''syntax:-
lambda arguments:expression '''
#Ex:-
add = lambda a,b : a+b
print(add(9,3)) # 12
'''No arguments'''
greet = lambda:"HELLO!"
print(greet()) # HELLO!

'''lambda in a map() function'''
n = [1,2,3,4]
sq = list(map(lambda x : x**2, n))
print(*sq) # 1 4 9 16
'''Convert to uppercase'''
names = ['anu','vijju','gowthami']
up = list(map(str.upper,names))
print(up) #['ANU', 'VIJJU', 'GOWTHAMI']