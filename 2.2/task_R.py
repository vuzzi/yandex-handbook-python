a, b, c = int(input()), int(input()), int(input())

a_max = max(a, b, c)
b_min = min(a, b, c)
c_min = a + b + c - a_max - b_min

if a_max ** 2 == (b_min ** 2 + c_min ** 2):
    print("100%")
elif a_max ** 2 > (b_min ** 2 + c_min ** 2):
    print("велика")
elif a_max ** 2 < (b_min ** 2 + c_min ** 2):
    print("крайне мала")
