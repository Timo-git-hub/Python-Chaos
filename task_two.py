total = 0
count = 0

number = float(input("Enter a number (-1 to stop): "))

while number != -1:

    total = total + number
    count = count + 1

    average = total / count

    print("Running average:", average)

    number = float(input("Enter another number (-1 to stop): "))

print("Program ended.")

