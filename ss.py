def fact(num):
    if num == 0:
        return 1
    else:
        return num*fact(num-1)

print(fact(6))

num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("The factorial of", num, "is", factorial)


# .Write a program to print all numbers from 1 to 100 that are divisible by 5.
for i in range( 1,100):
    if i%5==0 :
        print(i)

# .Write a program that reverses a string entered by the user.
s="kiran"
print(s[::-1])
print(''.join (reversed(s)))
re=''
for i in s:
    re=i+re
print(re)

# .Write a program to check if a number is positive, negative, or zero.
num = int(input("enter a number:"))
if num >0:
    print("postive number")
elif num==0:
    print("zero")
else:
    print("negative number")

# Write a Python program that accepts a user's age and tells if they are eligible to vote (18+).
age=int(input("enter age:"))
if age>18:
    print("eligible to vote")
else:
    print("no vote")

# .Take two numbers as input and print the maximum.
a=int(input("enter a number:"))
b=int(input("enter a number:"))
print(max(a,b))

# Write a program to check whether a character is a vowel or consonant.
s=input(" enter a character:")
vowels="AEIOUaeiou"
if s in vowels:
    print("vowel")
else:
    print("constant")

# Write a program to determine whether a given year is a leap year.

year=int(input("enter the year:"))
if year%4==0:
    print("leap year")
else:
    print("not a leap year")

# Write a program to generate Fibonacci series up to n terms.
n=int(input("enter a number:"))
a,b=0,1
for i in range(0,n+1):
    print(a)
    a,b=b,a+b

# Write a program to check whether a number is an Armstrong number.
num=int(input("enter a number:"))
orginal_num=num
length=len(str(num))
sum_of_powers=0
while (num>0): #15
    digit=num%10 # %= remainder=3,5
    sum_of_powers+=digit**length 
    num=num//10
if sum_of_powers==orginal_num:  
    print("armstrong number")       
else:       
    print("not an armstrong number")

# .Write a program to check whether a number is prime.
num=int(input("enter a number:"))
for i in range(2,num+1):
    if num%i==0:
        print("not prime")
        break
    else:
        print("prime")
        break

# Write a Python function to check whether a string is a palindrome.
s="madam"
a=s[::-1]
if s==a:
    print("s")
else:
    print("n")

# Write a program to sort a list in ascending order without using sort().
l=[6,0,5,8,4,8]
l.sort()
print(l)

def ascend(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

my_list = [12, 4, 56, 1, 99, 23]
sorted_list = ascend(my_list)
print("Sorted list in ascending order:", sorted_list)

# Example list
numbers = [6, 3, 8, 1, 4]
sorted_list = []

while numbers:
    smallest = min(numbers)     # Find the smallest number
    sorted_list.append(smallest)  # Add it to the new sorted list
    numbers.remove(smallest)      # Remove it from the original list

print("Sorted list:",sorted_list)

i=0
while i<5:
    print("i=",i)
    i+=1

for i in range(3):
    for j in range(5):
        print("*",end="")
    print()
n=5
for i in range(1,n+1):
    print("*"*i)

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print()

n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

# number guessing game
import random
a=random.randint(1,10)
while True:
    user=int(input("enter a number:"))
    if user==a:
        print("correct guess")
        break
    elif user<a:
        print("small number,guess a larger number")
    else:
        print("larger number,guess a smaller number")

fruits = ["apple", "banana", "mango"]
for i in fruits:
    print(i)
# OR using index
for i in range(len(fruits)):
    print(fruits[i])

