import numpy as np
import math

# Use math.exp() to get y = e^x
x = 3
y = math.exp(x)
print("x = %d, e^x = %d") % (x,y)

x = 0
y = math.exp(x)
print("x = %d, e^x = %d") % (x,y)

'''
Note that if
x = [1,2,3]
then math.exp(x) crashes. Feel free to try this.
'''

# matrix multiplication
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[1, 2, 0],
              [2, 4, 2],
              [0, 2, 1]])

AB = np.matmul(A, B)
