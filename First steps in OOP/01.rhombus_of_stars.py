def print_row(n):
    print(" " * (n - row), end="")
    for col in range(1, row + 1):
        print("* ", end="")
    print()


n = int(input())

for row in range(1, n + 1):
    print_row(n)

for row in range(n - 1, -1, -1):
    print_row(n)