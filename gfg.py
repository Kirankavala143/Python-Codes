def process(text):
    text = ''.join(e for e in text if e.isalnum() or e.isspace())
    text = text.strip()
    return text
result = input("Enter a text:")   #Enter a text:###Hello i am Akhila from @Kiet-W with the roll no: 22JN1A4506,!
print(process(result)) #Output: Hello i am Akhila from KietW with the roll no 22JN1A4506