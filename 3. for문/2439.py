lines = int(input())

count = lines - (lines - 1)

for i in range(lines, 0, -1):
    print(" "*(i-1), end="")
    print("*"*count)     
    count+=1