import numpy as np


A = np.array([[3, -9], [2, 4]])
print(A)

B = np.array([4, 9])

Z = np.linalg.solve(A, B)

print(Z)
