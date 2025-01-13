a, b, c = int(input()), int(input()), int(input())

print("YES") if a < b + c and b < a + c and c < a + b else print("NO")
