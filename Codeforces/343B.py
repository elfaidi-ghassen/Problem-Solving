ls = []
s = input()
for char in s:
    if ls and ls[-1] == char:
        ls.pop()
    else:
        ls.append(char)
 
print("Yes" if not ls else "No")
