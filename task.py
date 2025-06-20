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
year=int(input())
if (year%4==0) and (year!=100) or (year%400==0):
    print("True")
else:
    print("False")



num = int(input("Enter a number: "))
i=1
while i<=10:
    print(num,"*",i,"=",num*i)
    i+=1
    