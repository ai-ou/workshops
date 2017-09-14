import numpy as np
import math

'''
 Use math.exp() to get y = e^x
'''

x = 3
y = math.exp(x)
print("x = %d, e^x = %d" % (x,y))

x = 0
y = math.exp(x)
print("x = %d, e^x = %d" % (x,y))

'''
Note that if
x = [1,2,3]
then math.exp(x) crashes. Feel free to try this.
'''
