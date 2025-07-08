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
def factorial(n):
    if n == 0:    
        return 1          
    else:        
        return n * factorial(n-1)
print(factorial(5))           

# while loop revsere a number
# n = int(input("Enter a number: "))
# rev = 0        
# while n > 0:            
#     rev = rev * 10 + n % 10            
#     n = n // 10            
# print(rev)

# for loop reverse a number
n = int(input("Enter a number: "))
rev = 0        
for i in str(n):            
    rev = rev * 10 + int(i)            
print(rev)            

# Reverse a number using recursion
def reverse_number(n):
    if n == 0:        
        return 0    
    else:        
        return n % 10 + reverse_number(n // 10)
print(reverse_number(123))        