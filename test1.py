# # while loop to print reverse of numbers
# n = int(input("Enter a number: "))
# # for i in range(n, 0, -1):
# #     print(i, end=" ")
# # while n>0:
# #     print(n)
# #     n-=1
# while n<=0:
#     print(n)
#     n += 1
a, b = map(int, input().split())

# Determine the effective lower and upper bounds of the range
lower_bound = min(a, b)
upper_bound = max(a, b)

# The logic for printing the sequence depends on whether the numbers
# are generally positive or negative, as implied by the expected outputs.

if upper_bound >= 0:
    # This branch handles cases where the range includes positive numbers or zero,
    # or is entirely positive (e.g., 10 20).
    # The expected behavior is to print even numbers in descending order.

    # Find the largest even number less than or equal to the upper_bound
    current_num = upper_bound
    if current_num % 2 != 0:
        current_num -= 1  # Adjust to the preceding even number

    # Print the sequence in descending order, stepping by -2
    while current_num >= lower_bound:
        print(current_num, end=" ")
        current_num -= 2
else:
    # This branch handles cases where the range is entirely negative
    # (e.g., -10 -20).
    # The expected behavior is to print even numbers in ascending order.

    # Find the smallest even number greater than or equal to the lower_bound
    current_num = lower_bound
    if current_num % 2 != 0:
        current_num += 1  # Adjust to the next even number (towards zero)

    # Print the sequence in ascending order, stepping by +2
    while current_num <= upper_bound:
        print(current_num, end=" ")
        current_num += 2

# # for loop to print reverse of numbers
# n = int(input("Enter a number: "))
# for i in range(n, 0, -1):
#     print(i, end=" ")

# while loop to print reverse of numbers
n = int(input("Enter a number: "))
while n>0:    
    print(n)      
    n-=1              
