r, i, c = list(map(int, [input() for _ in range(3)]))
ans = i
if i == 0:
    ans = 3 if r != 0 else c
elif i == 1:
    ans = c
elif i == 4:
    ans = 3 if r != 0 else 4
elif i == 6:
    ans = 0
elif i == 7:
    ans = 1
print(ans)
