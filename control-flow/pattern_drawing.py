size_of_pattern = int(input("Enter the size of the pattern: "))

rows = 1
while rows <= size_of_pattern:
    for i in range(size_of_pattern):
        print("*", end="")
    print()
    rows = rows + 1
