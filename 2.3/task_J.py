x, y = 0, 0

while (text := input()) != "СТОП":
    if "СЕВЕР" in text:
        y += int(input())
    elif "ЮГ" in text:
        y -= int(input())
    elif "ЗАПАД" in text:
        x -= int(input())
    elif "ВОСТОК" in text:
        x += int(input())
print(y, x, sep="\n")
