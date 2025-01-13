n1, n2 = int(input()), int(input())

for i in range(n1, n2 - 1 if n2 < n1 else n2 + 1, -1 if n2 < n1 else 1):
    print(i, end=" ")
