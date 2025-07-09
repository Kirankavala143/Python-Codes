# What’s the difference between is and == in Python?
# == is a comparison operator that checks whether two values are equal or not.
# is is an identity operator that checks whether two variables point to the same object or not.

# What happens when you use mutable types as default function arguments?
# Using mutable types (like lists or dictionaries) as default arguments can lead to unexpected behavior because the default value is shared across all calls to the function.
# If the mutable object is modified, the change will persist across future calls to the function.

# What’s the difference between float('nan') == float('nan') and math.isnan()?
# float('nan') == float('nan') returns False because NaN (Not a Number) is not equal to itself.
# math.isnan() returns True if the input value is NaN, allowing you to check for NaN values correctly.

# How can you force Python to treat an int literal as binary, octal, or hexadecimal?
# You can force Python to treat an int literal as binary, octal, or hexadecimal by using prefixes:
# 0b for binary, 0o for octal, and 0x for hexadecimal.      
# Example:
# num = 0b1010  # 10 in binary
# num = 0o123   # 83 in octal
# num = 0x123   # 291 in hexadecimal        

