n = int(input())

d1 = n // 100
d2 = n // 10 % 10
d3 = n % 10

d_max = max(d1, d2, d3)

if d1 == d_max:
    num_max = str(d1) + str(max(d2, d3))
    if d2 == 0:
        num_min = str(d3) + str(d2)
    elif d3 == 0:
        num_min = str(d2) + str(d3)
    else:
        num_min = str(min(d2, d3)) + str(max(d2, d3))

if d2 == d_max:
    num_max = str(d2) + str(max(d1, d3))
    if d1 == 0:
        num_min = str(d3) + str(d1)
    elif d3 == 0:
        num_min = str(d1) + str(d3)
    else:
        num_min = str(min(d1, d3)) + str(max(d1, d3))

if d3 == d_max:
    num_max = str(d3) + str(max(d1, d2))
    if d1 == 0:
        num_min = str(d2) + str(d1)
    elif d2 == 0:
        num_min = str(d1) + str(d2)
    else:
        num_min = str(min(d1, d2)) + str(max(d1, d2))

print(num_min, num_max)
