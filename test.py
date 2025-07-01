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

# 3 Armstrong number
# num=int(input("enter a number:"))
# original_num=num
# length=len(str(num))
# sum=0
# while num>0:
#     digit=num%10
#     sum+=digit**length
#     num=num//10

# if sum==original_num:
#     print("armstrong number")
# else:
#     print("not an armstrong number")

# Write a program that reads an amount A and prints the minimum number of 2000, 500, 200, 50, 
# 20, 5, 2 and 1 rupee notes required for the given amount.

# 4

# A=int(input())
# notes=[2000,500,200,100,50,20,5,2,1]
# for i in notes:
#    count=A//i
#    print(f"{i} :{count}",end=" ")
#    A=A%i

#5 Given a number N write a program to print a Hollow Pyramid of 2*N-1 rows using numbers 
# Sample input1: 
# 4 
# Sample output1: 
# 1 
# 2 2 
# 3   3 
# 4     4 
# 3   3 
# 2 2 
# 1

# n = int(input("Enter N: "))

# # Upper half of the pyramid
# for i in range(1, n + 1):
#     if i == 1:
#         print(i)
#     else:
#         print(i, end=" ")
#         print(" " * (2 * i - 3), end="")
#         print(i)

# # Lower half (inverted)
# for i in range(n - 1, 0, -1):
#     if i == 1:
#         print(i)
#     else:
#         print(i, end=" ")
#         print(" " * (2 * i - 3), end="")
#         print(i)


# 6 You are given two numbers A and B where 1<=A<=B write a program to find number of perfect 
# squares in the range A and B (including A and B)

# A=int(input())
# B=int(input())
# count=0
# for i in range(A,B+1):
#     if i**0.5==int(i**0.5):
#         count+=1
# print(count)

# import math
# A = int(input())
# B = int(input())
# count = math.floor(math.sqrt(B)) - math.ceil(math.sqrt(A)) + 1
# print(count)

# 7 odd,even

# def show_numbers(num):
#     for i in range(1,num+1):
#       if i%2==0:
#         print(i,"even")
#       else:
#         print(i,"odd")

# num=int(input())
# show_numbers(num)
    
#8 reverse 
# s="kiran"
# for i in s[::-1]:
#     print(i)

# order number
# n=int(input())
# l=[]
# for i in range(1,n+1):
#     print(i)
#     l.append(i)
#     print(l)

#9 user input
# n=int(input())
# list=[]
# for i in range(1,n+1):
#     num=int(input())
#     list.append(num)
# print(list)

# 10 add new key value
Student_dict={ "Ram" : "Cricket",  "Naresh":"Football", "Vani":"Tennis", "Rahim":"Cricket"}
keys,values=input().split()
Student_dict[keys] = values
print(Student_dict)
  
