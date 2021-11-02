n = int(input())
M, count = 1, 0
while n != 0:
    if M < n:
        count = 0
        M = n
    count = (count + 1) if M == n else count
    n = int(input())
print(count)
