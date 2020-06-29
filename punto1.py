import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
from mpl_toolkits.mplot3d import Axes3D


xy = np.genfromtxt("xy.csv", dtype=float, delimiter=",", skip_header=1, usecols  = range(1, 22))


yPMF = np.sum(xy, axis=0)
xPMF = np.sum(xy, axis=1)

xValues = np.linspace(5, 15, 11)
yValues = np.linspace(5, 25, 21)

#PMF marginal en X y Y
xSum = sum(xPMF)
ySum = sum(yPMF)

def gaussian_dist(x, mu, sigma):
    return 1/(np.sqrt(2*np.pi*sigma**2)) * np.exp(-(x-mu)**2/(2*sigma**2))



plt.plot(yValues, yPMF, xValues, xPMF)
plt.title("Funcion densidad marginal de X y Y")

ys = gaussian_dist(yValues, 0, 1)
xs = gaussian_dist(xValues, 0, 1)


paramX, _ = curve_fit(gaussian_dist, xValues, xPMF)
print(paramX)

paramY, _ = curve_fit(gaussian_dist, yValues, yPMF)
print(paramY)

