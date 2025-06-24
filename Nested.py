# # num=int(input())
# # for i in range(1,num+1,1):
# #     print(i,end=" ")
# # print()
# for i in range(1,11):
#     for j in range(i,i*10+1,i):
#         print(j,end=" ")
#     print()

# for i in range(1,3):
#     j=1
#     while j<3:
#         print(i,j)
#         j+=1
#     print("kiran")

# ll=[[20,30,40],[50,60,70],[80,90,100]]
# for l in ll:
#     for i in l:
#         print(i, end=" ")
#     print()  # Print a new line after each inner list

# # Print a square pattern of stars
# n=int(input("Enter the size of the square: "))
# for i in range(n):
#     for j in range(n):
#         print("*", end="")
#     print()  # Print a new line after each row

# # Print a right-angled triangle pattern of stars
# n=int(input("Enter the size of the triangle: "))
# for i in range(n):
#     for j in range(i+1):
#     # for j in range(n-i): reversed triangle
#         print("*", end="")
#     print()  # Print a new line after each row

# # print a pyramid pattern of stars
# n=int(input("Enter the size of the pyramid: "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end="")
#     for k in range(2*i+1):
#         print("*", end="")
#     print()  # Print a new line after each row


n=123

while n>=10:
    # n=n%10  # This will give the last digit
    n=n//10
print(n)  # This will print the first digit of the number

s="hello"
print(s[2::])

for i in range(1,5):
    for j in range(1,10):
        print(i+j)