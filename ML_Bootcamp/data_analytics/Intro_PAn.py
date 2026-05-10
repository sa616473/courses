import numpy as np
import pandas as pd


#___________________________________________________________________________________
#lesson 1
# Series in panda
'''
labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}

print pd.Series(data = my_data)

"""
"""
--> returns this

0	10
1	20
2	30
"""
"""
print pd.Series(data=my_data, index= labels)

"""
"""
-->returns this

a 	10
b 	20
c	  30
"""
"""
print pd.Series(d)
"""
"""
--> returns this
Key		Value
a 		 10
b		   20
c		   30

"""

# a series cna hold anything objects to datatypes and functions
 
"""
# pd.series([sum,print,len])

0	fucntion built in
1	function built in 
2	function built in

"""
"""
ser1 = pd.Series([1,2,3,4], ['USA', 'Germany', 'USSR', 'Japan'])
ser2 = pd.Series([1,2,5,4], ['USA', 'Germany', 'Italy', 'Japan'])

print ser1
print ser2['Italy']
print ser1 + ser2

# we can perform arthematic operations on series just like arrays

"""
"""
"""
#____________________________________________________________________________
#lesson 2
# Data frames in panda
"""
np.random.seed(101)
df = pd.DataFrame(np.random.randn(5,4), ['a','b','c','d','e'], ['w','x','y','z'])
l = [[1,2],[2,3]]
l = np.array(l)
l = pd.DataFrame(l,['age','height'],['life', 'health'])
print l
print df
"""
"""
resut ->

        life  health
age        1       2
height     2       3
          w         x         y         z
a  2.706850  0.628133  0.907969  0.503826
b  0.651118 -0.319318 -0.848077  0.605965
c -2.018168  0.740122  0.528813 -0.589001
d  0.188695 -0.758872 -0.933237  0.955057
e  0.190794  1.978757  2.605967  0.683509

# Gives us a perfect data frame
"""
"""
print df['x']['c']
print df.x.c		# alrenative way and confusings
print df[['x','z']] # gives a part of the data frame


# to grab the items first get the column and then the row

df['new'] = df['w'] + df['x']
print df

df['new'] = [1,2,3,4,5]
print df

# adding a new cloumn to dataframe

print df.drop('x', axis = 1)

# to remove columns we use the drop method this will not change the orginal
# data in order to change the orginal data we need to set the inplace = True
# axis= 0 for rows
# axis= 1 for columns

print df.shape
# for the shape dimensions of the data frame

print df.loc['c']
print df.iloc[2]
#prints a series of the row c

print df.loc['c':'d', 'x':'y']
print df.iloc[2:4, 1:3]

# Grabing the subsets of the data frames
"""
#__________________________________________________________________________________________
# lesson 3
# DAta frames part 2
"""
          w         x         y         z
a  2.706850  0.628133  0.907969  0.503826
b  0.651118 -0.319318 -0.848077  0.605965
c -2.018168  0.740122  0.528813 -0.589001
d  0.188695 -0.758872 -0.933237  0.955057
e  0.190794  1.978757  2.605967  0.683509

# inital data frame
"""
"""
np.random.seed(101)
df = pd.DataFrame(np.random.randn(5,4), ['a','b','c','d','e'], ['w','x','y','z'])
print df

print df > 0
# this will return a data fram true for all values greater the 0
"""
"""
---> Result
       w      x      y      z
a   True   True   True   True
b   True  False  False   True
c  False   True   True  False
d   True  False  False   True
e   True   True   True   True
"""
"""
booldf = df > 0
print df[booldf] # Equvilent df[df > 0]
"""
"""
--> Result

  w         x         y         z
a  2.706850  0.628133  0.907969  0.503826
b  0.651118       NaN       NaN  0.605965
c       NaN  0.740122  0.528813       NaN
d  0.188695       NaN       NaN  0.955057
e  0.190794  1.978757  2.605967  0.683509

# retruns a data frame with NaNs and values
# NaNs are false

"""
"""
print df['w'] > 0
"""
"""
--> Result

a     True
b     True
c    False
d     True
e     True
Name: w, dtype: bool

"""
"""
print df.loc['c'] > 0

"""
"""
--> Result

w    False
x     True
y     True
z    False
Name: c, dtype: bool

"""
"""
print df.loc['c' : 'd', 'w' : 'y'] > 1
"""
"""
--> Result

       w      x      y
c  False  False  False
d  False  False  False
"""
"""
print df[df['w'] > 0]
"""
"""
--> Result

          w         x         y         z
a  2.706850  0.628133  0.907969  0.503826
b  0.651118 -0.319318 -0.848077  0.605965
d  0.188695 -0.758872 -0.933237  0.955057
e  0.190794  1.978757  2.605967  0.683509

# gets rid of the false row in the w column 

"""
"""
print df[df['z'] < 0]
"""
"""
--> result

          w         x         y         z
c -2.018168  0.740122  0.528813 -0.589001

"""
"""
print df[df['z'] < 0][['x','y']]

"""
"""
--> Result

          x         y
c  0.740122  0.528813SS

"""
"""

print df[df['w'] > 0][df[df['w'] > 0]['y'] < 0]

print df[(df['w'] > 0) & (df['y'] < 0)]

"""
"""
--> Result
          w         x         y         z
b  0.651118 -0.319318 -0.848077  0.605965
d  0.188695 -0.758872 -0.933237  0.955057
# python and works only for one for multiple conditions
# we need to use &

"""
"""
print df.reset_index()

"""
"""
--> Result
  index         w         x         y         z
0     a  2.706850  0.628133  0.907969  0.503826
1     b  0.651118 -0.319318 -0.848077  0.605965
2     c -2.018168  0.740122  0.528813 -0.589001
3     d  0.188695 -0.758872 -0.933237  0.955057
4     e  0.190794  1.978757  2.605967  0.683509

"""
"""
newindex = ['hello','world','happy','horray','hell']
df['fun'] = newindex

print df.set_index('fun', inplace = True)
print df

"""
"""
--> result

               w         x         y         z
fun                                           
hello   2.706850  0.628133  0.907969  0.503826
world   0.651118 -0.319318 -0.848077  0.605965
happy  -2.018168  0.740122  0.528813 -0.589001
horray  0.188695 -0.758872 -0.933237  0.955057
hell    0.190794  1.978757  2.605967  0.683509

"""
#_______________________________________________________________________________________
#lesson 4
# Multi Index and Index hirerachy
"""
outside = ['G1', 'G1', 'G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))

"""
"""
--> Result
[('G1', 1), ('G1', 2), ('G1', 3), ('G2', 1), ('G2', 2), ('G2', 3)]

"""
"""
hier_index = pd.MultiIndex.from_tuples(hier_index)


print hier_index

"""
"""
--> Result

MultiIndex(levels=[[u'G1', u'G2'], [1, 2, 3]], codes=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]])

"""
"""
df = pd.DataFrame(np.random.randn(6,2), hier_index,['A','B'])
print df

"""
"""
--> result

             A         B
G1 1 -0.807648  0.598966
   2  0.569462 -0.347479
   3 -0.343528  0.926892
G2 1 -1.026740  0.450313
   2 -0.845371 -0.464961
   3 -0.681891 -0.914345

"""
"""
print df.loc['G1','A'][1]

"""
"""
-> result
-1.134097264252374

"""
"""
df.index.names = ['groups', 'NUm']
print df

"""
"""
--> Result 
                   A         B
groups NUm                    
G1     1   -0.853974  0.116750
       2    0.794272 -0.972888
       3    0.370144  2.558539
G2     1    0.619690 -0.883645
       2    0.530668 -0.607246
       3   -0.102381  0.713712
"""
"""
print df.loc['G2','B'][2]


print df.xs
print df.xs(1, level = 'NUm')

"""
"""
Returns a cross section of the rows and columns of a data frame

               A         B
groups                    
G1      0.219976 -0.770112
G2     -1.431489  1.005300

"""
#_______________________________________________________________________________
#lesson 5
#Missing Data
"""
d = {'A':[1,2,np.nan], 'B' : [5,np.nan, np.nan], 'C' : [1,2,3]}

df =  pd.DataFrame(d)

print df

"""
"""
--> result

     A    B  C
0  1.0  5.0  1
1  2.0  NaN  2
2  NaN  NaN  3

"""
"""
print df.dropna()

"""
"""
--> result

   A    B  C
0  1.0  5.0  1

"""
"""
print df.dropna(axis=1)

"""
"""
--> Result

   C
0  1
1  2
2  3

"""

"""

print df.dropna(thresh = 2)

"""
"""
--> Result
     A    B  C
0  1.0  5.0  1
1  2.0  NaN  2

# Row two has 2 NaN values

"""
"""
print df.fillna(value = df .mean())

"""
"""

--> Reuslt 
Fills the empty spaces with mean of the column's value

     A    B  C
0  1.0  5.0  1
1  2.0  5.0  2
2  1.5  5.0  3

"""
#___________________________________________________________________________________
# lesson 7
# Group By

"""
data = {'Company' : ['GOOG','GOOG', 'MSFT', 'MSFT', 'FB', 'FB'], 
		'Person' : ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
		'Sales' : [200, 100, 340, 124, 243, 350]
		}
df = pd.DataFrame(data)
print df
"""
"""
--> Result

  Company   Person  Sales
0    GOOG      Sam    200
1    GOOG  Charlie    100
2    MSFT      Amy    340
3    MSFT  Vanessa    124
4      FB     Carl    243
5      FB    Sarah    350

"""
"""
byComp = df.groupby('Company')
print 1
print byComp.mean() #1

print 2
print byComp.sum() #2

print 3
print byComp.std() #3

"""

"""
--> Result
1

         Sales
Company       
FB       296.5
GOOG     150.0
MSFT     232.0

2
         Sales
Company       
FB         593
GOOG       300
MSFT       464

3
              Sales
Company            
FB        75.660426
GOOG      70.710678
MSFT     152.735065

"""
"""
print byComp.sum().loc['FB']

"""
"""
--> result

Sales    593
Name: FB, dtype: int64

"""

"""
print df.groupby('Company').count()

'''
'''
--> RESULT
         Person  Sales
Company               
FB            2      2
GOOG          2      2
MSFT          2      2
'''
'''

print df.groupby('Company').describe()

"""
"""
--> Reuslt

 Sales                                                        
        count   mean         std    min     25%    50%     75%    max
Company                                                              
FB        2.0  296.5   75.660426  243.0  269.75  296.5  323.25  350.0
GOOG      2.0  150.0   70.710678  100.0  125.00  150.0  175.00  200.0
MSFT      2.0  232.0  152.735065  124.0  178.00  232.0  286.00  340.0

"""
"""
print df.groupby('Company').describe().transpose()

"""
"""
--> Result

Company              FB        GOOG        MSFT
Sales count    2.000000    2.000000    2.000000
      mean   296.500000  150.000000  232.000000
      std     75.660426   70.710678  152.735065
      min    243.000000  100.000000  124.000000
      25%    269.750000  125.000000  178.000000
      50%    296.500000  150.000000  232.000000
      75%    323.250000  175.000000  286.000000
      max    350.000000  200.000000  340.000000


"""

#__________________________________________________________________________________
# lesson 8
# Merging concatenation and joining
"""
pd.concat([df1, df2, df3])

this method will concatnat all three data frames into one

this will concatenate top and bottom

pd.concat([df1, df2, df3], axis = 1) 

this will concat sidewards

Glues the data frame

"""
"""
left = pd.DataFrame({'key' : ['k1', 'k2', 'k3'], 'hello' : ['H4','H5','H6'], 'world' : ['W7','W8','W9']})
right = pd.DataFrame({'key' : ['k1', 'k2', 'k3'], 'hell' : ['h4','h5','h6'], 'war' : ['w7','w8','w9']})

print left
print right

print  pd.merge(left, right, how = 'inner', on = 'key')

"""
"""
--> Result 

  hello key world
0    H4  k1    W7
1    H5  k2    W8
2    H6  k3    W9

  hell key war
0   h4  k1  w7
1   h5  k2  w8
2   h6  k3  w9

  hello key world hell war
0    H4  k1    W7   h4  w7
1    H5  k2    W8   h5  w8
2    H6  k3    W9   h6  w9

"""
"""
left = pd.DataFrame({'hello' : ['H4','H5','H6'], 'world' : ['W7','W8','W9']}, index = ['k1', 'k2', 'k3'] )
right = pd.DataFrame({'hell' : ['h4','h5','h6'], 'war' : ['w7','w8','w9']}, index = ['k1', 'k2', 'k3'] )

print left.join(right)
print left.join(right, how = 'outer')
print left.join(right, how = 'right')
print left.join(right, how = 'left')

"""
"""
--> Result
1. Inner
   hello world hell war
k1    H4    W7   h4  w7
k2    H5    W8   h5  w8
k3    H6    W9   h6  w9

2.Outer
   hello world hell war
k1    H4    W7   h4  w7
k2    H5    W8   h5  w8
k3    H6    W9   h6  w9

3. Right
   hello world hell war
k1    H4    W7   h4  w7
k2    H5    W8   h5  w8
k3    H6    W9   h6  w9

4. left
   hello world hell war
k1    H4    W7   h4  w7
k2    H5    W8   h5  w8
k3    H6    W9   h6  w9

"""
#______________________________________________________________________________
# lesson 9
# Operations

"""
df = pd.DataFrame({'col1' : [1,2,3,4], 
					'col2' : [444, 555, 666, 444], 
					'col3' : ['abc', 'def', 'ghi', 'xyz']})

print df.head()


"""

"""
--> Result

   col1  col2 col3
0     1   444  abc
1     2   555  def
2     3   666  ghi
3     4   444  xyz

"""
"""
print df['col2'].unique()
print df['col2'].nunique()
print df['col2'].value_counts()

"""
"""
--> result

[444 555 666]

3 --> Unquie values #

444    2
555    1
666    1
Name: col2, dtype: int64

This method gives us all the unique values in a given column

"""
"""
print df[df['col1'] > 2]

"""
"""
--> Result

   col1  col2 col3
2     3   666  ghi
3     4   444  xyz

you can put paranthesses and use conditonal operators such as & and |

"""

"""
def times2(x):
	return x*2

print df['col2'].apply(times2)
print df['col3'].apply(len)
print df['col2'].apply(lambda x : x + x)

"""

"""

--> result

1.

0     888
1    1110
2    1332
3     888
Name: col2, dtype: int64

2.

0    3
1    3
2    3
3    3
Name: col3, dtype: int64

3.

0     888
1    1110
2    1332
3     888
Name: col2, dtype: int64

"""

"""

print df.drop(0) # to drop row
print df.drop('col1', axis = 1) # drop column

"""

"""
---> result

   col1  col2 col3
1     2   555  def
2     3   666  ghi
3     4   444  xyz

   col2 col3
0   444  abc
1   555  def
2   666  ghi
3   444  xyz

"""

"""

print df.columns
print df.index

"""
"""

--> Result

Index([u'col1', u'col2', u'col3'], dtype='object')

RangeIndex(start=0, stop=4, step=1)

"""
"""

print df.sort_values('col2')
print df.sort_values(by = 'col2')

"""
"""
--> result
1.

   col1  col2 col3
0     1   444  abc
3     4   444  xyz
1     2   555  def
2     3   666  ghi

2.
   col1  col2 col3
0     1   444  abc
3     4   444  xyz
1     2   555  def
2     3   666  ghi

"""
"""
print df.isnull()

"""

"""
--> result

    col1   col2   col3
0  False  False  False
1  False  False  False
2  False  False  False
3  False  False  False

"""
"""
data = {'A' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
		'B' : ['one','one', 'two', 'two', 'one','one'],
		'c' : ['x', 'y', 'x', 'y', 'x', 'y'],
		'd' : [1,3,2,5,4,1]}

df = pd.DataFrame(data)

print df

"""
"""
--> Data frame we are working with

     A    B  c  d
0  foo  one  x  1
1  foo  one  y  3
2  foo  two  x  2
3  bar  two  y  5
4  bar  one  x  4
5  bar  one  y  1

"""
"""
print df.pivot_table(values = 'd', index = ['A', 'B'], columns = ['c'])

"""
"""
--> Result

A   B            
bar one  4.0  1.0
    two  NaN  5.0
foo one  1.0  3.0
    two  2.0  NaN
"""
#_________________________________________________________________________________________
#lesson 10 
#Data imput and output
"""
print pd.read_csv('Refactored_Py_DS_ML_Bootcamp-master/03-Python-for-Data-Analysis-Pandas/example')

"""
"""
--> Data fram we are woring with

    a   b   c   d
0   0   1   2   3
1   4   5   6   7
2   8   9  10  11
3  12  13  14  15

"""
"""
df = pd.read_csv('Refactored_Py_DS_ML_Bootcamp-master/03-Python-for-Data-Analysis-Pandas/example')

df.to_csv('test.csv', index = False)

df = pd.read_excel('Refactored_Py_DS_ML_Bootcamp-master/03-Python-for-Data-Analysis-Pandas/Excel_Sample.xlsx')
df.to_excel('test.xlsx', sheet_name = 'New')

"""
"""

--> Result 

We read the example file wrote that file to test.csv
and we read the example one more time and 
wrote it to test.xlsv

# pip install openpyxl

"""
"""
data_html = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
print data_html
print data[0].head()

"""
"""
Webscrapping the html file using pandas

"""
"""
from sqlalchemy import create_engine

# import create_engine from sqlalchemy

"""
"""
engine = create_engine('sqlite:///:memo:')

df.to_sql('my_table', engine)

sqldf = pd.read_sql('my_table', con = engine)

# reading and writing into pandas simple sql engine

"""
#______________________________ END OF PANDAS _________________________________________________________________________________________________________________
'''