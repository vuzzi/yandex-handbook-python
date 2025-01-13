n1, n2, n3 = int(input()), int(input()), int(input())

if n1 > n2 > n3:
    win1, win2, win3 = "Петя", "Вася", "Толя"
elif n1 > n3 > n2:
    win1, win2, win3 = "Петя", "Толя", "Вася"
elif n2 > n1 > n3:
    win1, win2, win3 = "Вася", "Петя", "Толя"
elif n2 > n3 > n1:
    win1, win2, win3 = "Вася", "Толя", "Петя"
elif n3 > n1 > n2:
    win1, win2, win3 = "Толя", "Петя", "Вася"
elif n3 > n2 > n1:
    win1, win2, win3 = "Толя", "Вася", "Петя"

print(f"{win1:^24}\n"
      f"{win2:^8}\n"
      f"{win3:^40}\n"
      f"{"II":^8}{"I":^8}{"III":^8}")
