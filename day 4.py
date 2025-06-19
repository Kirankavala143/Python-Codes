s="kiran wants to smart"
if "kir" in s:
    print("found")

k="kiran"
k="K"+k[1:]
print(k)

# Count the number of vowels in a string.
a="kirankumar"
vowels="AEIOUaeiou"
count=0
for i in a:
    if i in vowels:
        count+=1
print(count)

# Reverse a string (without using slicing).
a="kiran"
print(''.join(reversed(a)))
reverse=""
for i in a:
        reverse=i+reverse
print(reverse)

# Check if a string is a palindrome.
a=input("enter a string:")
b=(a[::-1])
if a==b:
    print("palindrome")
else:
    print("not a palindrome")

# Count how many times each character appears in a string.
a="kirankumar"
print(a.count("k"))
c=input("enter a string:")
character=input("enter a character:")
print(c.count(character))

# Check if two strings are anagrams (e.g., "listen" and "silent").
a=input("enter a string:")
b=input("enter a string:")
if sorted(a)==sorted(b):
    print("anagrams")
else:
    print("not anagrams")


# Remove all duplicate characters from a string.
s="kirankumar"
result=""
seen=set()
for i in s:
    if i not in seen:
        seen.add(i)
        result += i
print(result)


def remove_duplicates(s):
    result = ""
    seen = set()
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result

# Example
s = input("Enter a string: ")
print("String after removing duplicates:", remove_duplicates(s))

# Find the first non-repeating character in a string.


