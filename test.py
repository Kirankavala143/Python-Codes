# 1 write a program to print the sum of the cubes of the numbers from M to N
# def sum_of_cubes(m,n):
#     sum=0
#     for i in range(m,n+1):
#         sum+=i**3
#     return sum

# m=int(input())
# n=int(input())
# print(sum_of_cubes(m,n))    

# a=int(input("enter a number: "))
# b=int(input("enter a number: "))
# sum=0
# cub=0
# for i in range(a,b+1):
#     cub=i**3
#     sum+=cub

# print(sum)
    

# Write a program that reads a distance D in km and calculates the total Score. 
# For the first 50 km (0-50km), the score for each km, is 3 
# For the next 50 km (51-100km), the score for each km, is 5 
# For the next 100 km (101-200km), the score for each km, is 6 
# For the first 50 km (201-250km), the score for each km, is 8 
# For the above 250 km, the score for each km, is 10 
# Apart from the above scores, there is a bonus score of 100 
# Sample input1: 
# 120 
# Sample output1: 
# 620 
# Explanation: 
# D=120km 

d = int(input())
score = 0
bonus = 100
if d > 250:
  score += (d-250) * 10
  d = 250
if d > 200:
  score += (d-200) * 8
  d = 200
if d > 100:
  score += (d-100) * 6
  d = 100
if d > 50:
  score += (d-50) * 5
  d = 50
if d > 0:
  score += d * 3
tot = score + bonus
print(tot)

#  Armstrong number
num=int(input("enter a number:"))
original_num=num
length=len(str(num))
sum=0
while num>0:
    digit=num%10
    sum+=digit**length
    num=num//10

if sum==original_num:
    print("armstrong number")
else:
    print("not an armstrong number")

# Write a program that reads an amount A and prints the minimum number of 2000, 500, 200, 50, 
# 20, 5, 2 and 1 rupee notes required for the given amount.
A=int(input())

print(A//2000)
A=A%2000
print(A//500)
A=A%500
print(A//200)
A=A%200
print(A//50)
A=A%50
print(A//20)
A=A%20
print(A//5)
A=A%5
print(A//2)
A=A%2
print(A//1)
