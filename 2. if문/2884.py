h, m = input().split()

h = int(h)
m = int(m)

if m < 45 and h > 0:
    m = (m + 60) - 45
    h -= 1
elif m < 45 and h == 0:
    m = (m + 60) - 45
    h = (h + 24) - 1
else:
    m -= 45
    
print(h, m)
