# Find time complexity of:

# Reversing an array
# a= [1, 2, 3, 4, 5]
# reversed_array = a[::-1]
# print(reversed_array)

# Checking for a duplicate in a list
a = [1, 2, 3, 4, 5, 1]
has_duplicate = len(a) != len(set(a))
print(has_duplicate)  

# Finding the first repeated character in a string ITS SECOND OCCURRENCE INDEX
# def first_repeated_char(s):
#     seen = {}
#     for char in s:
#         if char in seen:
#             return char     
#         seen[char] = 1
#     return None           
# s = "hello world"
# print(first_repeated_char(s)) 

# first occurrence of a repeated character in a string
# def first_repeated_char(s):
#     seen = set()
#     for char in s:
#         if char in seen:         
#             return char
#         seen.add(char)
#     return None
# s = "hello world" 
# print(first_repeated_char(s))

# enumerate
# def first_repeated_char_first_occurrence(s):
#     seen = {}
#     for index, char in enumerate(s):
#         if char in seen:
#             return char, seen[char]  # return the *first* time it appeared
#         seen[char] = index
#     return None

# s = "hello world"
# print(first_repeated_char_first_occurrence(s))

# Finding the first non-repeating word in a sentence
   

# Finding the first repeated character and its second occurrence index in a string
# def first_repeated_char(s):
#     seen = {}
#     for index, char in enumerate(s):
#         if char in seen:
#             return char, index
#         seen[char] = index
#     return None           
# s = "hello world"
# print(first_repeated_char(s)) 



# anothwer way
# def first_repeated_char(s):
#     seen = {}
#     i = 0
#     for ch in s:
#         if ch in seen:
#             return ch, i
#         seen[ch] = i
#         i += 1
#     return None
# s = "hello world"
# print(first_repeated_char(s))


# first occurrence of a repeated character in a string
# def first_repeated_char(s):
#     seen = set()
#     for char in s:
#         if char in seen:
#             return char
#         seen.add(char)
#     return None
# s = "hello world"
# print(first_repeated_char(s))

# Sorting a list using built-in sort
# a = [5, 2, 9, 1, 5, 6]
# a.sort()  
# print(a)

# Sorting a list using sorted
# a = [5, 2, 9, 1, 5, 6]
# sorted_a = sorted(a)
# print(sorted_a)