# for 반복문 풀이

a = int(input())

tmp = 0

for i in range(a):
    tmp += (i+1)
    
print(tmp)

# 공식 풀이 (1부터 n까지의 자연수의 합은 n * (n+1) / 2 이다.)

# sum = int(a * (a+1) / 2)
# print(sum)