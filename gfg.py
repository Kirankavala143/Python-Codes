
# def process(text):
#     text = ''.join(e for e in text if e.isalnum() or e.isspace())
#     text = text.strip()
#     return text
# result = input("Enter a text:")   
# print(process(result)) 

# count digits
# n=int(input("Enter a number: "))
# count = 0
# while n>0:
#     n=n//10
#     count+=1
# print("Number of digits:", count)

# factorial of a number
# import math
# n = int(input("Enter a number: "))
# print(math.factorial(n))
# res=1
# for i in range(2,n+1):
#     res=res*i
# print("Factorial of", n, "is", res)

# find gcd of two numbers
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# small=min(a, b)
# for i in range(1,small+1):
#     if a%i==0 and b%i==0:
#         gcd=i
# print("GCD of", a, "and", b, "is", gcd)

# find lcm of two numbers
# lcm = (a * b) // gcd
# print("LCM of", a, "and", b, "is", lcm)

# Check if a number is prime
n = int(input("Enter a number: "))
if n<=1:
    print("Enter the number greater than 1")
else:
    for i in range(2,n):
        if n%i==0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")

# All divisors of a number
n = int(input("Enter a number: "))
for i in range(1,n):
    if n % i == 0:
        print(i)
    
# difference between two tables
n1 = int(input())
n2 = int(input())

for i in range(1,11):
    print(n1*i-n2*i,end=" ")

n = 4
for i in range(n):
    print("* " * n)


    



