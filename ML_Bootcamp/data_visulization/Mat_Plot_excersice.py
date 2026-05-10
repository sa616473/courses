import matplotlib as plt

print plt.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

pp_1 = PdfPages('blank.pdf')

x = np.arange(0,100)
y = x*2
z = x ** 2

fig = plt.figure()

axes= fig.add_axes([0,0,1,1])

axes.plot(x,y)
axes.set_xlabel('X axis')
axes.set_ylabel('y axis')
axes.set_title('Grrsph')

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,1,1])
ax2 = fig.add_axes([0.2,0.5,.2,.2])

ax1.plot(x,z)
ax2.plot(x,y)

fig,axes = plt.subplots(nrows = 1, ncols=2)


plt.savefig(pp_1, format='pdf')
pp_1.close()