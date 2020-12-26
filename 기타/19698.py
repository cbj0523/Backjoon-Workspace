import math

N, W, H, L = list(map(int, input().split()))

area = W * H

mW = math.trunc(W / L)
mH = math.trunc(H / L)

if mW * mH >= N:
    print(N)
else:
    print(mW * mH)