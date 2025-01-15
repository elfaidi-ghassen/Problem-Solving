n, m = list(map(int, input().split()))
d = {}
for _ in range(m):
    w1, w2 = input().split()
    d[w1] = w2
text = input()
 
result = []
for word in text.split():
    temp = word
    if len(d[word]) < len(word):
        temp = d[word]
    result.append(temp)
print(" ".join(result))
