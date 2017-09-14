# standard 'hello world'
print('hello world!')


# variable assignment
a = 1
print(a)


# arithmetic
a = a + 1
print(a)


# increment
a += 1
print(a)


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
    return (a * b, a / b)

product, quotient = product_and_quotient(6, 3)
print((product, quotient))
