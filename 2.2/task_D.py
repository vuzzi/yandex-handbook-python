n1, n2, n3 = int(input()), int(input()), int(input())

if n1 > n2 > n3:
    print("1. Петя\n2. Вася\n3. Толя")
elif n1 > n3 > n2:
    print("1. Петя\n2. Толя\n3. Вася")
elif n2 > n1 > n3:
    print("1. Вася\n2. Петя\n3. Толя")
elif n2 > n3 > n1:
    print("1. Вася\n2. Толя\n3. Петя")
elif n3 > n1 > n2:
    print("1. Толя\n2. Петя\n3. Вася")
elif n3 > n2 > n1:
    print("1. Толя\n2. Вася\n3. Петя")
