n = int(input())
i = 2

while n != i:
    if n % i == 0 and n // i != 1:
        print(i, end=" * ")
        n = n // i
    else:
        i += 1

print(i, end="")
