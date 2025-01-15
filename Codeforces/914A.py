squares = set()
n = 0
while True:
    if n * n > 10**6:
        break
    squares.add(n * n)
    n = n + 1
 
def greatest_non_square(ls):
    return max(set(ls) - squares)
 
def test():
    size = int(input())
    line = input()
    print(greatest_non_square(list(map(int, line.split()))))
test()
