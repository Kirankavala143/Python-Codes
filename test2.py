# neon number

# def is_neon_number(n):
#     square = n * n
#     digit_sum = sum(int(digit) for digit in str(square))
#     return digit_sum == n

# n = int(input("Enter a number: "))
# if is_neon_number(n):
#     print(f"{n} is a Neon number")
# else:
#     print(f"{n} is not a Neon number")

#spy number
# def is_spy_number(n):
#     digit_sum = 0
#     digit_product = 1
#     while n > 0:
#         digit = n % 10
#         digit_sum += digit
#         digit_product *= digit
#         n //= 10
#     return digit_sum == digit_product

# n = int(input("Enter a number: "))
# if is_spy_number(n):
#     print(f"{n} is a Spy number")
# else:
#     print(f"{n} is not a Spy number")

# automorphic number
# def is_automorphic_number(n):
#     square = n * n
#     return str(square).endswith(str(n))     

# n = int(input("Enter a number: "))
# if is_automorphic_number(n):    
#     print(f"{n} is an Automorphic number")
# else:           
#     print(f"{n} is not an Automorphic number")

# def is_palindrome(n):
#     original = n     
#     reverse = 0     
#     while n > 0:
#         remainder = n % 10     
#         reverse = reverse * 10 + remainder     
#         n //= 10     
#     return original == reverse        
# n = int(input("Enter a number: "))
# if is_palindrome(n):    
#     print(f"{n} is a Palindrome number")  
# else:
#     print(f"{n} is not a Palindrome number")

# perfect number
# def is_perfect_number(n):
#     if n < 1:
#         return False
#     divisors = []         
#     for i in range(1, n):
#         if n % i == 0:
#             divisors.append(i)             
#     return sum(divisors) == n

# n = int(input("Enter a number: "))
# if is_perfect_number(n):
#     print(f"{n} is a Perfect number")    
# else:
#     print(f"{n} is not a Perfect number")

# a=int(input("Enter a number: "))
# b=a//4
# c=a%4
# print("Quotient:", b)
# print("Remainder:", c)

# # lcm of 2 numbers
# def gcd(x, y):
#     while y:  
#         x, y = y, x % y
#     return x
# def lcm(x, y):
#     return x * y // gcd(x, y)
# x = int(input("Enter the first number: "))
# y = int(input("Enter the second number: "))
# print("The LCM of", x, "and", y, "is", lcm(x, y))

s="kiran kumar"
a=s.split()
print(" ".join(a[::-1]))

# find length of last word
a="hello world"
b=a.split()
print(b)
def length_of_last_word(s):
    words = s.split()
    if not words:
        return 0
    return len(words[-1])
print("Length of last word:", length_of_last_word(a))

# find length of last word without using split
def length_of_last_word_no_split(s):
    length = 0
    found_char = False
    for char in reversed(s):
        if char != ' ':
            found_char = True
            length += 1
        elif found_char:
            break
    return length        
print("Length of last word:", length_of_last_word_no_split(a))