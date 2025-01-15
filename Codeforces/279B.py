n, t = list(map(int, input().split()))
ls = list(map(int, input().split()))
l = 0
r = 0
total = 0
current = 0
while r < n:
    if t >= ls[r]:
        t -= ls[r]
        r += 1
        current += 1
    else:
        t += ls[l]
        l += 1
        current -= 1
    total = max(current, total)

print(total)