a, b, c = float(input()), float(input()), float(input())

D = b**2 - 4 * a * c

if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
elif D < 0 or (a == 0 and b == 0 and c != 0):
    print("No solution")
elif a == 0 and b != 0 and c != 0:
    print(f"{-(c / b):.2f}")
elif D > 0:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    print(f"{min(x1, x2):.2f} {max(x1, x2):.2f}")
elif D == 0:
    print(f"{(-b + D ** 0.5) / (2 * a):.2f}")
