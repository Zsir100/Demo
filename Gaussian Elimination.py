import numpy as np
def gauss(A, b):
    #函数输入参数与返回值均为ndarray对象
    A=A.astype('float64')
    b=b.astype('float64')
    n = len(b)
    # 消元
    for i in range(n):
        for j in range(i+1, n):
            if A[j][i] != 0:
                lam = A[j][i] / A[i][i]
                A[j][i:] -= lam * A[i][i:]
                b[j] -= lam * b[i]
    # 回代
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i]-A[i][i+1:]@x[i+1:])/A[i,i]
    return x

A = np.array([[6,2,1],[1,3,2],[2,4,1]])
b = np.array([6, 2, 0])
s = gauss(A, b)
print(s)