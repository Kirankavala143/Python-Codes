
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
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
small=min(a, b)
for i in range(1,small+1):
    if a%i==0 and b%i==0:
        gcd=i
print("GCD of", a, "and", b, "is", gcd)

# find lcm of two numbers
lcm = (a * b) // gcd
print("LCM of", a, "and", b, "is", lcm)