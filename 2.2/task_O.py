n1, n2 = int(input()), int(input())

d1 = n1 // 10
d2 = n1 % 10
d3 = n2 // 10
d4 = n2 % 10

d_max = max(d1, d2, d3, d4)
d_min = min(d1, d2, d3, d4)
d_mid = (d1 + d2 + d3 + d4 - d_max - d_min) % 10

print(d_max, d_mid, d_min, sep="")
