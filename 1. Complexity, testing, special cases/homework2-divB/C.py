line = input()
n = len(line)
count = 0
for i in range(n - 1, (int(n / 2) + n % 2 - 1), -1):
    count = count + 1 if line[i] != line[n - i - 1] else count
print(count)
