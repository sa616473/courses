import matplotlib

matplotlib.use('Agg')


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""
df1 = pd.read_csv('Refactored_Py_DS_ML_Bootcamp-master/07-Pandas-Built-in-Data-Viz/df1', index_col = 0)
# If I set the index column to 0 i get the 0 column as my index

df2 = pd.read_csv('Refactored_Py_DS_ML_Bootcamp-master/07-Pandas-Built-in-Data-Viz/df2')
df3 = pd.read_csv('Refactored_Py_DS_ML_Bootcamp-master/07-Pandas-Built-in-Data-Viz/df3')


"""
"""
--> Data we are working with

                   A         B         C         D
2000-01-01  1.339091 -0.163643 -0.646443  1.041233
2000-01-02 -0.774984  0.137034 -0.882716 -2.253382
2000-01-03 -0.921037 -0.482943 -0.417100  0.478638
2000-01-04 -1.738808 -0.072973  0.056517  0.015085
2000-01-05 -0.905980  1.778576  0.381918  0.291436
          a         b         c         d
0  0.039762  0.218517  0.103423  0.957904
1  0.937288  0.041567  0.899125  0.977680
2  0.780504  0.008948  0.557808  0.797510
3  0.672717  0.247870  0.264071  0.444358
4  0.053829  0.520124  0.552264  0.190008
          a         b         c         d
0  0.336272  0.325011  0.001020  0.401402
1  0.980265  0.831835  0.772288  0.076485
2  0.480387  0.686839  0.000575  0.746758
3  0.502106  0.305142  0.768608  0.654685
4  0.856602  0.171448  0.157971  0.321231

"""


# sna_plot = df1['A'].hist()
# Gets me the histogram diretly from pandas

# sna_plot = df1['A'].plot.hist()

# sna_plot = df2.plot.area(alpha = 0.4)

# sna_plot = df2.plot.bar(stacked = True)
# print df1.index

# df1.plot.line(x = df1.index(), y ='B')

# sna_plot = df1.plot.scatter(x = 'A', y = 'B', c= 'C', cmap = 'coolwarm')
# sna_plot = df1.plot.hexbin(x = 'A', y = 'B', cmap = 'coolwarm', gridsize = 25)
"""
sna_plot = df1.plot.density()
fig = sna_plot.get_figure()
fig.savefig('blank.pdf')

"""
#____________________________________________________________________________________
#Pandas built in exersice
"""
df3 = pd.read_csv('Refactored_Py_DS_ML_Bootcamp-master/07-Pandas-Built-in-Data-Viz/df3')

# sna_plot = df3.plot.scatter(x = 'a', y = 'b', color= 'red', figsize = (12,3))
# sna_plot = df3[['a','b']].plot.box()
# sna_plot = df3['a'].plot.hist(bins = 30)
temp = df3.iloc[0:30]
f = plt.figure()
sna_plot = temp.plot.area(alpha = 0.4)
plt.legend(loc = 'center left', bbox_to_anchor = (1.0,0.5))

# sna_plot = df3['a'].plot.kde(lw = 5, linestyle = '--')


fig = sna_plot.get_figure()
fig.savefig('blank.pdf')

"""