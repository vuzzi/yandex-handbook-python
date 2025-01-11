name = input()
n = int(input())

print(
    f"Группа №{n // 100}.\n"
    f"{n % 10}. {name}.\n"
    f"Шкафчик: {n}.\n"
    f"Кроватка: {n // 10 % 10}."
)
