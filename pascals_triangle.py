def pascals_triangle(rows):
    for i in range(rows):
        for j in range(rows - i ):
            print(" ", end="")
        number = 1
        for j in range(i + 1):
            print(number, end=" ")
            number = number * (i - j) // (j + 1)
        print()
pascals_triangle(5)
