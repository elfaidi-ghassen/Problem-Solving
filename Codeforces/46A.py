n = int(input())
arr = [i for i in range(1, n + 1)]
 
k = 1
i = 0
for z in range(n - 1):
    print(arr[(i + k)%n], end=" ")
    i = (i + k)%n
    k += 1
