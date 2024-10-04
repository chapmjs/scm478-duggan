# Overview of Lecture 4
# Here we explore lambda expressions which can be used to define functions, and see how these can be used to support vectorised operations over arrays.

# Reference: Chapter 5, David M. Beazley, Python Distilled

# (1) lambda functions

# The general for is 
# lambda args: expression, where
#  * args is a comma-separated list of arguments, and
#  * expression is an expression involving those arguments
# 
# Multiple statments or noexpression statements (e.g. try and while) cannot be used in a lambda function

f1 = lambda x,y:x+y

f1(10,20)

# (2) Higher-order functions
# Python supports teh concept of higher-order functions, which means that a function can be:
#  (1) Passed as arguments to other functions
#  (2) Placed in data structures
#  (3) Returned by a function as a result

# Functions are first-class objects, meaning there is no difference how you might handle a function
# and any other kind of data.

# Here is an example where three function are defined, and one of these is a higher-order function (process).
# It is higher-order because one of it parameters is a function. Notice that we don't have a special identifer
# for the function, it is simply treated as another variable.

def add(a,b):
   return a+b
 
def mult(a,b):
   return a * b
 
def process(a,b,f):
    return f(a,b)
  
a1 = process(1,2,add)
print(a1)

a2 = process(1,2,mult)
print(a2)


# You can also loop over a list of functions
calls = [add, mult]

x = 10
y = 20

for f in calls:
    result = f(x, y)
    print(result)
    
# (3) Iterables in Python
# An iterable is any Python object capable of returning its members one at a time, 
# permitting it to be iterated over in a for-loop.

# https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Iterables.html

# Checking to see if a function is iterable by looking for the __iter__ attribute
def check_iter(o):
    return hasattr(o, '__iter__')

a = [1, 2, 3]
print(check_iter(a))
print(sum(a))

b = range(10)
print(check_iter(b))

c = "Hello World"
print(check_iter(c))

# Functions that act on iterables:

# Here are some useful built-in functions that accept iterables as arguments:
# 
# list, tuple, dict, set: construct a list, tuple, dictionary, or set, respectively, from the contents of an iterable
# sum: sum the contents of an iterable.
# sorted: return a list of the sorted contents of an interable
# any: returns True and ends the iteration immediately if bool(item) was True for any item in the iterable.
# all: returns True only if bool(item) was True for all items in the iterable.
# max: return the largest value in an iterable.
# min: return the smallest value in an iterable.

# The function enumerate is iterable, and contains the index and contents of an iterable object 
list(enumerate(a))

# Iterables can then be used as part of a looping structure

for i in a:
    print(i)
    
for i in range(len(c)):
    print(c[i])
    
for x,y in enumerate(a):
    print(x,y)
    
    
# (4) map() function
# The map() function returns a map object (which is an iterator) of the results 
# after applying the given function to each item of a given iterable (list, tuple etc.)

# See https://www.geeksforgeeks.org/python-map-function/
# map(fun, iter) 
#  Parameters: 
#  fun:  It is a function to which map passes each element of given iterable. 
#  iter:  It is iterable which is to be mapped. 
#  NOTE:  You can pass one or more iterable to the map() function. 
# 
#  Returns:  Returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.) 
# 
# 
#  NOTE :  The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) . 
# 
def f1(x):
   return 2*x

a = list(range(10))

b0 = map(f1,a)
b1 = list(b0)

b2 = list(map(lambda x: 2*x,a))


a1 = list(range(0,10))
a2 = list(range(10,20))

a3 = list(map(lambda x,y:x+y,a1,a2))
print(a3)


# (5) The filter method
# https://www.geeksforgeeks.org/filter-in-python/
# The filter() method filters the given sequence with the help of a function that 
# tests each element in the sequence to be true or not. 

# Syntax: filter(function, sequence)
# 
# 
# Parameters:
# 
# 
# function: function that tests if each element of a sequence is true or not.
# sequence: sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators.
# Returns: an iterator that is already filtered.

a = list(range(20))
print(a)

b = list(filter(lambda x: x % 2 == 0, a))
print(b)


# (6) reduce
# https://www.geeksforgeeks.org/reduce-in-python/
# The reduce(fun,seq) function is used to apply a particular function passed in its argument 
# to all of the list elements mentioned in the sequence passed along.
# This function is defined in “functools” module.

# At first step, first two elements of sequence are picked and the result is obtained.
# Next step is to apply the same function to the previously attained result and the 
# number just succeeding the second element and the result is again stored.

import functools

# initializing list
lis = [1, 3, 5, 6, 2]

def add(a,b):
    print(a,b)
    return a+b

sum = functools.reduce(add, lis)
print(sum)

sum1 = functools.reduce(lambda a,b:a+b, lis)
print(sum1)

mx = functools.reduce(lambda a, b: a if a > b else b, lis)
print(mx)

mn = functools.reduce(lambda a, b: a if a < b else b, lis)
print(mn)

# (7) Revisiting Functions that act on iterables:
a = [0,1,2,3,4,5,6,7,8,9]

# sum: sum the contents of an iterable.
# sorted: return a list of the sorted contents of an interable
# any: returns True and ends the iteration immediately if bool(item) was True for any item in the iterable.
# all: returns True only if bool(item) was True for all items in the iterable.
# max: return the largest value in an iterable.
# min: return the smallest value in an iterable.

a = [5, 10, 15, 20]
var = sum(a)
print(var)



# Examples - 

# (1) Using map to get the square of a list of numbers

x1 = list(range(-100,100))

y = list(map(lambda x:x**2, x1))

import matplotlib.pyplot as plt
plt.plot(x1,y)

# (2) Filtering all lowercase vowels from a string
s = "HellO World"

# Note the use of the in operator, useful to detect the presence of an element within a list

s1 = list(filter(lambda x:x in ['a','e','i','o','u'], s))
print(s1)

# Challenges
















    


