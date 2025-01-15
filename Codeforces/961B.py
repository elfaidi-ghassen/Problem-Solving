n, k = list(map(int, input().split()))
ls1 = list(map(int, input().split()))
ls2 = list(map(int, input().split()))
 
cs1 = [ls1[0]]
for i in range(1, len(ls1)):
    cs1.append(ls1[i] + cs1[i - 1])
 
cs2 = [ls1[0] * ls2[0]]
for i in range(1, len(ls2)):
    cs2.append(ls1[i] * ls2[i] + cs2[i - 1])
 
 
def fromTo(ls, l, r):
    if l == 0:
        return ls[r]
    else:
        return ls[r] - ls[l - 1] 
 
 
max = fromTo(cs1, 0, k - 1) + fromTo(cs2, k, n - 1)
for i in range(1, n - k + 1):
    newmax = fromTo(cs2, 0, i - 1) + fromTo(cs1, i, i + k - 1) + fromTo(cs2, i + k, n - 1)
    if newmax > max:
        max = newmax
 
 
print(max)
