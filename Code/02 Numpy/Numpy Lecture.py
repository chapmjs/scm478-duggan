# Based on chapter 4, Wes McKinney
# NumPy Basics: Arrays and Vectorised Computation

import numpy as np

# One of the key features of NumPy is its N-dimesnional array object, or ndarray, which is a 
# fast and flexible container for large datasets in Python


### (1) Exploring a one-dimensional numpy array
# Create a 1-D array
list = [1,2,3,4,5]
data = np.array(list)

# Show some array attributes
data.dtype
data.shape

# Arithmetic with arrays, note the vectorisation property
data * 2

data + 10

data + data

data - data

data ** 2

# Slicing an array

# From index 0 up to (not including) index 2
data[0:2]

# Set all array elements to 99
data[:] = 99

# Back to the original
data = np.array(range(5))

# Creating a slice variable is a "view"

d = data[0:2]
print(data)
d[:] = -1
print(data)


### (2) Boolean indexing (powerful feature)

data = np.array(range(2,12))

ans = data % 2 == 0

print(ans)

n_data = data[ans]
print(n_data)


### (3) Useful array creation functions

# All zeros
np.zeros(10)

# Empty values
np.empty(10)

# Set to a sequence
np.arange(10)
np.arange(2,8)

# All ones
np.ones(10)

# Initialised to a specific value
np.full(10,1000)


# Identity matrix (note 3x3 produced)
np.eye(3)

# 11 points (inclusive between a lower an upper value)
np.linspace(0, 1, 11)

# Create a matrix of zeros but with a specified diagonal
np.diag(range(10))




# (4) using random number generation (NumPy) to initialise arrays
# https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.integers.html

#  No seed
rng = np.random.default_rng(200)

dice1 = rng.integers(1, 7, 10,dtype='int8')
print(dice1)
# We can use boolean indexing to count the number of 6s
#  USe ?np.random.randint for help.

c = sum(dice1 == 6)
print(c)

# In 2 dimensions
dice2 = rng.integers(1, 7,(3,3))


# (5) NumPy data types
import sys

i8  = np.zeros(10,dtype='int8')
print(sys.getsizeof(i8))

ui8 = np.zeros(10,dtype='uint8')
print(sys.getsizeof(ui8))

i16 = np.zeros(10,dtype='int16')
print(sys.getsizeof(i16))

ui16 = np.zeros(10,dtype='uint16')
print(sys.getsizeof(ui16))

i64 = np.zeros(10,dtype='int64')
print(sys.getsizeof(i64))

ui64 = np.zeros(10,dtype='uint64')
print(sys.getsizeof(ui64))

f16 = np.zeros(10,dtype='float16')
print(sys.getsizeof(f16))

f32 = np.zeros(10,dtype='float32')
print(sys.getsizeof(f32))

f64 = np.zeros(10,dtype='float64')
print(sys.getsizeof(f64))

fb = np.zeros(10,dtype='bool')
print(sys.getsizeof(fb))


# (6) Two dimensional arrays


l1 = [[1, 2, 3],   [4, 5, 6],   [7, 8, 9]]  

d2 = np.array(l)

# Iteration

num_rows, num_cols = d2.shape
print(num_rows,num_cols)

# show entire rows
for i in range(num_rows):
  print(d2[i])

#  Show cells
for i in range(num_rows):
  for j in range(num_cols):
    print(i,j)

#  enumerate 
for (x,y), value in np.ndenumerate(d2):
  print (x,y)

# Reshaping an array

d_rs1 = np.arange(12).reshape(3,4)
print(d_rs1)

d_rs2 = d_rs1.reshape(4,3)
print(d_rs2)

d_rs3 = d_rs1.reshape(12,1)
print(d_rs3)

d_rs4 = d_rs1.reshape(1,12)
print(d_rs4)

# Multiplication

# Element wise
l2 = np.eye(3)  
m1 = d2 * l2
print(m1)

# Matrix algebra
m2 = np.matmul(d2, l2)

print(m2)

# Use infix operator @ for matrix multiplication
m3 = d2 @ l2
print(m3)

# Two dimensional array slicing
l2 = [[10, 20, 30],   [40, 50, 60],   [70, 80, 90]]  

arr1 = np.array(l2)

a1 = arr1[:2,1:] # Row (0,2], column (1,end)
print(a1)
print(a1.shape)


