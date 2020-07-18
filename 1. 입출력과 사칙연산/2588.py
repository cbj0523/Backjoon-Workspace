A = int(input())
B = input()

Bnum = list(map(int, list(B)))

third = A * Bnum[2]
fourth = A * Bnum[1]
fifth = A * Bnum[0]

print(third)
print(fourth)
print(fifth)

print("{}".format(A * int(B)))
