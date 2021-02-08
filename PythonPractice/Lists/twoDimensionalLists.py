matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][2]) #prints 3

#can rewrite values too
matrix[0][2] = 20
print(matrix)
print()

#can print pretty arrays with numpy
import numpy as np
print(np.matrix(matrix))

#iterating matrices

for row in matrix:
    for item in row:
        print(item)