# Digit Counter
# n=int(input("Enter a number: "))
# a=abs(n)
# s=str(a)
# print(len(s))

# a=int(input("Enter a number: "))
# s=abs(a)
# count=0
# while s>0:
#     s=s//10
#     count+=1
# print(count)

# sum of digits
# n=int(input("Enter a number:"))
# total = 0
# while n > 0:
#     total += n % 10  # Add the last digit to the total
#     n //= 10  # Remove the last digit
# print(total)


# n=int(input("Enter a number: "))
# n=str(abs(n))
# sum=0
# for i in n:
#     sum+=int(i)
# print(sum)

# Factorial of a number
# def factorial(n):
#     if n == 0:    
#         return 1          
#     else:        
#         return n * factorial(n-1)
# print(factorial(5))           

# while loop revsere a number
# n = int(input("Enter a number: "))
# rev = 0        
# while n > 0:            
#     rev = rev * 10 + n % 10            
#     n = n // 10            
# print(rev)

# for loop reverse a number
# n = int(input("Enter a number: "))
# rev = 0        
# for i in str(n):            
#     rev = rev * 10 + int(i)            
# print(rev)            

# # Reverse a number using recursion
# def reverse_number(n):
#     if n == 0:        
#         return 0    
#     else:        
#         return n % 10 + reverse_number(n // 10)
# print(reverse_number(123))        

# Reverse a string using recursion
# def reverse_string(s):  
#     if len(s) == 0:        
#         return s    
#     else:        
#         return s[-1] + reverse_string(s[:-1])
# print(reverse_string("hello"))


#  Given a string representing a mathematical expression (e.g., "3 + 5 * 2 - 8 / 4"), evaluate the result without using eval().
# def evaluate_expression(expression):
#     tokens = expression.split()
#     total=0
#     current_number = 0
#     operation = '+'

#     for i in tokens:
#         if i.isdigit():
#             current_number = int(i)
#         else:
#             if operation == '+':
#                 total += current_number
#             elif operation == '-':
#                 total -= current_number
#             elif operation == '*':
#                 total *= current_number
#             elif operation == '/':
#                 total /= current_number
            
#             operation = i
# # Apply the last number
#     if operation == '+':
#         total += current_number 
#     elif operation == '-':
#         total -= current_number 
#     elif operation == '*':
#         total *= current_number 
#     elif operation == '/':
#         total /= current_number

#     return total    

# expression = "3 + 5 * 2 - 8 / 4"        
# result = evaluate_expression(expression)
# print("Result:", result)    




# Swap two variables without using a third variable
# a = 5
# b = 10
# a = a + b
# b = a - b   
# a = a - b
# print("After swapping: a =", a, ", b =", b)
# Swap two variables using bitwise XOR
# a = 5
# b = 10
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print("After swapping: a =", a, ", b =", b)

# Swap two variables without using arithmetic or bitwise operations or tuple unpacking
# a = 5
# b = 10
# a, b = b, a
# print("After swapping: a =", a, ", b =", b)
# # Swap two variables using a temporary variable
# a = 5
# b = 10
# temp = a
# a = b
# b = temp
# print("After swapping: a =", a, ", b =", b)

# Q: Print all the prime numbers between 2 and N 

# n=int(input("Enter a number: "))
# if n<2:
#     print("There are no prime numbers less than 2.")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print("n0t a prime number")
#             break
#     else:
#         print("prime number")

# Q: Print all the prime numbers between 2 and N

# def print_primes(N):
#     for num in range(2, N + 1):
#         is_prime = True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(num)

# N = int(input("Enter a number: "))
# print_primes(N)

# Q: Print all the prime numbers between 2 and N using list comprehension
# def print_primes_comprehension(N):
#     primes = [num for num in range(2, N + 1) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))]
#     for prime in primes:
#         print(prime)
# N = int(input("Enter a number: "))
# print_primes_comprehension(N)


#  Print all the prime numbers between 2 and N, but stop printing when a number is divisible by the sum of its digits.
# n=int(input("Enter a number: "))
# def sum_of_digits(num):
#     return sum(int(digit) for digit in str(num))
# for i in range(2,n+1):
#     if i%sum_of_digits(i)==0:
#         break
#     else:
#         print(i)    


# nums = list(map(int, input().split()))
# multiples_of_3 = list(filter(lambda x: x % 3 == 0, nums))

# if multiples_of_3:
#     print(*multiples_of_3)
# else:
#     print("No multiples of 3 found")



# # Q: Print a hollow diamond pattern of stars for a given odd number of rows.
# def print_hollow_diamond(n):
#     if n % 2 == 0:
#         print("Please enter an odd number.")
#         return

#     # Upper part
#     for i in range(n // 2 + 1):
#         for j in range(n // 2 - i):
#             print(" ", end="")
#         print("*", end="")
#         if i > 0:
#             for j in range(2 * i - 1):
#                 print(" ", end="")
#             print("*")
#         else:
#             print()

#     # Lower part
#     for i in range(n // 2 - 1, -1, -1):
#         for j in range(n // 2 - i):
#             print(" ", end="")
#         print("*", end="")
#         if i > 0:
#             for j in range(2 * i - 1):
#                 print(" ", end="")
#             print("*")
#         else:
#             print()
# n = int(input("Enter an odd number of rows: "))
# print_hollow_diamond(n)


# Write a recursive function to convert a decimal number into its binary representation without using built-in functions.
# def decimal_to_binary(n):
#     if n == 0:
#         return ""
#     else:
#         return decimal_to_binary(n // 2) + str(n % 2)    
# n = int(input("Enter a decimal number: "))
# print("Binary representation:", decimal_to_binary(n))   

# using built in functions to covert decimal to binary
# n = int(input("Enter a decimal number: "))
# print("Binary representation:", bin(n)[2:])
# # to convert binary to decimal
# n= input("Enter a binary number: ")
# print("Decimal representation:", int(n, 2))

# n=5
# print(bin(n)[2:])  # Output: 101
# print(oct(n)[2:])  # Output: 0o5
# print(hex(n)[2:])  # Output: 0x5

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print("Fibonacci series:")
n = int(input("Enter the number of terms: "))
for i in range(n):
    print(fibonacci(i), end=" ")

# def fibonacci_iter(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b
# n = int(input("Enter the number of terms: "))
# fibonacci_iter(n)

# sum of fibonacci_iter
def fibonacci_sum(n):
    a, b = 0, 1
    sum = 0
    for _ in range(n):
        sum += a
        a, b = b, a + b
    return sum
n = int(input("Enter the number of terms: "))
print("Sum of Fibonacci series:", fibonacci_sum(n))

# range from this number to this number
# def fibonacci_range(start, end):
#     a, b = 0, 1
#     while a <= end:
#         if a >= start:
#             print(a, end=' ')
#         a, b = b, a + b 
# n1 = int(input("Enter the start of the range: "))
# n2 = int(input("Enter the end of the range: "))
# fibonacci_range(n1, n2)

s= "hello world"
squares = [x**2 for x in range(10)]
word_count = {char: s.count(char) for char in set(s)}
print("Squares:", squares)
print("Word count:", word_count)

s="hello world"
word_count={char: s.count(char) for char in set(s)}
print("Word count:", word_count)