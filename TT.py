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


n=int(input("Enter a number: "))
n=str(abs(n))
sum=0
for i in n:
    sum+=int(i)
print(sum)

