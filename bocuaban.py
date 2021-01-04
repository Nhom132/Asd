import numpy as np
n = int(input('Nhap n vao: '))
def baitap(n):
    A = np.random.randint(100, size=(n, n))
    print('Ma tran random cap n dinh thuc khac 0')
    while np.linalg.det(A) == 0:
        A = np.random.randint(10, size=(n, n))
    return A
print(baitap(n))