# Create a dictionary with student names and marks.
student_marks = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}
print(student_marks)

# Find the student with the highest marks.
topper=max(student_marks,key=student_marks.get)
print("topper:",topper)
print("marks:",student_marks[topper])


# Count how many students scored above 50.
count=0
for i in student_marks.values():
    if i>50:
        count+=1
print(count)

# DICTIONARY COMPREHENSION

# {key_expression: value_expression for item in iterable if condition}
# {x:x**2 for x in range(5)}


# Write a function to invert keys and values.
def ivert(d):
    return {v:k for k,v in d.items()}
def invert_dict(d):
    return {v: k for k, v in d.items()}
print(invert_dict(student_marks))

# 'Create two sets and find union, intersection, and difference.
s={1,2,3,4,5}
s1={2,3,4,5,6}
print(s.union(s1))
print(s.intersection(s1))
print(s.difference(s1))

# Remove duplicates from a list using a set.
l=[2,3,4,5,3,4,5,3]
l=list(set(l))
print(l)

# Check if two sets are disjoint.
s={1,2,3}
s1={4,5,6}
print(s.isdisjoint(s1)) 

# Find the symmetric difference between two sets.
s={1,2,3,4,5}
s1={2,3,4,5,6}
print(s.symmetric_difference(s1))

# Project: Student Gradebook

# Store student data in a dictionary.
student_data={
    "student1":{
       "name":"Alice",
       "marks":85,
    },
    "student2":{
       "name":"Bob",
       "marks":92,
    },
    "student3":{
       "name":"Charlie",
       "marks":78,
    },
    "student4":{
       "name":"David",
       "marks":95,
    }
 }


# Allow searching for a student by name.
name = input("Enter name: ")
found = False

for i in student_data:
    if student_data[i]["name"] == name:
        print("Name:", student_data[i]["name"])
        print("Marks:", student_data[i]["marks"])
        found = True
        break

if not found:
    print("Student not found")

# Allow adding, removing, and updating records.
add_name = input("Enter name: ")
add_marks = int(input("Enter marks: "))

student_data["student5"] = {
    "name": add_name,
    "marks": add_marks
}
# remove student
remove_name = input("Enter name to remove: ")
if remove_name in student_data:
    del student_data[remove_name]
else:
    print("Student not found")

# Allow updating marks.
update_name = input("Enter name to update: ")
update_marks = int(input("Enter new marks: "))
found = False

for roll in student_data:
    if student_data[roll]["name"].lower() == update_name.lower():
        student_data[roll]["marks"] = update_marks
        print("Marks updated successfully.\n")
        found = True
        break

if not found:
    print("Student not found.\n")



# Option to sort and display all records.
for i in sorted(student_data):
    print("Name:", student_data[i]["name"])
    print("Marks:", student_data[i]["marks"])
    print()



student={"name":"kiran","marks":78}
print(student)

