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

# def LargeSmallSum(arr):
#     if len(arr) <= 3:
#         return 0
#     even_nums = []
#     odd_nums = []
#     for i in range(len(arr)):
#         if i % 2 == 0:
#             even_nums.append(arr[i])
#         else:
#             odd_nums.append(arr[i])
#     if len(even_nums) < 2 or len(odd_nums) < 2:
#         return 0
#     even_nums.sort(reverse=True)
#     odd_nums.sort()
#     return even_nums[1] + odd_nums[1]

# n = int(input())
# arr = list(map(int, input().split()))
# print(LargeSmallSum(arr))

# # 5 Write a program to print the following pattern
# n = int(input("Enter the number of rows: "))
# for i in range(1, n + 1):        
#     for j in range(1, i + 1):
#         print(j, end=" ") 
#     print()

# def fizzbuzz(n):
#     for i in range(1, n + 1):
#         fizz = ["", "Fizz"][divmod(i, 3)[1] == 0]
#         buzz = ["", "Buzz"][divmod(i, 5)[1] == 0]
#         print((fizz + buzz) or i)

# # Example:
# fizzbuzz(15)


# def fizzbuzz(n):
#    result=[]
#    for i in range(n+1):
#        fizz=[" ", "Fizz"][divmod(i,3)[1] == 0]
#        buzz=[" ", "Buzz"][divmod(i,5)[1] == 0]
#        result.append(fizz+buzz or str(i))
#    return result

# n=int(input())
# print("\n".join(fizzbuzz(n)))


n = int(input())
while n>=10:
    sum=0
    while n>0:
        sum+=n%10
        n=n//10
    n=sum
print(n)

# while n >= 10:
#     sum = 0
#     while n > 0:
#         sum += n % 10
#         n //= 10
#     n = sum

# print(n)