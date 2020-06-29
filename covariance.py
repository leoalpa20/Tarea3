import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
from scipy.stats import pearsonr
import scipy.stats
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri

x = np.genfromtxt("xyp.csv", dtype=float, delimiter=",", skip_header=1, usecols=range(1))
xAverage = np.average(x)

y = np.genfromtxt("xyp.csv", dtype=float, delimiter=",", skip_header=1, usecols=1)
yAverage = np.average(y)

z = np.genfromtxt("xyp.csv", dtype=float, delimiter=",", skip_header=1, usecols=2)

X = np.reshape(x, -1)
Y = np.reshape(y, -1)
Z = np.reshape(z, -1)


fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_trisurf(X, Y, Z, linewidth=0.01,antialiased=True, cmap=plt.cm.Spectral)
plt.title("Funcion densidad conjunta")
plt.show()

#################################Covariance#######################################3

xyp = np.genfromtxt("xyp.csv", dtype=float, delimiter=",", skip_header=1)

cov = 0


for x in xyp:
    cov += (x[0]-xAverage)*(x[1]-yAverage)*(x[2])

print(cov)

############################PEARSON##############################################################

xyp_noProb = np.genfromtxt("xyp.csv", dtype=float, delimiter=",", skip_header=1, usecols=range(0,2))

pearson = 0


std = np.std(xyp_noProb, axis = 0)


resultado = 1
for x in std:
    resultado = resultado*x

pearson = 0
for x in xyp:
    pearson += ((x[0]-xAverage)*(x[1]-yAverage)*(x[2]))/resultado

print(pearson)






