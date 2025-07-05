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

a=int(input("Enter a number: "))
b=a//4
c=a%4
print("Quotient:", b)
print("Remainder:", c)

