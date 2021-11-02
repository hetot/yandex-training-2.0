n, i, j = list(map(int, input().split()))
ans = min(abs(j - i) - 1, abs(i - 1) + abs(n - j) if i < j else abs(j - 1) + abs(n - i))
print(ans)
