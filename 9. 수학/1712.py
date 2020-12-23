i, j, k = map(int, input().split())
 
if (k - j) <= 0:
    print("-1")
else:
    c = i / (k - j)
    c = c + 1
    print(int(c))