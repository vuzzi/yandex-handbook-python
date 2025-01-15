n = input()
result = int(n)

for i in n:
    if int(i) == result % 10:
        result //= 10

print("YES") if result == 0 else print("NO")
