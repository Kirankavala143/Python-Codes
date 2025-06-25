
# # def process(text):
# #     text = ''.join(e for e in text if e.isalnum() or e.isspace())
# #     text = text.strip()
# #     return text
# # result = input("Enter a text:")   
# # print(process(result)) 

# # count digits
# # n=int(input("Enter a number: "))
# # count = 0
# # while n>0:
# #     n=n//10
# #     count+=1
# # print("Number of digits:", count)

# # factorial of a number
# # import math
# # n = int(input("Enter a number: "))
# # print(math.factorial(n))
# # res=1
# # for i in range(2,n+1):
# #     res=res*i
# # print("Factorial of", n, "is", res)

# # find gcd of two numbers
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# small=min(a, b)
# for i in range(1,small+1):
#     if a%i==0 and b%i==0:
#         gcd=i
# print("GCD of", a, "and", b, "is", gcd)

# # find lcm of two numbers
# lcm = (a * b) // gcd
# print("LCM of", a, "and", b, "is", lcm)

# # Check if a number is prime
# n = int(input("Enter a number: "))
# if n<=1:
#     print("Enter the number greater than 1")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print(n, "is not a prime number")
#             break
#     else:
#         print(n, "is a prime number")

# # All divisors of a number
# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     if n % i == 0:
#         print(i)
    
# # difference between two tables
# n1 = int(input())
# n2 = int(input())

# for i in range(1,11):
#     print(n1*i-n2*i,end=" ")

# n = 4
# for i in range(n):
#     print("* " * n)


s= "welcome to the world of geeks"
def reverse_words(s):
    words = s.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words
result = reverse_words(s)
print(result)

    
# capitalize the words in a string
def capitalize_words(s):
    words = s.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
s = "hello world"
result = capitalize_words(s)
print(result)


a="welcome to the world of geeks"
words=a.split()
capitalize_words=[]
for i in words:
    capitalize_words.append(i.capitalize())
    
capitalized_sentence = ' '.join(capitalize_words)
word_count = len(words)
print(capitalized_sentence)
print(word_count)

# elements smaller than the x
def smaller_element(l, x):
    res=[]
    for i in l:
        if i< x:
            res.append(i)
    return res

l = [1, 2, 3, 4, 5]
x = 3
print(smaller_element(l, x))  # Output: [4, 5]

def sum(l,x):
    return[i for i in l if i<x]
print(sum(l, x))  # Output: [1, 2]

def num(l):
    even=[i for i in l if i%2==0]
    odd=[i for i in l if i%2!=0]
    return even, odd
l = [1, 2, 3, 4, 5, 6]
even, odd = num(l)
print("Even numbers:", even)  # Output: [2, 4, 6
print("Odd numbers:", odd)    # Output: [1, 3, 5]

def average(l):
    sum=0
    for i in l:
        sum+=i
    return sum/len(l)
l = [1, 2, 3, 4, 5]
print("Average:", average(l))  # Output: 3.0

def distinct(l):
    res=1
    for i in range(1,len(l)):
        if l[i] not in l[0:i]:
            res=res+1
    return res  
    # return len(set(l)) 

l = [1, 2, 3, 4, 5, 1, 2]
print("Distinct elements count:", distinct(l))  # Output: 5


# smallest postive mising number
def smallest_missing_positive(arr):
    s = set(arr)  # Convert list to set for O(1) lookups
    num = 1       # Start checking from 1
    while True:
        if num not in s:
            return num  # Found the missing number!
        num += 1        # Check next number
print(smallest_missing_positive([3, 4, -1, 1]))  # Output: 2
print(smallest_missing_positive([1, 2, 0]))      # Output:3


def small(arr):
    s=set(arr)
    num=1
    while True:
        if num not in s:
            return num
        num+=1
arr = [5, 4, -1, 1]
print(small(arr))  # Output: 2


# Frequency count
s="kirankumar"
count={}
for i in s:
    if i.isalpha():
        if i in count:
            count[i]+=1
        else:
            count[i]=1
print(count)


def frequency_count(s):
    count={}
    for i in s:
        if i.isalpha():
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
    return count
s = "hello world"
result = frequency_count(s)
print(result)
