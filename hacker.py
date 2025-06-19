arr=[2,3 ,6, 6, 5]
unique_scores = list(set(arr))  # remove duplicates
unique_scores.sort()  
print(unique_scores)  # sort in ascending order

print(unique_scores[-2])

t = int(input())
for i in range(t):
    s=input()
    x=s+s
    print(x)
t = int(input())
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

t = int(input())
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
