l, k = list(map(int, input().split()))
coord = list(map(int, input().split()))
left, right = -1, -1

if l % 2 == 1 and int(l / 2) in coord:
    print(int(l / 2))
elif k == 2:
    print(' '.join(map(str, coord)))
else:
    for i in range(int(l / 2), l):
        if i in coord:
            right = i if right == -1 else right
        if l - i - 1 in coord:
            left = l - i - 1 if left == -1 else left
    print(left, right)
