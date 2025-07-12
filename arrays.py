# Arrays
a=[1, 2, 3, 4, 5]
# b=[6, 7, 8, 9, 10]
# c=a+b
# print(c)

# Append, Insert, Pop
# a.append(11)
# a.insert(0,0)
# print(a)
# a.pop(0)
# print(a)    

# Slice, Loop through/
# print(a[1:4])  # Slicing

# for i in a:
#     print(i, end=' ')  # Looping through the array  

# Reverse an array
# reversed_array = a[::-1]
# print(reversed_array)

# Find the max/min element
# max_element = max(a)
# min_element = min(a)              
# print("Max:", max_element)
# print("Min:", min_element)

# another way to find max/min
# max_element = a[0]
# min_element = a[0]
# for i in a:
#     if i > max_element:
#         max_element = i
#     elif i < min_element:
#         min_element = i
# print("Max:", max_element)
# print("Min:", min_element)

# Rotate an array

# def rotate_array(arr, k):
#     n = len(arr)
#     k = k % n  # Ensure k is within the range of the array length
#     rotated_arr = arr[k:] + arr[:k]
#     return rotated_arr

# arr = [1, 2, 3, 4, 5]
# k = 2
# rotated_arr = rotate_array(arr, k)
# print(rotated_arr)    

# ind the first non-repeating character in a string
def first_non_repeating_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None
s = "swiss"
result = first_non_repeating_char(s)
print("First non-repeating character:", result)

