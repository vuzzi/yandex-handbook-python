count = (int(input()) * 60 + int(input()) + int(input()))
print(f"{(count // 60 % 24):0>2}:{(count % 60):0>2}")
