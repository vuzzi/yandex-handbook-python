left = 0
right = 1001
s = ''

while s != "Угадал!":
    mid = (left + right) // 2
    match (s := input(str(mid) + "\n")):
        case "Меньше":
            right = mid + 1
        case "Больше":
            left = mid
