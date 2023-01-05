import os

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

mpl.rc('font', family='serif',size='20')
mpl.rc('axes', labelsize='x-large')
mpl.rc('figure', facecolor='w')
mpl.rc('text', usetex=True)
mpl.rc('text.latex',preamble=r'\usepackage{amsmath}')

outname = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/Overview/Images/mapExample"

# 2D plot
ax = plt.figure().add_subplot()

x = np.linspace(0, 10, 101)
y = np.sin(np.pi * x / 2) + 0.1 * np.power(x, 2)

ax.plot(x, y, "k-")
ax.plot(x[::10], y[::10], "ko")

ax.set_xlabel(r"$\widehat{q}_1$")
ax.set_ylabel(r"$\widehat{q}_2$")
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
plt.tight_layout()

plt.savefig(outname + "_2d.png")

# 3D plot
ax = plt.figure().add_subplot(projection='3d')

theta = np.linspace(-4 * np.pi, 4 * np.pi, 101)
z = np.linspace(0, 2, 101)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

ax.plot(x, y, z, "k")
ax.scatter(x[::10], y[::10], z[::10], c="k", alpha=1.0)

ax.set_xlabel(r"$q_1$")
ax.set_ylabel(r"$q_2$")
ax.set_zlabel(r"$q_3$")
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
ax.get_zaxis().set_ticks([])
plt.tight_layout()

plt.savefig(outname + "_3d.png")
