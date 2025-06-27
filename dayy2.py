a="kiran"
print(a[::-1])
print(''.join(reversed(a)))
re=""
for i in a:
    re=i+re
print(re)

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