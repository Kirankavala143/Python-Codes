# covert string to integer
a="5"
b=int(a)
print(b*5)

# Even or Odd Checker
n=int(input("Enter a number: "))
if n%2==0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")

# Factorial using loops and recursion
def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial_loop(n))
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
# Example usage
n = 5
print(factorial_recursive(n))

# Palindrome Checker
def is_palindrome(s):
    s = s.lower()  # Convert to lowercase for case-insensitive comparison
    return s == s[::-1]  # Check if the string is equal to its reverse
# Example usage
s = "racecar"
if is_palindrome(s):
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")   

def fibonacci(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    
# Fibonacci Sequence
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
# Example usage
n = 10
fib_sequence = fibonacci(n)
print(f"Fibonacci sequence of length {n}: {fib_sequence}")

# Prime Number Checker
def is_prime(num):
    if num < 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i==0:
            return False
    return True
# Example usage
num = 29
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
# Sum of Digits
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10  # Add the last digit to the total
        n //= 10  # Remove the last digit
    return total

# Example usage
n = 12345
result = sum_of_digits(n)
print(f"The sum of digits in {n} is: {result}")


