import numpy as np
import math

# Use math.exp() to get y = e^x
x = 3
y =
print("x = %d, e^x = %d" % (x,y))

a = 0
b =
print("x = %d, e^x = %d" % (a,b))

'''
************VECTORS AND MATRICES****************
'''


'''
Note that if you
type " x = [1,2,3] "
then math.exp(x) crashes. Feel free to try this.

np.array() initializes vectors and matrices that are compatible with numpy operations
performing operations on vectors and matrices is much more computationally efficient
than operating on similarly sized lists of numbers in a for loop. This is called
VECTORIZATION, and it's very important in deep learning.

You'll have to use np.exp() instead of math.exp().
'''

#UNCOMMENT BELOW
'''
Z = np.array([1,2,3])
W =     # w = e^z
print(W)

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[1, 2, 0],
              [2, 4, 2],
              [0, 2, 1]])

#use np.matmul()
AB =
print(AB)
'''

'''
******************BROADCASTING*******************
'''
def sigmoid(x):
    return (1/(1+np.exp(-x)))
'''
BROADCASTING happens when you perform an operation
on a matrix that is typically performed
on something smaller than a matrix. Instead, the
operation happens to the matrix's components
(either a row, column, or individual entry)
on an individual basis. Example:
        [1,2,3]                 [1 + 1, 2 + 1, 3 + 1]
x =     [4,5,6]     x + 1 =     [4 + 1, 5 + 1, 6 + 1]
        [7,8,9]                 [7 + 1, 8 + 1, 9 + 1]
'''

#UNCOMMENT BELOW
'''
S = np.array([[0,1,2],  # 3x3 matrix
              [2,1,2],
              [2,1,0]])

T = np.array([-1,1,0])   # 1x3 row vector

#Grab some scratch paper! Predict what these will be!
print (s + t)
print (s * t) #note: this performs elementwise multiplication and
#              WILL NOT MULTIPLY MATRICES/VECTORS TOGETHER
print(sigmoid(t))
'''



'''
FINAL ASSIGNMENT: Calculate and print the elementwise sigmoid of TS
'''
#UNCOMMENT BELOW
'''
sigTS =
print(sigTS)
'''

'''
*********OTHER FUN THINGS FOR WHICH THERE MAY NOT BE ENOUGH TIME***********

np.sum() # sums the values of an array: can also sum a particular axis of an array
np.reshape() # reshapes an array
np.linalg.norm() # take the norm of an array
np.rand() # generate an array of random values between 0 and 1
np.randn() # random values between -1 and 1, on a normal distribution
np.tile() # construct an array from the input (which can also be an array)
'''
