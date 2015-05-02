vowels = "aeiouyAEIOUY"
count = 0

string = input("Enter string: ")

for ch in string:
    if ch in vowels:
        count += 1

print(count)
