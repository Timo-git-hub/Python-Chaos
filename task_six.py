word = input("Enter a string: ")

index = 0

for character in word:

    if index % 2 == 0:
        print(character)

    index += 1

