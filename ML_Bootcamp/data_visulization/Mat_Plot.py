import matplotlib as plt

print plt.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

#lesson 1
# MAtplot lib
#_____________________________________________________________________________________

pp_1 = PdfPages('blank.pdf')

x = np.linspace(0,5,11)
y = x ** 2

"""
--> DATA
xaxis = [0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5 5. ]
yaxis = [ 0.    0.25  1.    2.25  4.    6.25  9.   12.25 16.   20.25 25.  ]
"""
plt.plot(x,y, 'r-')
plt.xlabel('x axis')
plt.ylabel('Y axis')
plt.title('title')

#Multiplots
plt.subplot(1,2,1)
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y, x, 'b')


#plots two different graphs

# Object oriented method
fig = plt.figure()

axes = fig.add_axes([0.1,0.1,0.8,0.8])

axes.plot(x,y)
axes.set_xlabel('X axis')
axes.set_ylabel('y axis')
axes.set_title('Grrsph')

fig = plt.figure()
#figure is an empty canvas and we can add graphs to it

axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
# axes3 = fig.add_axes([0.5,0.1,0.4,0.8])

axes1.plot(x,y, 'y')
axes2.plot(y,x, 'g')

fig,axes = plt.subplots(nrows=2, ncols=2)
plt.tight_layout()

axes[0][0].plot(x,y)

fig , axes = plt.subplots(figsize = (8,2), nrows = 2, ncols = 1)



fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x,x**2,'#FF0093', label='x Square',linewidth=1,linestyle = 'steps')
ax.plot(y,x**3, 'b', label = 'x cubes', marker = 'o', markersize = 30)
ax.set_xlim([0,1])
ax.set_ylim([0,2])
ax.legend(loc = (0.5,0.3))

# ax.plot(x,y, color = '#FF0093', linewidth= 20)

fig.tight_layout()

plt.savefig(pp_1, format='pdf')
pp_1.close()

"""
plotting the data and consverting it to
a pdf file
"""


