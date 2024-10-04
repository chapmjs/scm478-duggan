# Functions are a core building block of most Python programmes. The can be 
# veiwed as "mini-programs" that accept inputs, process the inputs, and return results.

# Functions are the glue by which a system is put together and teh basic mechanism of moving data around.

# Reference: Chapter 5, David M. Beazley, Python Distilled


# *** (1) Function definitions
# Functions are define with the def statement
#   

# The general form is

# def fname(p1, p2, ..., pn):
#    statements
   
# Where:
#   * fname is the function name
#   * p1, p2, ..., pn are an arbitrary number of parameters
#   * statements are valid Python statements
#   * The return statement is used to return values from a function.


# Here is a simple function that adds two numbers and returns the sum.

def add(x,y):
    return x + y
  
# The first part of the function definition specifies the function name and 
# parameter names.

# Here, we name the function "add" and specify that it can accept two parameters, x and y
# The colon operator signals the start of the function body, which must be indented.

# Here, the function body returns a single value, which is the addition of the two input values


ans = add(1,2)
print(ans)

# We now call the function with arguments, and these are copied to the variables by position.
# The order and number of arguments must match the parameters provided in the function definition.


# (2) *** Default arguments
# You can attach default values to parameters by assigning values within the function definition.
# This reduces the number of arguments you are required to pass to the function

def add(x,y=100):
    return x + y
  
  
ans = add(1)
print(ans)

# (2) *** Keyword arguments
# The examples we have seen so far pass arguments by their position.
# Python also allows you to name each parameter in teh call and specify the value

def subtract(x,y):
    return x-y
  
m1 = subtract(10,20)
print(m1)

m2 = subtract(y=20,x=10)
print(m2)

# Positional and keyword arguments can appear in the same function call, 
# provided that all teh positional arguments appesr first

# It is possible to force the use of keyword arguments, by using * 
# in the definition. Parameters after * must be called via keyword
# arguments.

def multiply(x,*,y):
    return x-y
  
m3 = multiply(10,20) # Generates an error
m3 = multiply(10,y=20)
print(m3)


# (3) *** Positional arguments
# Many of Python's in-built functions only accept arguments by position.
# This can be enforced by adding a slash at the end of the parameter list

def divide(x,y,/):
    return x/y
  
m4 = divide(10,y=2) # Generates an error
m4 = divide(10,2) # OK
print(m4)


# (4) *** Function parameter passing
# When a function is called, the function parameters are local names that get bound to
# the passed input arguments
# Care is required if mutatble objects such as lists or numpy arrays are passed, as changes
# to these are reflected in the original object.
# This is known as a "side-effect" of a function call.

import numpy as np

def check_array(a):
   a[a==0] = -99
   return None
 
a_test = np.eye(3)
print(a_test)
check_array(a_test)
print(a_test)


def check_array_copy(a):
   b = np.copy(a) # b is a copy of a (new object)
   a[b==0] = -99 # This will still cause a side effect
   return b
 
a_test = np.eye(3)
print(a_test)
b = check_array_copy(a_test)
print(a_test)
print(b)

# (5) *** Function scoping rules
# Each time a function executes, a local namespace is created. The namespace is
# an environment that contains the names and values of the functon parameters as 
# well as all variables that are assigned inside the functon body

# All other names that are used but not assigned in the function body (the free variables)
# are dynamically found in the global namespace (enclosing module)

# Functions can inspect their execution environment using the built-in function
# locals()

def f(a,b):
    y = a + b
    locs = locals()
    print(type(locs),locs)

ans = f(1,2)


# A function can obtain its own stack frame using inspect.currentframe()
# 

# Frame attributes (p133 Beazley)
#   Attribute         Description
#   f.f_back          Previous stack frame (toward the caller)
#   f.f_code          Code object being evaluated
#   f.f_locals        Dictionary of local variables (locals())
#   f.f_globals       Dictionary used for global variables (globals())
#   f.f_builtins      Dictionary used for built-in names
#   f.f_lineno        Line number
#   f.f_lasti         Current instruction
#   f.f_trace         Function called at the start of each source code line

import inspect

def g(a,b):
    y = a - b
    f = inspect.currentframe()
    print(type(f),f)
    print(f.f_locals)
    print(f.f_globals)
    print(f.f_lineno)
    print(f.f_back)

ans = g(1,2)

    
# (6) *** Example
# Write a function that filters a 1D numpy array and returns only those values that are even
# Make sure that the new variable returned in a copy in its own right. You can
# check this using the id() function
# Return the value a one-dimensional array

# Solution  1: with loops
def get_even_1(a):
    ev = np.array([]) # Create an empty list
    # Loop through the input array
    for i in range(a.size):
        if(a[i] % 2 == 0):
            ev = np.append(ev,a[i]) # grow the list
    
    return ev
  
  
def get_even_2(a):
# Selecting data from an array by boolean indexing always creates a copy of the data, 
# even if the returned array is unchanged.
# https://www.oreilly.com/library/view/python-for-data/9781449323592/ch04.html
    ev = a[a % 2 == 0]
    print("Check variable locations in memory")
    print("a",id(a),"ev",id(ev))
    return ev  
  
rng = np.random.default_rng(200)
sample1 = rng.integers(1, 100, 20)

evens1 = get_even_1(sample1)
print(sample1)
print(evens1)


evens2 = get_even_2(sample1)
print(sample1)
print(evens2)
evens2 = evens2 *2
print(evens2)
print(sample1)


# (7) Challenges

# Challenge 3.1
# Write a function (swap) that takes:
# A two dimensional numpy array (m)
# A target value (t)
# A replacement value (r), and
# Replaces all occurrences of t in m with the value r
# Write two versions, one with a loop, the other vectorised
# The results must be a new variable, and check for this in the function code.

# Challenge 3.2
# Write a function called summarise that:
# * Takes in a 2-D array
# * Create a copy
# * Calculates the sum of all the columns
# * Adds this to a new row at the end of the array
# * Returns the nw array.


# Challenge 3.3
# Write a function called validate that:
# * Takes in a 2-D array
# * Replaces all Negative values with the Type None
# * Performs this action on the original array.


   
   










