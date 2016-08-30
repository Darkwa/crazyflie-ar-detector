import csv
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

#lecture du fichier
data = csv.reader(open('./log.csv'))
time = []
x = []
y = []
z = []
fields = next(data)
i = 0
for row in data :
    i = 0
    for string in row :
        if i == 0:
            x.append(float(string))
        elif i == 1:
            y.append(float(string))
        elif i == 2:
            z.append(float(string))
        i += 1

#visualisatoin de la courbe
mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(x, y, z, label='quadcopter position')
ax.legend()

plt.show()


