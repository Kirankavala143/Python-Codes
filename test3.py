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
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverse_number(n // 10, rev * 10 + n % 10)

# Example usage
n = int(input("Enter a number: "))
print("Reversed number:", reverse_number(n))

# reverse a integer using recursion strings
def reverse_string(n):
    if len(n) == 0:
        return n
    else:
        return n[-1] + reverse_string(n[:-1])

# Example usage
n= input("Enter a string: ")
n=str(n)  # Ensure n is a string
s = reverse_string(n)
print("Reversed string:", reverse_string(n))


