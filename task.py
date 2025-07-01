# # find min and max in a list 
# l=[4,7,9,2,1,4,5,6]
# smallest = largest = l[0]
# for i in l:
#     if i < smallest:
#         smallest = i
#     elif i > largest:
#         largest = i
# print(smallest)
# print(largest)

# s=l.sort()
# smallest = l[0]
# largest = l[-1]
# print(smallest)
# print(largest)


#User function Template for python3
# Take a, b and c input and print the greatest of three
# a,b,c=map(int,input().split())
# if a>=b and a>=c:
#     print(a)
# elif b>=a and b>=c:
#     print(b)
# else:
#     print(c)

#User function Template for python3
# Take year input and print if year is a leap year
# year=int(input())
# if (year%4==0) and (year!=100) or (year%400==0):
#     print("True")
# else:
#     print("False")



# num = int(input("Enter a number: "))
# i=1
# while i<=10:
#     print(num,"*",i,"=",num*i)
#     i+=1
    

def first(s):
    char_count={}

    for i in s:
        if i in char_count:
            char_count[i] +=1
        else:
            char_count[i] =1
    
    for i in s:
        if char_count[i]==1:
            return i
    return None

# Example usage
s = "aabbcdeff"
result = first(s)
if result:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found")

# prime number up to 50
# n = int(input("Enter a number: "))
# for num in range(2, 51):  # Start from 2 (smallest prime)
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):  # Only check till square root of num
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=" ")

# def prime():
#     primes = []
#     for num in range(2, 51):
#         is_prime = True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(num, end=" ")
#             primes.append(num)
#     return primes

# # Call the function
# prime_numbers = prime()
# print("\nList of primes returned:", prime_numbers)



def find(n):
    if n<=1:
        print("Enter the number greater than 1")
    else:
        for i in range(2, n):
            if n % i == 0:
                print(n, "is not a prime number")
                break
        else:
            print(n, "is a prime number")   

    return n

n=int(input())
print("Enter a number to check if it is prime:",find(n))


# 1 write a program to print the sum of the cubes of the numbers from M to N

def sum_of_cubes(m,n):
    sum=0
    for i in range(m,n+1):
        sum+=i**3
    return sum

m=int(input())
n=int(input())
print(sum_of_cubes(m,n))    