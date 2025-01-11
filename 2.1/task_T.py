n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())

x = (m * n - k2 * n) // (k1 - k2)
y = n - x

print(x, y)
