# s="kiran wants to smart"
# if "kir" in s:
#     print("found")

# k="kiran"
# k="K"+k[1:]
# print(k)

# # Count the number of vowels in a string.
# a="kirankumar"
# vowels="AEIOUaeiou"
# count=0
# for i in a:
#     if i in vowels:
#         count+=1
# print(count)

# # Reverse a string (without using slicing).
# a="kiran"
# print(''.join(reversed(a)))
# reverse=""
# for i in a:
#         reverse=i+reverse
# print(reverse)

# # Check if a string is a palindrome.
# a=input("enter a string:")
# b=(a[::-1])
# if a==b:
#     print("palindrome")
# else:
#     print("not a palindrome")

# # Count how many times each character appears in a string.
# a="kirankumar"
# print(a.count("k"))
# c=input("enter a string:")
# character=input("enter a character:")
# print(c.count(character))

# # Check if two strings are anagrams (e.g., "listen" and "silent").
# a=input("enter a string:")
# b=input("enter a string:")
# if sorted(a)==sorted(b):
#     print("anagrams")
# else:
#     print("not anagrams")


# # Remove all duplicate characters from a string.
# s="kirankumar"
# result=""
# seen=set()
# for i in s:
#     if i not in seen:
#         seen.add(i)
#         result += i
# print(result)


# def remove_duplicates(s):
#     result = ""
#     seen = set()
#     for char in s:
#         if char not in seen:
#             seen.add(char)
#             result += char
#     return result

# # Example
# s = input("Enter a string: ")
# print("String after removing duplicates:", remove_duplicates(s))

# # Find the first non-repeating character in a string.
# def first_non_repeating_char(s):
#     char_count = {}
#     for char in s:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
            
#     for char in s:
#         if char_count[char] == 1:
#             return char
            
#     return None
# s = input("Enter a string: ")
# result = first_non_repeating_char(s)
# if result:
#     print("First non-repeating character:", result)
# else:
#     print("No non-repeating character found.")

# Check if a string is a pangram (contains every letter of the alphabet at least once).
import string
def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(s.lower())
s = input("Enter a string: ")
if is_pangram(s):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")   



# Show missing letters (if not a pangram):
def is_pangram_verbose(s):
    alphabet = set(string.ascii_lowercase)
    input_set = set(s.lower())
    missing = alphabet - input_set
    if not missing:
        print("The string is a pangram.")
    else:
        print("Not a pangram. Missing letters:", ''.join(sorted(missing)))

s = input("Enter a string: ")
is_pangram_verbose(s)



# Find the longest word in a string.
def longest_word(s):
    words = s.split()
    longest = max(words, key=len)
    return longest
s = input("Enter a string: ")
result = longest_word(s)
print("Longest word:", result)

s="hello is the kirankumar world"
word=s.split()
longest=max(word,key=len)
print("Longest word:", longest)
# Find the shortest word in a string.
def shortest_word(s):
    words = s.split()
    shortest = min(words, key=len)
    return shortest
s = input("Enter a string: ")
result = shortest_word(s)
print("Shortest word:", result)


# Count the number of words in a string.
def word_count(s):
    words = s.split()
    return len(words)
s = input("Enter a string: ")
result = word_count(s)
print("Number of words:", result)

# Check if a string contains only digits.
def is_digit_string(s):
    return s.isdigit()

s = input("Enter a string: ")
if is_digit_string(s):
    print("The string contains only digits.")   
else:
    print("The string contains non-digit characters.")

# Check if a string contains only alphabetic characters.
def is_alpha_string(s):
    return s.isalpha()

s = input("Enter a string: ")
if is_alpha_string(s):
    print("The string contains only alphabetic characters.")
else:
    print("The string contains non-alphabetic characters.")



