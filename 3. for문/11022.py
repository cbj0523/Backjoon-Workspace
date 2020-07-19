count = int(input())

sums = []
alpha = []
beta = []

for i in range(count):
    a, b = map(int, input().split())
    sums.append(a+b)
    alpha.append(a)
    beta.append(b)
for i in range(count):
    print("Case #{}: {} + {} = {}".format(i + 1, alpha[i], beta[i], sums[i]))