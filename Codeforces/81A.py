s = input()
 
stack = []
for char in s:
    if len(stack) == 0:
        stack.append(char)
    else:
        if stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
 
print("".join(stack))
