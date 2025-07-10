# # num=int(input())
# # for i in range(1,num+1,1):
# #     print(i,end=" ")
# # print()
# for i in range(1,11):
#     for j in range(i,i*10+1,i):
#         print(j,end=" ")
#     print()

# for i in range(1,3):
#     j=1
#     while j<3:
#         print(i,j)
#         j+=1
#     print("kiran")

# ll=[[20,30,40],[50,60,70],[80,90,100]]
# for l in ll:
#     for i in l:
#         print(i, end=" ")
#     print()  # Print a new line after each inner list

# # Print a square pattern of stars
# n=int(input("Enter the size of the square: "))
# for i in range(n):
#     for j in range(n):
#         print("*", end="")
#     print()  # Print a new line after each row

# # Print a right-angled triangle pattern of stars
n=int(input("Enter the size of the triangle: "))
for i in range(n):
    for j in range(i+1):
    # for j in range(n-i): reversed triangle
        print("*", end="")
    print()  # Print a new line after each row

# print a pyramid pattern of stars
n=int(input("Enter the size of the pyramid: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for k in range(2*i+1):
        print("*", end="")
    print()  # Print a new line after each row


n=123

while n>=10:
    # n=n%10  # This will give the last digit
    n=n//10
print(n)  # This will print the first digit of the number

s="hello"
print(s[2::])

for i in range(1,5):
    for j in range(1,10):
        print(i+j)

# First Non-Repeating Character
# Find the first character in a string that does not repeat.
# Input: "aabbcdeff" → Output: "c"
def first_non_repeating_char(s):
    char_count = {}
    
    # Count occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None  # If no non-repeating character is found

# Example usage
s = "aabbcdeff"
result = first_non_repeating_char(s)
if result:
    print(f"The first non-repeating character is: '{result}'")
else:
    print("No non-repeating character found.")


# First Repeating Character
def first_repeating_char(s):
    seen = set()
    
    # Iterate through the string
    for char in s:
        # If the character is already seen, return it
        if char in seen:
            return char
        # Otherwise, add it to the seen set
        seen.add(char)
    
    return None  # If no repeating character is found
# Example usage
s = "abcdeafg"
result = first_repeating_char(s)
if result:
    print(f"The first repeating character is: '{result}'")
# Remove Vowels from a String


# Remove Duplicate Characters from a String
# Input: "programming" → Output: "progamin"
def remove_duplicates(s):
    seen=[]
    for i in s:
      if i not in seen:
        seen.append(i)
        result = ''.join(seen)
    return result
s = "programming"
print("Enter a string to remove duplicates:",remove_duplicates(s))


# Remove Vowels from a String
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    result = ''.join([char for char in s if char not in vowels])
    return result
s = "hello world"
print("String after removing vowels:", remove_vowels(s))
# Reverse a String
def reverse_string(s):
    return s[::-1]  # Using slicing to reverse the string
s = "hello"
print("Reversed string:", reverse_string(s))

# average of numbers by taking input from user
n=map(int, input("Enter the number of elements: ").split())
total = 0
n = int(input("Enter the number of elements: "))                


total = 0
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    total += num
average = total / n