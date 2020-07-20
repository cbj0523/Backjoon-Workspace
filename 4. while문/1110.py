count = 0
N = int(input())
if N < 10:
    N = N * 10
new = N
while True:    
    count += 1
    if new >= 10:
        letter = list(map(int, list(str(new))))
        A = letter[0] + letter[1]
        if A >= 10:
            A = list(map(int, list(str(A))))[1]
        new = A + (letter[1] * 10)
        if new == N:
            break
    else:
        new = new * 10 + new
        if new == N:
            break
    
print(count)