def multiplication(a, b):
    result = []
    for i in range(len(a)):
        temp1 = 0
        for j in range(len(b)):
            temp1 += a[i][j] * b[j]
        result.append(temp1)
    print(result)
        
A = [ [1, 2], [3, 4], [5, 6] ]
B = [ 2, 3 ]

multiplication(A, B)