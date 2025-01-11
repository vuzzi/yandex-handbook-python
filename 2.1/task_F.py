product = input()
price = int(input())
weight = int(input())
money = int(input())

print(f"Чек\n"
      f"{product} - {weight}кг - {price}руб/кг\n"
      f"Итого: {weight * price}руб\n"
      f"Внесено: {money}руб\n"
      f"Сдача: {money - price * weight}руб")
