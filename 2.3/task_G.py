a, b = int(input()), int(input())

product = a * b

while a != b:
    if a > b:
        a = a - b
    elif b > a:
        b = b - a
print(product // a)
