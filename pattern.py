# *
# **
# ***
# ****
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="")
    print()

# ****
# ***
# **
# *

for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()

#    *
#   ***
#  *****



for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(1,i*2):
        print("*",end="")
    print()

#    *
#   ***
#  *****
#   ***
#    *


n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()

