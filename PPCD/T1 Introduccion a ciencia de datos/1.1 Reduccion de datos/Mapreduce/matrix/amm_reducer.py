"""Reducer para la matriz de momentos aumentada"""
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
    for i in range(X.shape[0]):
        A += w[i].reshape(-1,1) @ w[i].reshape(1,-1)
    return A

if __name__ == "__main__":
    D1 = np.genfromtxt('D_1.txt')
    D2 = np.genfromtxt('D_2.txt')
    A = augmented_moment_matrix(D1) + augmented_moment_matrix(D2)
    np.savetxt('matrix_output.txt', A, fmt='%d', delimiter='\t')
