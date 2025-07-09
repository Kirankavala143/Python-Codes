n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()

# right angled
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# reverse triangle
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# Right angled triangle with spaces
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# right sided triangle 
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# hill pattern
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# reverse hill pattern
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# Right-Shifted Rectangle of Stars
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(n):
#         print("*",end=" ")
#     print()

# diamond pattern
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# pyramid
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# double hill
# for i in range(n):
#     for j in range(i,n-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(2*(n-i-1)):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

#butterfly
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    print()

# left pascal triangle





























# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()


#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5

# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     print()