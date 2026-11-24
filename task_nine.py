target = int(input("Enter the target value: "))

found = False

for first in range(1, 10):

    for second in range(first + 1, 10):

        for third in range(second + 1, 10):

            if first + second + third == target:

                print(first, "+", second, "+",
                      third, "=", target)

                found = True

if found == False:
    print("No combinations found.")