a2_1 = arr1[2] # Third row
print(a2_1)
print(a2_1.shape)

a2_2 = arr1[2,:] # Row 2, all columns
print(a2_2)
print(a2_2.shape)

a2_3 = arr1[2:,:] # Row 2 until end, all columns
print(a2_3)
print(a2_3.shape)

a3 = arr1[:,:2] # All rows, up until column 2
print(a3)
print(a3.shape)

a4_1 = arr1[1,:2] # Second row, up to 3rd column
print(a4_1)
print(a4_1.shape)

a4_2 = arr1[1:2,:2] # Second row up until 3rd, up to 3rd column
print(a4_2)
print(a4_2.shape)



# Selective setting of elements
l3 = [[100, 200, 300],   [400, 500, 600],   [700, 800, 900]]  

arr2 = np.array(l3)
print(arr2)

arr2[arr2==100] = 0
print(arr2)

arr2[arr2> 600] = -99
print(arr2)

arr2[1] = 0
print(arr2)

arr2[0,1:2] = 40
print(arr2)

# Adding columns to an array

a1 = np.arange(12).reshape(4,3)

c_new = np.arange(4).reshape(4,1)

a2 = np.append(a1,c_new,axis=1)
a21 = np.concatenate((a1,c_new,c_new),axis=1)

r_new = np.zeros((1,4))

a2 = np.append(a2,r_new,axis=0)


# Finding indexes


l4 = [[1000, 2000, 3000],   [3000, 5000, 6000],   [7000, 8000, 3000]]  

arr4 = np.array(l4)

c1 = arr4 == 3000
print(c1)

locs1 = np.where(arr4==3000)
print(locs1)

locs2 = np.where(arr4==1000)
print(locs2)

locs3 = np.where(arr4==np.min(arr4))
print(locs3)

locs4 = np.where(arr4==np.max(arr4))
print(locs4)

# Student grading example

#  Instantiate a default random number generator
# https://realpython.com/numpy-random-normal/#how-to-use-numpy-to-generate-normally-distributed-random-numbers
rng = np.random.default_rng(200)

cx_100 = np.array(rng.normal(50, 10, size=(10,1)))
cx_101 = np.array(rng.normal(60, 5, size=(10,1)))
cx_102 = np.array(rng.normal(70, 1, size=(10,1)))
cx_103 = np.array(rng.normal(40, 10, size=(10,1)))
cx_104 = np.array(rng.normal(80, 3, size=(10,1)))

grades = np.concatenate((cx_100,cx_101,cx_102,cx_103,cx_104),axis=1)

# Analyse the grades - using a loop
max_grade  = np.zeros((10,1))
min_grade  = np.zeros((10,1))
mean_grade = np.zeros((10,1))
sd_grade   = np.zeros((10,1))

# Note the methods on an numpy object
# Use dir(grades) to see full list

# Iterate on a row by row basis to get
# the scores for 
for i in range(grades.shape[0]):
    max_grade[i] = np.max(grades[i])
    min_grade[i] = np.min(grades[i])
    mean_grade[i] = np.mean(grades[i])
    sd_grade[i] = np.std(grades[i])
    
# Add the columns to the original array
grades2 = np.concatenate((grades,max_grade,min_grade,mean_grade, sd_grade),axis=1)

np.set_printoptions(precision=0)

grades2
    
    
# Use the np functions on the entire array, with the axis = 1 argument
# Note that no loops were used.

max_grade1  = np.max(grades,axis=1).reshape(10,1)
min_grade1  = np.min(grades,axis=1).reshape(10,1)
mean_grade1 = np.mean(grades,axis=1).reshape(10,1)
std_grade1  = np.std(grades,axis=1).reshape(10,1)

grades3 = np.concatenate((grades,max_grade1,min_grade1,mean_grade1,std_grade1),axis=1)
grades3 = np.round(grades3)


# Setup indices for querying
# These are numpy arrays, and we can use np.where() to find the relevant index
s_list = ['S001',
          'S002',
          'S003',
          'S004', 
          'S005',
          'S006',
          'S007',
          'S008',
          'S009',
          'S010']
          
students = np.array(s_list)

m_list = ['CX_100',
          'CX_101',
          'CX_102',
          'CX_103', 
          'CX_104']
          
modules = np.array(m_list)
          
grades[np.where(students=='S002'),:]

grades[np.where(students=='S010'),np.where(modules=='CX_104')]

    
    

    















     









