import numpy as np
# mixed discriminant calculator for 4 x 4 matrices

I = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
A = [[1, -1, 2, 0], [-1, 4, -1, 1], [2, -1, 6, -2], [0, 1, -2, 4]]
C = [[1, 0, 0, 0], [0, 0, -60, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
def D(X, Y, Z, W):
    A = np.array(X)
    B = np.array(Y)
    C = np.array(Z)
    D = np.array(W)
    return det(A + B + C + D) - det (A + B + C) - det (A + B + D) - det (A + C + D) - det (B + C + D) + det(A + B) + det (A + C) + det(A + D) + det(B + C) + det (B + D) + det(C + D) - det (A) - det (B) - det (C) - det (D)

def copy_matrix(A):
    ans = [[A[i][j] for j in range(len(A))] for i in range(len(A))]
    return ans

def det(A, total=0):
    indices = list(range(len(A)))
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
    for fc in indices:
        As = copy_matrix(A)
        As = As[1:]
        height = len(As)
 
        for i in range(height): 
            As[i] = As[i][0:fc] + As[i][fc+1:] 
 
        sign = (-1) ** (fc % 2)
        sub_det = det(As)
        total += sign * A[0][fc] * sub_det 
    return total

print(D(A, I, C, C)**2 - D(A, I, I, C) * D(A, C, C, C))
print(C)

# D(A, I, C, C)^2 >= D(A, I, I, C) D(A, C, C, C)