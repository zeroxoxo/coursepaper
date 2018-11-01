import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np


path = 'C:/Users/1/Desktop/Data/gam_atr/'
df = pd.read_table(path + '/blocks_stats.tsv', sep='\t')
df1 = pd.DataFrame(df.iloc[:, [0, 1, 3]])
df1.set_index(['m', 'g'], inplace=True)
df2 = df1.unstack()

x = [14,12,10,8,6,4]
y = [12,10,8,6,4,2]

X, Y = np.meshgrid(x, y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(X, Y, df2, rstride=50, cstride=50, color='black')
ax.plot_surface(X, Y, df2, cmap='binary')

plt.xlabel('M')
plt.ylabel('G')
plt.show()
