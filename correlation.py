import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats

xyp = np.genfromtxt("xyp.csv", dtype=float, delimiter=",", skip_header=1)

corr = 0
for x in xyp:
   mult += x[0]*x[1]*x[2]

print(corr)

