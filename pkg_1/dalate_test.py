import numpy as np

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(arr)
arr = np.delete(arr, 1, axis=0)
print(arr)

