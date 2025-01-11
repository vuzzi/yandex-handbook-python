product = input()
price = int(input())
weight = int(input())
money = int(input())

print(
    f"{'Чек':=^35}\n"
    f"Товар:{product:>29}\n"
    f"Цена:{f'{weight}кг * {price}руб/кг':>30}\n"
    f"Итого:{f'{weight * price}руб':>29}\n"
    f"Внесено:{f'{money}руб':>27}\n"
    f"Сдача:{f'{money - (weight * price)}руб':>29}\n"
    f"{'=' * 35}"
)
