import matplotlib
matplotlib.use('Agg')

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
# Lesson 1
# Distribution Plots
#_________________________________________________________________________________
"""
tips = sns.load_dataset('tips')

"""


"""
--> Result
--> Data frame we are working with
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4

"""



# to get rid of the line we can do kde = False
# bins gives you more detailed distrbution of the histogram
"""
#Different type of  plots

sns_plot = sns.distplot(tips['total_bill'], bins=30, kde=False)

sns_plot = sns.jointplot(x ='total_bill', y = 'tip', data=tips, kind= 'kde', color= 'purple')

sns_plot = sns.pairplot(tips, hue= 'sex', palette= 'coolwarm')

sns_plot = sns.rugplot(tips['total_bill'])

"""

"""
#Saving graphs to pdf

fig = sns_plot.get_figure()
fig.savefig('blank.pdf')

# sns_plot.savefig("blank.pdf")

"""
#_________________________________________________________________________________
#lesson 2
# categorical plots

"""
tips = sns.load_dataset('tips')
print tips.head()

"""
"""
--> result
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4

"""
"""
sns_plot = sns.barplot(x= 'sex', y='total_bill', data= tips, estimator = np.std)

sns_plot = sns.countplot(x = 'sex', data = tips)

sns_plot = sns.boxplot(x = 'day', y = 'total_bill', data=tips, hue= 'smoker')

sns_plot = sns.violinplot(x = 'day', y = 'total_bill', data=tips, hue = 'sex', split=True)

sns_plot = sns.stripplot(x='day', y = 'total_bill', data=tips, jitter=True, hue = 'se', split = True)

sns_plot = sns.swarmplot(x ='day', y = 'total_bill', data=tips, color= 'black' )

sns_plot = sns.catplot(x = 'day', y = 'total_bill', data=tips, kind='violin')

"""
"""
# fig = sns_plot.get_figure()
# fig.savefig('blank.pdf')

sns_plot.savefig('blank.pdf')

"""

#__________________________________________________________________________________
#lesson 3
#Matrix Plots
"""
tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
print tips.head()
print 
print flights.head()
"""
"""
--> tips

   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4

--> Flights
   year     month  passengers
0  1949   January         112
1  1949  February         118
2  1949     March         132
3  1949     April         129
4  1949       May         121

"""
"""
tc =  tips.corr()
fg = flights.pivot_table(index = 'month', columns= 'year', values='passengers')
"""
"""
--> Data we are working with
            total_bill       tip      size
total_bill    1.000000  0.675734  0.598315
tip           0.675734  1.000000  0.489299
size          0.598315  0.489299  1.000000

"""
"""
print fg
"""
"""
--> Flights dataframe after pivot table

year       1949  1950  1951  1952  1953  1954  1955  1956  1957  1958  1959  1960
month                                                                            
January     112   115   145   171   196   204   242   284   315   340   360   417
February    118   126   150   180   196   188   233   277   301   318   342   391
March       132   141   178   193   236   235   267   317   356   362   406   419
April       129   135   163   181   235   227   269   313   348   348   396   461
May         121   125   172   183   229   234   270   318   355   363   420   472
June        135   149   178   218   243   264   315   374   422   435   472   535
July        148   170   199   230   264   302   364   413   465   491   548   622
August      148   170   199   242   272   293   347   405   467   505   559   606
September   136   158   184   209   237   259   312   355   404   404   463   508
October     119   133   162   191   211   229   274   306   347   359   407   461
November    104   114   146   172   180   203   237   271   305   310   362   390
December    118   140   166   194   201   229   278   306   336   337   405   432
"""
"""
==> plots
sns_plot = sns.heatmap(tc, color = 'red', annot=True, cmap='coolwarm')

sns_plot = sns.heatmap(fg, cmap = 'magma', linecolor ='black' , linewidths=1)

sns_plot = sns.clustermap(fg, cmap='coolwarm', standard_scale= 1)
"""
"""
Saving to pdf
# sns_plot.savefig('blank.pdf')
# fig = sns_plot.get_figure()
# fig.savefig('blank.pdf')

"""
#____________________________________________________________________________________
# lesson 4
# Grid models
"""
iris = sns.load_dataset('iris')
print iris.head()
"""
"""
--> Data we are working with
   sepal_length  sepal_width  petal_length  petal_width species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa
2           4.7          3.2           1.3          0.2  setosa
3           4.6          3.1           1.5          0.2  setosa
4           5.0          3.6           1.4          0.2  setosa
"""
"""
print iris['species'].unique()
"""
"""
['setosa' 'versicolor' 'virginica']

"""
"""
g = sns.PairGrid(iris)
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
sns_plot = g.map_lower(sns.kdeplot)

tips = sns.load_dataset('tips')

g = sns.FacetGrid(data = tips, col = 'time', row = 'smoker')

g.map(plt.scatter, 'total_bill', 'tip')
sns_plot = g

sns_plot.savefig('blank.pdf')

"""
#___________________________________________________________________________________
#lesson 5
# Regression plots
"""
tips = sns.load_dataset('tips')
print tips.head()

"""
"""
--> Date we are working with

   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4

"""
"""
sns_plot = sns.lmplot(x ='total_bill', y= 'tip', data=tips, hue='sex', markers= ['o', 'v'], scatter_kws={'s':100}, legend=True,col = 'sex', row = 'time', aspect= 0.6, height=8)


sns_plot.savefig('blank.pdf')

"""
#___________________________________________________________________________________________________________________________________________________________________________________________
#lesson 6 
# Style and color
"""
tips = sns.load_dataset('tips')
"""
"""
--> Data we are working with

   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4

"""
"""
sns.set_style('darkgrid')
# plt.figure(figsize = (12,3))

sns.set_context('talk', font_scale= 2.5)
sna_plot = sns.countplot(x='sex', data= tips)
sns.despine(left=True)

fig = sna_plot.get_figure()
fig.savefig('blank.pdf')
"""
#________________________________________________________________________________
#Seaborn Excersice

"""
sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')

titanic.head()

titanic_corr = titanic.corr()

# sna_plot = sns.jointplot(x = 'fare', y = 'age', data = titanic)

# sna_plot = sns.distplot(titanic['fare'], norm_hist=False, kde=False, color = 'red', bins = 30)

# sna_plot = sns.swarmplot(x = 'class', y = 'age', data=titanic)

g = sns.FacetGrid(data = titanic, col = 'sex')
g.map(sns.distplot, 'age')
sna_plot = g

# sna_plot = sns.boxplot(x = 'class', y = 'age', data=titanic)

# sna_plot = sns.violinplot(x = 'class', y = 'age', data=titanic, split=True, jitter = True)

# sna_plot = sns.stripplot(x = 'class', y = 'age', data=titanic, dodge=True, jitter=True)

# sna_plot = sns.countplot(x = 'sex', data=titanic)

# sna_plot = sns.heatmap(titanic_corr, annot=False, cmap= 'coolwarm')

# sna_plot= sns.FacetGrid(col= 'class' , row = 'age', data = titanic )



# fig = sna_plot.get_figure()
# fig.savefig('blank.pdf')
sna_plot.savefig('blank.pdf')

"""
#__________________________________________________________________________________________
