# def sum(end):
#     sum=0
#     for i in range(1,end+1):
#         sum=sum+i
#     return sum 
# var=sum(10)
# var2=sum(20)
# print(var)
# print(var2)


#Syntax
'''def function_name(parameters):
        #block of code
        return value  #(optional)'''

'''Term        -        Description
    def        -   keyword to define function
function_name  -   Any valid python identifier
  parameters   -   input passes to the function
     :         -   Ends the function header
indentend block-   code that runs when the function is called
   return      -   Sends result back to caller '''

#Example:-
# def hi():
#     print("Hello students")
# hi()    # Hello students
# #Ex1:-
# def students():
#     return 80
# total = students()
# print("Total students :",total)  # Total students : 80
# #Ex2-without using function calling:-
# def stu():
#     return 80
# tot = stu()
# print("Total students :",80) # Total students : 80

# '''Function Arguments
# 3types of arguments
# 1.positional 2.Keyword 3.Default

# #ex-on positional'''
# def hi(name):
#     print("hello",name)
# hi("kiran")  # hello kiran

# '''#ex- on Default'''
# def hi(name="friends"):
#     print("Hello",name)
# hi()        # Hello friends
# hi("Surya")  # Hello Surya

# '''#ex- on Keyword'''
# def stu(name,age):
#     print("Name:",name)
#     print("Age:",age)
# stu(age = 19, name = "Akhila")  

# '''------------------------------------------------------------------
#    | Feature    |     Description               |    Example        |
#    ------------------------------------------------------------------             
#    |    def     |    defines a function        |   def hi()         |
#    |  Arguments |    pass data into a function |   def hi(name):    |
#    |   return   |    Sends result back         |   return a+b       |
#    |    call    |    Use the function          |   Hi("Kiran")      | 
#    ------------------------------------------------------------------ '''

# #Types of functions:-
# #examples:-
# '''1.No Arguments, No return value'''
# def fun():
#     print("Keep smiling")
# fun()   # Keep smiling
# '''2.With Arguments, No Return value'''
# def greet(name):
#     print("Hello",name)
# greet("students")  # Hello students
# '''3.No Arguments, With Return value'''
# def hi():
#     return "friends"
# value = hi()
# print("Wishes:",value) # Wishes: friends
# '''4.with Arguments and Return value'''
# def add(a,b):
#     return a+b
# res = add(2,5)
# print("Sum:",res)  #Su

# def sum_of_digits(num):
#     total = 0
#     while num > 0:
#         total += num % 10
#         num //= 10
#     return total

# def count_even_digit_sums(arr):
#     count = 0
#     for num in arr:
#         if sum_of_digits(num) % 2 == 0:
#             count += 1
#     return count

# # Input
# n = int(input())
# arr = list(map(int, input().split()))

# # Output
# print(count_even_digit_sums(arr))

# count palindromes
def is_palindrome(arr):
    return str(arr) == str(arr)[::-1]
def count_palindromes(arr):
    count = 0
    for num in arr:
        if is_palindrome(num):
            count += 1
    return count    

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(count_palindromes(arr))


