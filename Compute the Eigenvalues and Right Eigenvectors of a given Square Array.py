# eigendecomposition
from numpy import array
from numpy.linalg import eig

# define matrix
A = array([[1  , 4], [3, 2]])
print(A)
# factorize

values, vectors = eig(A)
print(values)
print(vectors)


'''
Harder way to solve Eigen values and Vectors (Start not complete)

# identity matrix
from numpy import identity
I = identity(3)
print(I)

#matrix determinant
from numpy import array
from numpy.linalg import det
# define matrix
A = array([
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
print(A)
# calculate determinant
B = det(A)
print(B)



# calculate determinant

expr = det(A-x@I)

B = solve(expr, dict = True)

C = np.linalg.solve(det(A-x@I))


print(B)

print(C)
'''
