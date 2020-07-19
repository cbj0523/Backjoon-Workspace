count = int(input())

sums = []

for i in range(count):
    a, b = map(int, input().split())
    sums.append(a+b)
for i in range(count):
    print("Case #{}: {}".format(i+1, sums[i]))