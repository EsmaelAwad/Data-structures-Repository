import numpy as np

m1 = np.array([[1,5,3,6],
               [5,9,8,4],
               [99,11,23,53]])
m2 = np.array([[2,3,4,6],
               [5,9,8,4],
               [45,36,89,88]])
m3 = np.array([[2,3,4,6],
               [5,9,8,4],
               [45,36,89,88]])
m4 = np.array([[2,3,4,6],
               [5,9,8,4],
               [45,36,89,88]])
print(f"m1 Shape is {m1.shape[0]} Rows, {m1.shape[1]} Columns\nm2 Shape is {m2.shape[0]} Rows, {m2.shape[1]} Columns")

tensor = np.array([m1,m2,m3,m4])

print("\n",tensor,"\n","\n",tensor.shape,"\n","\n",tensor.dtype)

#Transposing matricies.
m1_transposed = m1.transpose()

print(m1.shape,m1_transposed.shape)
