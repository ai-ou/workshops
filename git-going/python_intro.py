"""
>>> print('hello world!')
hello world!
"""

# variable assignment
a = 1

# arithmetic
a = a + 1 # a + 1 = 1 + 1 = 2
a = a * 2 # a * 2 = 2 * 2 = 4
a = a * a # a * a = 4 * 4 = 16

a = a ** 2 # a = a ^ 2 | square a
a = a ** (1/2) # a = a ^ (1/2) | square root a

# increment, multiply by
a += 1 # a + 1 = 16 + 1 = 17
a *= 3 # a * 3 = 17 * 3 = 51

# string declaration
org_name = "Artificial Intelligence at Ohio University"

# list declaration
num_list = [2, 4, 5]

# for...in list
def add_nums(numbers=[1, 2, 3]):
    total = 0
    for number in numbers:
        total += number
    return total

"""
>>> add_nums(num_list)
19
"""

""" looping through a range

>>> for i in range(10):
...     print(i)
...
0
1
2
3
4
5
6
7
8
9
"""

# simple comment. text on this line after '#' will not be interpreted as code.

"""
block comment.
technically a string.
used at the start of a function or class to contain documentation.
"""

# function definition
def greet(name):
    print('hello, %s!' % name)

def greet(name):
    print('hello, ' + name + '!')

# more string formatting
def advanced_greet(first_name, last_name):
    print("hello, %s %s!" % (first_name, last_name))


# example docstring usage
def add(a, b):
    """
    adds two numbers.
    a (int) - the first number to be added.
    b (int) - the second number to be added.
    """
    return a + b


# the power of tuples
def product_and_quotient(a, b):
    return a * b, a / b

product, quotient = product_and_quotient(6, 3)


""" PROBLEM 1
Write a function cube(n) that returns n cubed.
"""

def cube(n):
    return n

print("Result for Q1, should be 8: %i" % cube(2))

""" PROBLEM 2
Write a function to compute the factorial of n.
Recursion is your friend.
"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print ("Result for Q2, should be 120: %i" % factorial(5))
