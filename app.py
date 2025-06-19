a=input("enter your name:")
b=input("enter your age:")
print(f"hello {a} ,you are {b} years old")

a=int(input("enter a number:"))
b=int(input("enter a number:"))
print("addtion:",a+b)
print("subtraction:",a-b)
print("product",a*b)
print(f"add:{a+b},sub:{a-b},product:{a*b}")

#  list print even numbers
l=[5,4,8,5,99,65,356,658,32,5,7,87,56]
for i in l:
    if i%2==0:
        print(i)
s=[i for i in l if i%2==0]
print(s)

# reverse a string
s=input("enter a string:")
print(s[::-1])

print(''.join(reversed(s)))

re=''
for char in s:
    re=char+re
print(re)

# count vowels in a string
s="this is kiran"
vowels="aeiouAEIOU"
count=0
constant=0
for i in s:
    if i.isalpha():
        if i in vowels:
            count+=1
        else:
            constant+=1
    
print("number of vowels in a sentence",count)
print("number of constant in a sentence ",constant)

# no of letters in a string
a="kiran is"
count=0
for i in a:
    if i.isalpha():
        count+=1
print(count)

count=[i for i in a if i.isalpha()]
print(len(count))

# list-largest,smallest

numbers=[23,25,58,34]
numbers.sort()
smallest=numbers[0]
largest=numbers[-1]

largest= max(numbers)    
smallest=min(numbers)
print(largest)
print(smallest)

a=5
b=6
a,b=b,a
print(a,b)

a=a+b #11
b=a-b #5
a=a-b#
print(a,b)

a=a^b
b=a^b
a=a^b
print(a,b)

s="kirankumar"
count={}
for i in s:
    if i.isalpha():
        if i in count:
            count[i]+=1
        else:
            count[i]=1
print(count)


a="jkuftryuiliokmvbdew4esfgfvnm,hmncfdfbju"
count={}
for i in a:
    if i.isalpha():
        if i in count:
            count[i]+=1
        else:
            count[i]=1
print(count)