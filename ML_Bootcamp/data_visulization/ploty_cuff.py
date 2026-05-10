import matplotlib

matplotlib.use('Agg')

import pandas as pd
import numpy as np

from plotly import __version__
import cufflinks as cf
from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as px

cf.go_offline()

#Data

df = pd.DataFrame(np.random.randn(100,4), columns = 'A B C D'.split())


"""
--> Data we are working with

          A         B         C         D
0  0.040720  0.088769  0.947860 -0.223775
1 -0.070617 -1.293854  0.317639 -0.761501
2  0.408111 -0.089325 -0.404231 -0.044232
3 -0.666402 -0.131516 -1.404194 -1.853543
4 -0.110669  0.127784 -0.303840 -0.000030

"""

df2 = pd.DataFrame({'Category' : ['A', 'B', 'C'], 'Values' : [32,43,50]})


"""
--> Data we are working with

  Category  Values
0        A      32
1        B      43
2        C      50

"""
sna_plot = df.plot()

fig = sna_plot.get_figure()
fig.savefig('blank.pdf')




