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
n=int(input("Enter a number:"))
s=abs(n)
sum=0
for i in range(s):
    s=s//10
    sum+=i
print(sum)


