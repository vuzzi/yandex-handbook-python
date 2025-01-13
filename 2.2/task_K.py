seq = list(map(int, input()))
sum_min_max = max(seq) + min(seq)

print("YES") if sum_min_max == (sum(seq) - sum_min_max) * 2 else print("NO")
