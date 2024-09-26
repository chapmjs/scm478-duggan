# Overview of code for lecture 1
# Examples based on Wes McKinney text book, "Python for Data Analysis", Chapter 2.

# Use indentation instead of braces (usually 4 spaces)
for i in range(0, 5):
    print(i)
    
x = -1
if x < 0:
    print("Negative...")
else:
    print("Positive")
    
# Comments using the # sign.

# Semicolon not needed to end statement, but can be useful for multiple statements on
# one line

x = 10; y = 40; z = x+y
print(x,y,z)


### variables, assigned using = and are allocated a new area in memory
x = 400
print(id(x))

y = x
print(id(y))

y is x

### Scalar types: single value variables

# (1) None - the Python "null" value
a = None

# (2) str, string type, can hold Unicode strings. Strings are immutable
h = "Hello"

# For multiple lines, use triple quotes
z = """
This spans
More than
One line
"""

print(z)

# Show how you can call a method from the str object.
print(h.upper())

# Show all methods for an Python object
dir(h)


# (3) float, double precision floating point number
x = 3.11132

# (4) bool, boolean value, True or False
b = True
x = 10
c = x == 10

# (5) int, arbitrary precision integer
y = 100
type(y)


### Binary operations

a = 10; b = 5
a + b           # add a and b
a - b           # subtract a and b
a * b           # multiply a and b
a / b           # divide a by b
a // b          # floor divide a by b
a ** b          # raise a to the power of b
a & b           # True if both a and b are true
a | b           # True if either of a and b are true
a == b          # True if a equals b
a != b          # True if a is not equal to b
a < b, a <= b   # True if a less than, less than or equal to b
a > b, a >= b   # True if a greater than, greater than or equal to b
a is b          # True if a and b reference the same python object
a is not b      # True if a and b reference different python objects

### range() function
# range() function generates the  numbers starting from the given start integer (inclusive)
# to the stop integer (exclusive)

r = range(10)

for i in r:
    print(i)

# Can vary start
r = range(1,3)

for i in r:
    print(i)
    
    r = range(10)

# Can control steps
r = range(0,10,2)
for i in r:
    print(i)


### enumerate function - can manipulate index and value within a loop
r = range(4,12,2)

for index, value in enumerate(r):
    print(index,value)

### Writing functions
# A block of code which only runs when it is called. Can return an value
def add_numbers(x,y):
    return (x+y)
  
add_numbers(10,20)
  
# adding default value  
def add_numbers1(x,y=2):
    return x+y
  
add_numbers1(100)
add_numbers1(100,200)
  
# Return more than one value  
def process_numbers(x,y):
    return x+y,x-y
  
process_numbers(100,200)
  
### Python List type (similar to a one-dimesional array)
# Create a list (square brackets)
l = [1,2,3,4,5]

# Create a list with the list constructor (double brackets)
l = list((1,2,3,4,5))

# Create a list with the list constructor and range function
l = list(range(0,10))

# Slice a list (from, to - excludes to)
l[0:3]
l[:3]
l[3:]

# Change elements
l[1:3] = [99,99]

# Show methods on list l
dir(l)
l.__len__()
l.reverse()
x = l.pop()

l.insert(0,1000)

### List comprehension - form a new list by filtering elements of a collection and transforming
# [expr for value in collection]

l = [v*2 for v in range(10)]

l1 = [v*0 for v in range(10)]

### Random numbers
import random as r
n = r.randint(1,6)


### Example... throw two dice 100 times and sum the results. Use a function to sum
# Create a List of random numbers (dice throws)
dice1 = [r.randint(1,6) for _ in range(10)]
dice2 = [r.randint(1,6) for _ in range(10)]

# _ represents a temporary or throwaway variable



def add_arrays(d1, d2):
    sum_d = [0 for _ in range(d1.__len__())]
    for index, value in enumerate(sum_d):
        sum_d[index] = d1[index]+d2[index]
        
    return sum_d
  
dice3 = add_arrays(dice1, dice2)
  
  
# Note, we will start to use NumPy instead of lists when processing data.  

### Challenge Write a function that will return the frequency of throws for each combination







