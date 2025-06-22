# # FUNCTIONS
# def day(d,m,y):
#     print(d,m,y,sep="-")

# print("hi")

# day("21","06","2025")
# print("this is the today")

# def day(d,m,y):
#     return d +"-"+m+"-"+y

# print("hi")

# d=day("21","06","2025")
# print(d)
# print("this is the today")

def name(first, last):
    return first + " " + last

print(name("John", "Doe"))  # Output: John Doe

def add(a, b):
    sum=a+b
    mul=a*b
    return sum,mul
s,m=add(5,6)
print("Sum:", s)  # Output: Sum: 11
print("Product:", m)  # Output: Product: 30


def getfirstdigit(x):
    while x>=10:
        x=x//10
    return x

x=int(input("Enter a number: "))
print("First digit:", getfirstdigit(x))  # Output: First digit: 1 (for example, if input is 1234)
