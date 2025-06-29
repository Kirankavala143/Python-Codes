# a="kiran"
# print(a[::-1])
# print(''.join(reversed(a)))
# re=""
# for i in a:
#     re=i+re
# print(re)

# Count vowels and consonants
a="kirankumar"
vowels="aeiou"
count=0
constant=0
for i in a:
    if i in vowels:
        count+=1
    else:
        constant+=1
print(vowels)
print(constant)


# Remove duplicates from a string
a="kirankumar"
b=""
for i in a:
    if i not in b:
        b+=i
print(b)

# Find the most frequent character
a = "kirankumar"
count = {}
# Count character frequencies
for i in a:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
# Find the character with the highest frequency
most_frequent_char = max(count, key=count.get)

print("Most frequent character:", most_frequent_char)
print("Frequency:", count[most_frequent_char])

# Capitalize the first letter of each word
a = "hello is od kirankk world"
words = a.split()
print(words)
capitalized_words = [word.capitalize() for word in words]
result = " ".join(capitalized_words)
print(result)

# to convert or mutable the string
def fun(a,position,newchar):
    return a[:position] + newchar + a[position+1:]
string = "kirankumar"
position = 5
character = 's'
print(fun(string,position,character))

# Fibonacci Sequence
def fibonacci(n):
    a,b=0,1
    s=[]
    for i in range(n):
        s.append(a)
        a, b = b, a + b
    return s
# Fibonacci Sequence
n = 10
fib_sequence = fibonacci(n)
print(f"Fibonacci sequence of length {n}: {fib_sequence}")

# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string) - len(sub_string) + 1):
#         if string[i:i+len(sub_string)] == sub_string:
#             count += 1
#     return count

# string = "kirankumarkira"
# sub_string = "kira"
# print(count_substring(string, sub_string))

print(2 == 2.0)
