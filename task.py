# find min and max in a list 
l=[4,7,9,2,1,4,5,6]
smallest = largest = l[0]
for i in l:
    if i < smallest:
        smallest = i
    elif i > largest:
        largest = i
print(smallest)
print(largest)

s=l.sort()
smallest = l[0]
largest = l[-1]
print(smallest)
print(largest)


