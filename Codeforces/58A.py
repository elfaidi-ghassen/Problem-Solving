def said_hello(str):
    word = "hello"
    j = -1
    for k in word:
        while True:
            j += 1
            if j >= len(str):
                return False
            if str[j] == k:
                break
    return True
    
word = input()
print("YES" if said_hello(word) else "NO")
