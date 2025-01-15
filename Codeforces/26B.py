# import sys
# sys.stdin = open("input.txt", "r")

s = input()
log = []
count = 0
for char in s:
    if char == "(":
        log.append("(")
    elif char == ")":
        if len(log) == 0:
            continue
        last = log.pop()
        if last == "(":
            count += 1
        else:
            break
print(count * 2)


# sys.stdin.close()