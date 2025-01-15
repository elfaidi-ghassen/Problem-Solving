from collections import deque 
# import sys
# sys.stdin = open("input.txt", "r")
 
n = int(input())
 
for _ in range(n):
    s = input()
    ls_left = []
    ls_right = deque()
    for char in s:
        if char == "-":
            if len(ls_left) > 0:
                ls_left.pop()
        elif char == "<":
            if len(ls_left) > 0:
                ls_right.appendleft(ls_left.pop())
        elif char == ">":
            if len(ls_right) > 0:
                ls_left.append(ls_right.popleft())
        elif char.isalnum():
            ls_left.append(char)
    print("".join(ls_left + list(ls_right)))
