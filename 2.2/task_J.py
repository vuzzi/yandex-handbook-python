n = int(input())

d1 = n % 10 + n // 10 % 10
d2 = n // 100 + n // 10 % 10

print(max(d1, d2), min(d1, d2), sep="")
