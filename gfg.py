
def process(text):
    text = ''.join(e for e in text if e.isalnum() or e.isspace())
    text = text.strip()
    return text
result = input("Enter a text:")   
print(process(result)) 

# count digits
n=int(input("Enter a number: "))
count = 0
while n>0:
    n=n//10
    count+=1
print("Number of digits:", count)

# factorial of a number
n = int(input("Enter a number: "))
res=1
for i in range(2,n+1):
    res=res*i
print("Factorial of", n, "is", res)