# FUNCTIONS
# Write a function to check if a number is even or odd.
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
# Example usage
s=int(input("enter a number: "))
print(even_odd(s))  # Output: Even