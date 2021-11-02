coord = list(map(int, input().split()))
M = 0
shop_coord = list()
for i, x in enumerate(coord):
    if x == 2:
        shop_coord.append(i)
for i, x in enumerate(coord):
    if x == 1:
        l = min([abs(k - i) for k in shop_coord])
        M = l if l > M else M
print(M)
