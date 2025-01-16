n = int(input())
j = 0

for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        j += 1

print("YES") if j == 1 and n != 1 else print("NO")
