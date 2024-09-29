#!/usr/bin/env python
"""Mapper para la matriz de momentos aumentada"""
import numpy as np

if __name__ == "__main__":
    D = np.genfromtxt('matrix_input.txt')
    # Splits the matrix D into 2 partitions.
    split = np.array_split(D, 2)
    for i, d in enumerate(split):
        np.savetxt(f'D_{i+1}.txt', d, fmt='%d', delimiter='\t')
