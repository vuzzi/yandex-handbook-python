n = 0
while (text := input()) != "Приехали!":
    if "зайка" in text:
        n += 1
print(n)
