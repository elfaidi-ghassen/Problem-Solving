n = int(input())
lon = map(int, input().split())
lon = sorted(lon, reverse=True)
total = sum(lon)
count = 0
taken = 0
for k in lon:
    if taken > total:
        break
    else:
        count += 1
        taken += k
        total -= k
 
print(count)
