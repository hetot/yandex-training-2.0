n = int(input())
folders = list(map(int, input().split()))
folders.sort()
print(sum(folders[0:n - 1]))
