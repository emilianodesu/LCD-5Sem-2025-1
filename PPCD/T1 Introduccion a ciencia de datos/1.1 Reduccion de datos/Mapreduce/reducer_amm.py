"""Reducer para la matriz de momentos aumentada"""
import numpy as np

if __name__ == "__main__":
    D1 = np.genfromtxt('matrix/d1.txt')
    D2 = np.genfromtxt('matrix/d2.txt')
    A = D1 + D2
    np.savetxt('matrix/matrix_output.txt', A, fmt='%d', delimiter='\t')
