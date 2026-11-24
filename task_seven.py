word = input("Enter a string: ")

reverse = ""

for character in word:

    reverse = character + reverse

print("Original string:", word)
print("Reversed string:", reverse)

