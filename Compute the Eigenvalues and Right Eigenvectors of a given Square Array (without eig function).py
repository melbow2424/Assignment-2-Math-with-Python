import sympy as sy
from sympy import *
import numpy as np
from sympy import Array
from numpy import array
from numpy import identity

#Solving Eigenvalues

lamda = symbols('lamda')
A = Matrix([[2  , -4], [-1, -1]])

'''
print(A.dtype)
No data type for Matrix get error
AttributeError: 'MutableDenseMatrix' object has no attribute 'dtype'

This is the main reason why I can not use the np.linalg.solve()function.
The np.linalg.solve() function needs a float data type like an array has.  

Try to fix by changing Matrix to an array then I get this error:
AttributeError: 'numpy.ndarray' object has no attribute 'charpoly'

Although charpoly is not an attribute of numpy.
It is an attribute of sympy

'''
e = A.charpoly(lamda)

eigen_values = solve(e ,lamda)

print('Eigenvalues: ')
print(eigen_values)

I = identity(2)

#Solving Eigenvectors

y_values = []
for x in eigen_values:
    equ = A - x*I
    row_reduce = equ.rref()
    #b = Matrix([0, 0])
    #C = np.linalg.solve(equ,b)
    y_values.append(row_reduce)
    print(row_reduce)

'''

Only solved the row reduced form of matrices from Eigenvalues.
The np.linalg.solve() function would have solved for Eigenvectors but because my Matrix has no float data type,
the function could not solve. 

'''
