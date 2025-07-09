# What’s the difference between is and == in Python?
# == is a comparison operator that checks whether two values are equal or not.
# is is an identity operator that checks whether two variables point to the same object or not.

# What happens when you use mutable types as default function arguments?
# Using mutable types (like lists or dictionaries) as default arguments can lead to unexpected behavior because the default value is shared across all calls to the function.
# If the mutable object is modified, the change will persist across future calls to the function.

# What’s the difference between float('nan') == float('nan') and math.isnan()?
# float('nan') == float('nan') returns False because NaN (Not a Number) is not equal to itself.
# math.isnan() returns True if the input value is NaN, allowing you to check for NaN values correctly.

# How can you force Python to treat an int literal as binary, octal, or hexadecimal?
# You can force Python to treat an int literal as binary, octal, or hexadecimal by using prefixes:
# 0b for binary, 0o for octal, and 0x for hexadecimal.      
# Example:
# num = 0b1010  # 10 in binary
# num = 0o123   # 83 in octal
# num = 0x123   # 291 in hexadecimal        

# Explain operator precedence and associativity with an example.
# Operator precedence determines the order in which operators are evaluated in an expression.
# Associativity determines whether an operator is evaluated from left to right or right to left.    

# What will a = b = 5 and a += 1 do? Will b change?
# a = b = 5 assigns the value 5 to both variables a and b.
# a += 1 increments the value of a by 1, effectively adding 1 to its current value.
# Therefore, the result will be a = 6, and b will still be 5.

# What is the difference between x and y and x & y?
# x and y are variables that can hold any value, while x & y is a bitwise AND operation that performs a logical AND on the binary representations of x and y.

# Why does 3 < 2 < 1 return False in Python?
# In Python, the expression 3 < 2 < 1 is evaluated as (3 < 2) and (2 < 1).
# The second comparison (2 < 1) returns False, so the overall expression returns False. 

# Write a nested loop to print Pascal’s Triangle.
def print_pascals_triangle(n):
    for i in range(n):
        # Print leading spaces
        print(' ' * (n - i), end='')
        
        # Calculate and print the values in the row
        value = 1
        for j in range(i + 1):
            print(value, end=' ')
            value = value * (i - j) // (j + 1)
        
        print()  # Move to the next line

# Example usage
n = 5
print_pascals_triangle(n)

# Find the longest palindromic substring using only loops and if/else.
def longest_palindromic_substring(s):
    max_length = 0
    longest_palindrome = ""
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1]:  # Check if the substring is a palindrome
                if len(substring) > max_length:
                    max_length = len(substring)
                    longest_palindrome = substring
                    
    return longest_palindrome

# Example usage
s = "racecarfdghgfedcbracecar"
print(longest_palindromic_substring(s))
