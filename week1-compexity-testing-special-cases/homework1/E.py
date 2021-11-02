d = int(input())
x, y = list(map(int, input().split()))
ans = 0
if x < 0 or y < 0:
    if x < 0 and y < 0:
        ans = 1
    elif x < 0:
        ans = 1 if y <= d / 2 else 3
    else:
        ans = 1 if x <= d / 2 else 2
elif (x + y) > d:
    ans = 2 if x == y or x > y else 3
print(ans)
