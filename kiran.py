#    *  
#   * *
#  *   *  
# *     * 
#  *   * 
#   * *  
#    *

# n = int(input())
# a = 1
# for nums in range(1,n+1):
#     if nums == 1:
#         print(" "*(n-nums) + "*") 
#     else:
#         space = " "*(n-nums) + "*"
#         hollow_space = " "*a + "*"
#         print(space + hollow_space)
#         a += 2 
# 0.for nums in range(n-1,0,-1):
#     if nums == 1:
#         print(" "*(n-nums) + "*")
#     else:
#         space = " "*(n-nums) + "*"
#         hollow_space = " "*(n-a) + "*"
#         print(space + hollow_space)
#         a += 2

    

# average of numbers by taking input from user 
## n = int(input("Enter the number of elements: "))
# count = 0
# total = 0
# while count < n:

# def second_highest_unique(*args):
#     unique_nums = list(set(args))  # remove duplicates

#     if len(unique_nums) < 2:
#         return "Not enough unique numbers"
    
#     unique_nums.sort()
#     return unique_nums[-2]  # second largest

# # Taking input
# numbers = list(map(int, input().split()))
# print(second_highest_unique(*numbers))

def compute_product(numbers):
    product = 1
    
    def multiply(num):
        nonlocal product
        product *= num
    
    for i in numbers:
        multiply(i)
    
    return product

# Reading input
nums = list(map(int, input().split()))

# Output result
print(compute_product(nums))
