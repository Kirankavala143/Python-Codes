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
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()