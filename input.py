# What’s the difference between is and == in Python?
# == is a comparison operator that checks whether two values are equal or not.
# is is an identity operator that checks whether two variables point to the same object or not.

# What happens when you use mutable types as default function arguments?
# Using mutable types (like lists or dictionaries) as default arguments can lead to unexpected behavior because the default value is shared across all calls to the function.
# If the mutable object is modified, the change will persist across future calls to the function.