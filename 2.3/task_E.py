result = 0
while (n := float(input())) != 0:
    if n < 500:
        result += n
    else:
        result += n - n / 10
print(result)
