arr=[2,3 ,6, 6, 5]
unique_scores = list(set(arr))  # remove duplicates
unique_scores.sort()  
print(unique_scores)  # sort in ascending order

print(unique_scores[-2])

t = int(input("enter number of test cases: "))
for i in range(t):
    s=input()
    x=s+s
    print(x)


t = int(input("enter number of test cases: "))
for i in range(t):
    #Accept 2 integers inputs
    A, B = map(int,input().split())     
    #Sum of inputs
    S = A +B     
    print("kiran")          
    #Product of inputs
    P = A * B               
    #Print the desired output for each test case
    print(S,P) 

t = int(input("enter number of test cases: "))
for i in range(t): 
    X, Y = map(int, input().split())
    s=X*Y
    print(s)

def find_smallest_missing_positive(arr):
    s = set(arr)   # Step 1: Convert list to set

    num = 1        # Start checking from 1
    while True:
        if num not in s:
            return num   # Found the missing number!
        num += 1         # Check next number
print(find_smallest_missing_positive([3, 4, -1, 1]))  # Output: 2
print(find_smallest_missing_positive([1, 2, 0]))      # Output: 3
print(find_smallest_missing_positive([7, 8, 9, 11])) 


x = int(input("enter x: "))
y = int(input("enter y: "))
z = int(input("enter z: "))
n = int(input("enter n: "))

result = [[i, j, k] 
          for i in range(x + 1) 
          for j in range(y + 1) 
          for k in range(z + 1) 
          if i + j + k != n]

print(result)


# second largest number in a list
def second_largest(arr):
    first = second = float('-inf') 

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second if second != float('-inf') else None  # Return None if no second largest found
arr = [2, 3, 6, 6, 5]
print(second_largest(arr))  # Output: 5

