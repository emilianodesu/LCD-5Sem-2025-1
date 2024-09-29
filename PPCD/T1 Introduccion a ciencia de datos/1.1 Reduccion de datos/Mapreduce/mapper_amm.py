#!/usr/bin/env python
"""Mapper para la matriz de momentos aumentada"""
import numpy as np

def augmented_moment_matrix(X: np.ndarray) -> np.ndarray:
    """
    Computes the augmented moment matrix of a dataset X.

    Parameters
    ----------
    X : numpy.ndarray
        A 2D numpy array where the rows are the samples and the columns are the features.
    
    Returns
    -------
    numpy.ndarray
        The moments matrix of X.
    """
    num_features = X.shape[1]
    A = np.zeros((num_features+1, num_features+1))
    w = np.insert(X, 0, 1, axis=1)
    for i in range(num_features):
        A += w[i].reshape(-1,1) @ w[i].reshape(1,-1)
    return A

def splitter(D: np.ndarray, r: int) -> np.ndarray:
    """
    Splits the matrix D into r partitions.

    Parameters
    ----------
    D : numpy.ndarray
        A 2D numpy array dataset.
    r : int
        The number of partitions to split D into.
    
    Returns
    -------
    numpy.ndarray
        A list of n submatrices.
    """
    return np.array_split(D, r)

if __name__ == "__main__":
    D = np.genfromtxt('matrix/matrix_input.txt')
    print(augmented_moment_matrix(D))
    split = splitter(D, 2)
    for i, X in enumerate(split):
        A = augmented_moment_matrix(X)
        np.savetxt(f'matrix/d{i+1}.txt', A, fmt='%d', delimiter='\t')
    
