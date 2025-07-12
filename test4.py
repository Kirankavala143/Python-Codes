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

def LargeSmallSum(arr):
    if len(arr) <= 3:
        return 0
    even_nums = []
    odd_nums = []
    for i in range(len(arr)):
        if i % 2 == 0:
            even_nums.append(arr[i])
        else:
            odd_nums.append(arr[i])
    if len(even_nums) < 2 or len(odd_nums) < 2:
        return 0
    even_nums.sort(reverse=True)
    odd_nums.sort()
    return even_nums[1] + odd_nums[1]

n = int(input())
arr = list(map(int, input().split()))
print(LargeSmallSum(arr))
