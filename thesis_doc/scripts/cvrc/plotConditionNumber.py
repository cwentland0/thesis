import os

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import FormatStrFormatter

mpl.rc('font', family='serif', size='14')
mpl.rc('axes', labelsize='x-large')
mpl.rc('figure', facecolor='w')
mpl.rc('text', usetex=True)
mpl.rc('text.latex',preamble=r'\usepackage{amsmath}')

data_base = "/p/work/chriswen/CVRC_cutoff/unforced_dt1e-7/ROMs/stiffTests/"

data_dirs = [
    "mplsvt/k100/UnsteadyFieldResults",
    "lspg/k100/UnsteadyFieldResults",
]

iter_start = 50001
iter_end = 50300
sub_skip = 1

dt = 1e-7
time_scale = 1e-3

subiter_num = 10
num_modes = 100

ybounds = [1, 1e14]

plot_colors = ["b", "r"]
legend_labels = ["MP-LSVT", "LSPG"]
legend_loc = "upper left"
legend_fontsize = 14

out_dir = "/p/work/chriswen/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cvrc/unsampled"
out_name = "condition_number_10"

##### END USER INPUTS ##### 

iter_range = range(iter_start, iter_end+1, 1)
num_iters = len(iter_range)
cond_arr = np.zeros(num_iters, dtype=np.float64)

t = np.linspace(iter_start * dt * sub_skip, iter_end * dt * sub_skip, num_iters)
t /= time_scale

fig = plt.figure()
ax = fig.add_subplot(111)

for dir_idx, data_dir in enumerate(data_dirs):

    print("Processing directory: " + data_dir)

    for iter_idx, iter_val in enumerate(range(iter_start, iter_end+1, 1)):

        print("Iter " + str(iter_val))

        infile = os.path.join(data_base, data_dir, "rom_dm_sum_" + str(iter_val) + "_" + str(subiter_num) + ".dat")
        data = np.reshape(np.loadtxt(infile, dtype=np.float64), (num_modes, num_modes), order="F")
        cond_arr[iter_idx] = np.linalg.cond(data)

    ax.semilogy(t, cond_arr, plot_colors[dir_idx])

if time_scale == 1.0:
    time_string = "s"
elif time_scale == 1e-3:
    time_string = "ms"

ax.legend(legend_labels, loc=legend_loc, framealpha=0.8, prop={'size':legend_fontsize})
ax.set_ylabel(r"$\kappa$")
ax.set_xlabel("t (" + time_string + ")")
ax.xaxis.set_major_formatter(FormatStrFormatter('%g'))

if ybounds is not None:
    ax.set_ylim(ybounds)

plt.tight_layout()
outfile = os.path.join(out_dir, out_name + ".png")
print("Image saved to " + outfile)
plt.savefig(outfile, format="png")

