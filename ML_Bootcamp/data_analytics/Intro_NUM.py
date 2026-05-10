import numpy as np
# lesson 1
#--------------------------------------------------------------------------------
'''
my_list = [1,2,3]

print np.array(my_list)

my_mat = [[1,2,3], [4,5,6], [7,8,9]]

print my_mat
print np.array(my_mat)

#np.array() converts the list into a matrix

print np.arange(0,10)

# arange function which similar to range function in for loops
# gives all the numbers in the given range

print np.arange(0,10,2)

# gives all the even numbers gives the every 2 number

print np.zeros(5)

# zeros function generates number of zeros

print np.zeros((5,4))

# the tuple acts as the dimension of the zero matrices

print np.ones((7,8))

# gives all ones 

print np.linspace(0,25,27)

# gives EVENLY PLAced number of integers in the given range 

print np.eye(4)

# gives and identity matrix this is crazy python is out of the world

print np.random.rand(3,2)

print np.random.randn(2,4)

# given the matrix generates random numbers form 0 to 1

print np.random.randint(1,100, 20)

# generates low inclusive and high exculsive
# and the third parameter number of items

arr = np.arange(25) # an array from 0 to 24
ranarr = np.random.randint(0,50,10) # generates 10 rand integers form 0 to 49

myarr = arr.reshape(5,5) # change the 1d array into an 5 X 5 array

ranarr = ranarr.reshape(2,5)

print myarr
print ranarr

# reshapes the array  into specfic dimensions

print ranarr.max()
print myarr.min()

print ranarr.argmax() # return the max value indices
# finding min and max on a matrix

print myarr.shape
print arr.dtype

# cheching the shape and date type
"""
#---------------------------------------------------------------------------------
#lesson 2
# Numpy indexing and selection
"""
arr = np.arange(0,11)
print arr
print arr[8]
print arr[1:5]
print arr[:6]
print arr[5:]
arr[0:5] = 100 # changes those indices to 100
print arr

slice_of_arr = arr[0:6]
print slice_of_arr

slice_of_arr[:] = 99
print slice_of_arr

print arr

# here we can see that when we do slice_of_arr 
# we do not make copy of the orginal
# we actually transfer the address of the orginal
# so the orginals get manipulated
# how to make a copy of an array?

arr_copy = arr[0:6].copy()
arr_copy[:] = 87
print arr_copy
print arr

# wuth this method the orginal is not effected

arr_2d = np.array([[5,20,14], [6,4,8], [5,2,1]])
print arr_2d
print arr_2d[2,1]

#2d array

print  arr_2d[:2, 1:]

# getting a sub matrix from a orginal matrix
"""
"""
--        --
| 3  4  5  |   arr[:2]
| 7  2  1  |	grab elemnts  from rows 0 all the way to 1
| 8  2  4  |	result : --   --
--        --			 |3 4 5 |
						 |7 2 1	|
						 --    --
				arr [:, 1:]
					result : --   --
							 | 4 5 |
							 | 2 1 |
							 | 2 4 |
							 --   --

				arr [:2, 1:]
					result : --   --
							 | 4 5 |
							 | 2 1 |
							 --   --				

""" 
"""
arr = np.arange(1,11)

print arr > 5

# prints boolean values true for all the values greater than 5 otherwise false

bool_arr = arr > 5
print arr[bool_arr]

print arr [arr < 7]

# prints all the numbers to be true

arr_2d = np.arange(50).reshape(10,5)

print arr_2d
print arr_2d[5:7, 2:4]

# practice sub matrices

"""
#--------------------------------------------------------------------------------------
# lesson 3
# NumPy Operations
"""
arr = np.arange(0,11)
print arr + arr
print arr*2
print arr[1:] / arr[1:]
print arr % 4
print arr**3
print arr + 288
print arr / arr
print 1 / arr # numpy just gives a warning when we try to to 1/0
# Basic arthematic operations on arrays

arr = arr**2
print  np.sqrt(arr)
print np.tan(arr) # trignometric functions
print np.log(arr)

# universal array functions
"""
#-------------------------------------------------------------------------------------
# Practice problems
"""
print np.zeros(10)
# create an arrays of 10 zeros

print np.ones(10)
# create an array of 10 ones

print np.ones(10) * 5
# create an array of ten fives

print np.arange(10,51)
# create an array of integers from 10 to 50

print np.arange(10, 51, 2)
# same array with only even integers

print np.arange(0,9).reshape(3,3)
# create a 3 X 3 matrix from values 0 to 8

print np.eye(3)
# create an 3 X 3 identity matrix

print np.random.rand(1)
# genarate a random number in between 0 to 1

print np.random.randn(25)
# random samples of 25 numbers

print np.arange(1,101).reshape(10,10)/100
# create an 10 X 10 matrinx numbers from 0.01 to 1

print np.linspace(0.01,1,100).reshape(10,10)
#another way

print np.linspace(0,1,20)
# creat an 20 equally spaced array

mat = np.arange(1,26).reshape(5,5)

print mat[2:3, 1:5]
# NumPy indexing and selection

print np.sum(mat)
# getiing the sum of all elements in the matrix

print np.std(mat)
# getting standard deviation for mat

print mat.sum(axis = 0)
# to sum all the columns
"""
#------------------------------------------------------------------------------------------------

'''