# Create a dictionary to store 5 students’ names and their marks.
student_details={
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eve": 45
}
# Find the student with the highest marks.
a=max(student_details,key=student_details.get)
print("topper:",a)
print("marks:",student_details[a])

# find score higher than 50 and print student names
for i in student_details:
    if student_details[i]>50:
        print(i,student_details[i])

# count
count=0
for i in student_details:
    if student_details[i]>50:
        count+=1
print(count)

# Count the number of keys in a dictionary.
print(len(student_details))

# Check if a key exists in the dictionary.
print("Eve" in student_details)

# Remove a key-value pair from the dictionary.
del student_details["Eve"]
print(student_details)

# Check if a key exists in the dictionary.
if "Alice" in student_details:
    print("Alice is in the dictionary")
else:
    print("Alice is not in the dictionary")

# Merge two dictionaries.
student_details1={
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95
}

student_details2={
    "Eve": 45,
    "Frank": 56
}
# merge
student_details1.update(student_details2)
print(student_details1)

# Count frequency of each character in a string.
s="kiran"
count={}
for i in s:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)

