import numpy as np
from scipy import linalg
from numpy import array


'''
Found code online:

link: https://stackoverflow.com/questions/
3819500/code-to-solve-determinant-using-python-without-using-scipy-linalg-det

'''
def determinant(a):
    assert len(a.shape) == 2 # check if a is a two diamentional matrix
    assert a.shape[0] == a.shape[1] # check if matrix is square
    n = a.shape[0]
   
    for k in range(0, n-1):
       
        for i in range(k+1, n):
            if a[i,k] != 0.0:
                lam = a [i,k]/a[k,k]
                a[i,k:n] = a[i,k:n] - lam*a[k,k:n]

               
    # the matrix (a) is now in the upper triangular form
                
    return np.prod(np.diag(a))

matrix = array([
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])

print(determinant(matrix))
