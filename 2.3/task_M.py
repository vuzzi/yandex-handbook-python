n = range(int(input()) - 1)
min_name = input()

for _ in n:
    if (name := input()) < min_name:
        min_name = name
print(min_name)
