import os

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc('font', family='serif',size='12')
mpl.rc('axes', labelsize='x-large')
mpl.rc('figure', facecolor='w')
mpl.rc('text', usetex=False)
mpl.rc('text.latex',preamble=r'\usepackage{amsmath}')

# ---- inputs

data_file = "/home/chris/Research/Papers/thesis/thesis_doc/data/1d_flame/FOM/freq_100000/sol_prim_FOM.npy"

var_names = ["pressure", "vel", "temp", "mf"]
ylabels = ["Pressure (kPa)", "Velocity (m/s)", "Temperature (K)", "Reactant Mass Frac."]
ylims = [[970, 995], [8, 22], [0, 2800], [-0.1, 1.1]]

out_file_head = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/TransientFlame/Images/init_cond_"

# ---- plots ----

data = np.load(data_file)
data = data[:, :, 0]
data[0, :] /= 1.0e3
x = np.linspace(0.0, 0.01, 1024)

for var_idx in range(4):

    print("Plotting " + ylabels[var_idx])

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(x, data[var_idx, :], 'k', linewidth=2.0)

    ax.set_ylim(ylims[var_idx])
    ax.set_ylabel(ylabels[var_idx])
    ax.set_xlabel("x (m)")
    plt.tight_layout()

    out_file = out_file_head + var_names[var_idx] + ".png"
    plt.savefig(out_file)

