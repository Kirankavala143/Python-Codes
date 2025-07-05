# n=int(input("Enter the number of rows: "))
# for  i in range(n+1):
#     print("* " *i)
#     print()

# n=int(input("Enter the number of rows: "))
# for i in range(1, n+1):
#     for j in range(n, n-i, -1):
#         print(j, end=" ")
#     print()




#     A
#    AB 
#   ABC
#  ABCD
# ABCDE   
# n = 5
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(1, i + 1):
#         print(chr(64 + k), end="")
#     print()

# 1
# 12    
# 123
# 1234
# 12345

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()

#   *
#  **
# ***
#  **
#   *



       
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(1, i - 1):
        print("*", end="")
    print() 