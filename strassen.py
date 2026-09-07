# ◈ 260907:0623

import time
import random

def add(X, Y):
    n = len(X)
    return [[X[i][j] + Y[i][j] for j in range(n)] for i in range(n)]

def sub(X, Y):
    n = len(X)
    return [[X[i][j] - Y[i][j] for j in range(n)] for i in range(n)]

def strassen(X, Y):
    n = len(X)

    if n <= 2:
        if n == 1:
            return [[X[0][0] * Y[0][0]]]
        return [
            [X[0][0] * Y[0][0] + X[0][1] * Y[1][0], X[0][0] * Y[0][1] + X[0][1] * Y[1][1]],
            [X[1][0] * Y[0][0] + X[1][1] * Y[1][0], X[1][0] * Y[0][1] + X[1][1] * Y[1][1]]
        ]

    mid = n // 2

    A11 = [row[:mid] for row in X[:mid]]
    A12 = [row[mid:] for row in X[:mid]]
    A21 = [row[:mid] for row in X[mid:]]
    A22 = [row[mid:] for row in X[mid:]]

    B11 = [row[:mid] for row in Y[:mid]]
    B12 = [row[mid:] for row in Y[:mid]]
    B21 = [row[:mid] for row in Y[mid:]]
    B22 = [row[mid:] for row in Y[mid:]]

    P = strassen(add(A11, A22), add(B11, B22))
    Q = strassen(add(A21, A22), B11)
    R = strassen(A11, sub(B12, B22))
    S = strassen(A22, sub(B21, B11))
    T = strassen(add(A11, A12), B22)
    U = strassen(sub(A21, A11), add(B11, B12))
    V = strassen(sub(A12, A22), add(B21, B22))

    C11 = add(sub(add(P, S), T), V)
    C12 = add(R, T)
    C21 = add(Q, S)
    C22 = add(sub(add(P, R), Q), U)

    C = []

    for i in range(mid):
        C.append(C11[i] + C12[i])

    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C

def normal_multiply(X, Y):
    n = len(X)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += X[i][k] * Y[k][j]
    return C

sizes = [32, 64, 128, 256]

# Print the table header
print(f"{'Size (n x n)':<15} | {'Normal Mult (s)':<18} | {'Strassen (s)':<18}")
print("-" * 57)

# Benchmark loop
for n in sizes:
    # Generate random n x n matrices with single-digit integers
    A = [[random.randint(1, 9) for _ in range(n)] for _ in range(n)]
    B = [[random.randint(1, 9) for _ in range(n)] for _ in range(n)]
    
    # Time Normal Multiplication
    start = time.perf_counter()
    normal_multiply(A, B)
    normal_time = time.perf_counter() - start
    
    # Time Strassen's Algorithm
    start = time.perf_counter()
    strassen(A, B)
    strassen_time = time.perf_counter() - start
    
    print(f"{n:<15} | {normal_time:<18.6f} | {strassen_time:<18.6f}")