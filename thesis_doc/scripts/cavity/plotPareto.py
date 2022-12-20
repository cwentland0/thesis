import sys
sys.path.append("/home/chris/Research/Papers/thesis/thesis_doc/scripts")
from plotError import plotErrorAvgVs

import numpy as np

plot_type = 3
time_type = 2
vs_raw = True
mags = True

cores_list = [
    [2, 2, 2, 2, 3, 5, 6, 9, 13],
    [2, 2, 2, 2, 3, 5, 6, 9, 13],
    [2, 2, 2, 2, 3, 5, 6, 9, 13],
    [2, 2, 2, 2, 3, 5, 6, 9, 13],
    [120],
]

num_cores_FOM = 120
fom_cpu_hours_calc = np.array([371.776565253735*10, 395.686930656433*10, 296.471246242523*10, 22.1765227158880*10])
fom_cpu_hours_mpi = np.array([70.7120964904626*10, 146.679129362106*10, 46.9130725860596*10, 22.3457623936093*10])

xvals_list = [
    [0.5, 0.75, 1, 1.75, 2.5, 3.75, 5, 7.5, 10],
    [0.5, 0.75, 1, 1.75, 2.5, 3.75, 5, 7.5, 10],
    [0.5, 0.75, 1, 1.75, 2.5, 3.75, 5, 7.5, 10],
    [0.5, 0.75, 1, 1.75, 2.5, 3.75, 5, 7.5, 10],
    [100.0],
]

plot_colors = ['g', 'b', 'r', 'm', 'k']
marker_types = ['o', 'o', 'o', 'o', 7]
line_styles = ['-', '-', '-', '-', 'none']
marker_sizes = [6, 6, 6, 6, 12]

point_marker_idxs = [2, 4]
point_marker_styles = ["D", "X"]
point_marker_size = 8

xbounds = [0.1, 300]
ybounds = [1e-3, 1.05]
xlabel = None

legend_labels = [
    "Random",
    "Eigenvector",
    "GNAT, V1",
    "GNAT, V2",
    "Unsampled",
]
legend_loc = "upper left"
legend_fontsize = 14

deim_modes = 250

plot_var = "Average"
out_dir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cavity/deim"

##### dt = 2.5e-6 #####

plot_legend = True
plot_point_markers = False
base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cavity/ROMs/primitive/100ms_to_110ms_samp1_dt2p5e-6/mplsvt-real/implicit/k150/solutionModes/conservative"

data_dirs = [
    [
        "random/parts2/modes" + str(deim_modes) + "_samp0.005/UnsteadyFieldResults",
        "random/parts2/modes" + str(deim_modes) + "_samp0.0075/UnsteadyFieldResults",
        "random/parts2/modes" + str(deim_modes) + "_samp0.01/UnsteadyFieldResults",
        "random/parts2/modes" + str(deim_modes) + "_samp0.0175/UnsteadyFieldResults",
        "random/parts3/modes" + str(deim_modes) + "_samp0.025/UnsteadyFieldResults",
        "random/parts5/modes" + str(deim_modes) + "_samp0.0375/UnsteadyFieldResults",
        "random/parts6/modes" + str(deim_modes) + "_samp0.05/UnsteadyFieldResults",
        "random/parts9/modes" + str(deim_modes) + "_samp0.075/UnsteadyFieldResults",
        "random/parts13/modes" + str(deim_modes) + "_samp0.1/UnsteadyFieldResults",
    ],
    [
        "eigenvec/parts2/modes" + str(deim_modes) + "_samp0.005/UnsteadyFieldResults",
        "eigenvec/parts2/modes" + str(deim_modes) + "_samp0.0075/UnsteadyFieldResults",
        "eigenvec/parts2/modes" + str(deim_modes) + "_samp0.01/UnsteadyFieldResults",
        "eigenvec/parts2/modes" + str(deim_modes) + "_samp0.0175/UnsteadyFieldResults",
        "eigenvec/parts3/modes" + str(deim_modes) + "_samp0.025/UnsteadyFieldResults",
        "eigenvec/parts5/modes" + str(deim_modes) + "_samp0.0375/UnsteadyFieldResults",
        "eigenvec/parts6/modes" + str(deim_modes) + "_samp0.05/UnsteadyFieldResults",
        "eigenvec/parts9/modes" + str(deim_modes) + "_samp0.075/UnsteadyFieldResults",
        "eigenvec/parts13/modes" + str(deim_modes) + "_samp0.1/UnsteadyFieldResults",
    ],
    [
        "greedy_carlberg/parts2/modes" + str(deim_modes) + "_samp0.005/UnsteadyFieldResults",
        "greedy_carlberg/parts2/modes" + str(deim_modes) + "_samp0.0075/UnsteadyFieldResults",
        "greedy_carlberg/parts2/modes" + str(deim_modes) + "_samp0.01/UnsteadyFieldResults",
        "greedy_carlberg/parts2/modes" + str(deim_modes) + "_samp0.0175/UnsteadyFieldResults",
        "greedy_carlberg/parts3/modes" + str(deim_modes) + "_samp0.025/UnsteadyFieldResults",
        "greedy_carlberg/parts5/modes" + str(deim_modes) + "_samp0.0375/UnsteadyFieldResults",
        "greedy_carlberg/parts6/modes" + str(deim_modes) + "_samp0.05/UnsteadyFieldResults",
        "greedy_carlberg/parts9/modes" + str(deim_modes) + "_samp0.075/UnsteadyFieldResults",
        "greedy_carlberg/parts13/modes" + str(deim_modes) + "_samp0.1/UnsteadyFieldResults",
    ],
    [
        "greedy_ben/parts2/modes" + str(deim_modes) + "_samp0.005/UnsteadyFieldResults",
        "greedy_ben/parts2/modes" + str(deim_modes) + "_samp0.0075/UnsteadyFieldResults",
        "greedy_ben/parts2/modes" + str(deim_modes) + "_samp0.01/UnsteadyFieldResults",
        "greedy_ben/parts2/modes" + str(deim_modes) + "_samp0.0175/UnsteadyFieldResults",
        "greedy_ben/parts3/modes" + str(deim_modes) + "_samp0.025/UnsteadyFieldResults",
        "greedy_ben/parts5/modes" + str(deim_modes) + "_samp0.0375/UnsteadyFieldResults",
        "greedy_ben/parts6/modes" + str(deim_modes) + "_samp0.05/UnsteadyFieldResults",
        "greedy_ben/parts9/modes" + str(deim_modes) + "_samp0.075/UnsteadyFieldResults",
        "greedy_ben/parts13/modes" + str(deim_modes) + "_samp0.1/UnsteadyFieldResults",
    ],
    [
        "../../samp100p/UnsteadyFieldResults",
    ]
]

iter_start_list = [
    [40016]*len(data_dirs[0]),
    [40016]*len(data_dirs[1]),
    [40016]*len(data_dirs[2]),
    [40016]*len(data_dirs[3]),
    [2501],
]
iter_end_list = [
    [44000]*len(data_dirs[0]),
    [44000]*len(data_dirs[1]),
    [44000]*len(data_dirs[2]),
    [44000]*len(data_dirs[3]),
    [2750]
]
iter_skip_list = [
    [16]*len(data_dirs[0]),
    [16]*len(data_dirs[1]),
    [16]*len(data_dirs[2]),
    [16]*len(data_dirs[3]),
    [1],
]

out_name = "sampled_dt2p5e-6"

plotErrorAvgVs(
    plot_type,
    base_dir,
    data_dirs,
    iter_start_list,
    iter_end_list,
    iter_skip_list,
    xvals_list,
    plot_var,
    plot_colors,
    xlabel,
    out_dir,
    out_name,
    time_type=time_type,
    cores_list=cores_list,
    num_cores_FOM=num_cores_FOM,
    fom_cpu_hours_calc=fom_cpu_hours_calc,
    fom_cpu_hours_mpi=fom_cpu_hours_mpi,
    vs_raw=vs_raw,
    mags=mags,
    xscale="log",
    yscale="log",
    xbounds=xbounds,
    ybounds=ybounds,
    plot_legend=plot_legend,
    legend_labels=legend_labels,
    legend_loc=legend_loc,
    legend_fontsize=legend_fontsize,
    marker_types=marker_types,
    marker_sizes=marker_sizes,
    line_styles=line_styles,
    plot_point_markers=plot_point_markers,
    point_marker_idxs=point_marker_idxs,
    point_marker_styles=point_marker_styles,
    point_marker_size=point_marker_size,
)

##### dt = 5e-6 #####

plot_point_markers = True
plot_legend = False
base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cavity/ROMs/primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k150/solutionModes/conservative"

data_dirs = [
    [
        "random/parts2/modes" + str(deim_modes) + "_samp0.005/UnsteadyFieldResults",
        "random/parts2/modes" + str(deim_modes) + "_samp0.0075/UnsteadyFieldResults",
        "random/parts2/modes" + str(deim_modes) + "_samp0.01/UnsteadyFieldResults",
        "random/parts2/modes" + str(deim_modes) + "_samp0.0175/UnsteadyFieldResults",
        "random/parts3/modes" + str(deim_modes) + "_samp0.025/UnsteadyFieldResults",
        "random/parts5/modes" + str(deim_modes) + "_samp0.0375/UnsteadyFieldResults",
        "random/parts6/modes" + str(deim_modes) + "_samp0.05/UnsteadyFieldResults",
        "random/parts9/modes" + str(deim_modes) + "_samp0.075/UnsteadyFieldResults",
        "random/parts13/modes" + str(deim_modes) + "_samp0.1/UnsteadyFieldResults",
    ],
    [
        "eigenvec/parts2/modes" + str(deim_modes) + "_samp0.005/UnsteadyFieldResults",
        "eigenvec/parts2/modes" + str(deim_modes) + "_samp0.0075/UnsteadyFieldResults",
        "eigenvec/parts2/modes" + str(deim_modes) + "_samp0.01/UnsteadyFieldResults",
        "eigenvec/parts2/modes" + str(deim_modes) + "_samp0.0175/UnsteadyFieldResults",
        "eigenvec/parts3/modes" + str(deim_modes) + "_samp0.025/UnsteadyFieldResults",
        "eigenvec/parts5/modes" + str(deim_modes) + "_samp0.0375/UnsteadyFieldResults",
        "eigenvec/parts6/modes" + str(deim_modes) + "_samp0.05/UnsteadyFieldResults",
        "eigenvec/parts9/modes" + str(deim_modes) + "_samp0.075/UnsteadyFieldResults",
        "eigenvec/parts13/modes" + str(deim_modes) + "_samp0.1/UnsteadyFieldResults",
    ],
    [
        "greedy_carlberg/parts2/modes" + str(deim_modes) + "_samp0.005/UnsteadyFieldResults",
        "greedy_carlberg/parts2/modes" + str(deim_modes) + "_samp0.0075/UnsteadyFieldResults",
        "greedy_carlberg/parts2/modes" + str(deim_modes) + "_samp0.01/UnsteadyFieldResults",
        "greedy_carlberg/parts2/modes" + str(deim_modes) + "_samp0.0175/UnsteadyFieldResults",
        "greedy_carlberg/parts3/modes" + str(deim_modes) + "_samp0.025/UnsteadyFieldResults",
        "greedy_carlberg/parts5/modes" + str(deim_modes) + "_samp0.0375/UnsteadyFieldResults",
        "greedy_carlberg/parts6/modes" + str(deim_modes) + "_samp0.05/UnsteadyFieldResults",
        "greedy_carlberg/parts9/modes" + str(deim_modes) + "_samp0.075/UnsteadyFieldResults",
        "greedy_carlberg/parts13/modes" + str(deim_modes) + "_samp0.1/UnsteadyFieldResults",
    ],
    [
        "greedy_ben/parts2/modes" + str(deim_modes) + "_samp0.005/UnsteadyFieldResults",
        "greedy_ben/parts2/modes" + str(deim_modes) + "_samp0.0075/UnsteadyFieldResults",
        "greedy_ben/parts2/modes" + str(deim_modes) + "_samp0.01/UnsteadyFieldResults",
        "greedy_ben/parts2/modes" + str(deim_modes) + "_samp0.0175/UnsteadyFieldResults",
        "greedy_ben/parts3/modes" + str(deim_modes) + "_samp0.025/UnsteadyFieldResults",
        "greedy_ben/parts5/modes" + str(deim_modes) + "_samp0.0375/UnsteadyFieldResults",
        "greedy_ben/parts6/modes" + str(deim_modes) + "_samp0.05/UnsteadyFieldResults",
        "greedy_ben/parts9/modes" + str(deim_modes) + "_samp0.075/UnsteadyFieldResults",
        "greedy_ben/parts13/modes" + str(deim_modes) + "_samp0.1/UnsteadyFieldResults",
    ],
    [
        "../../samp100p/UnsteadyFieldResults",
    ]
]

iter_start_list = [
    [20008]*len(data_dirs[0]),
    [20008]*len(data_dirs[1]),
    [20008]*len(data_dirs[2]),
    [20008]*len(data_dirs[3]),
    [2501],
]
iter_end_list = [
    [22000]*len(data_dirs[0]),
    [22000]*len(data_dirs[1]),
    [22000]*len(data_dirs[2]),
    [22000]*len(data_dirs[3]),
    [2750]
]
iter_skip_list = [
    [8]*len(data_dirs[0]),
    [8]*len(data_dirs[1]),
    [8]*len(data_dirs[2]),
    [8]*len(data_dirs[3]),
    [1],
]

out_name = "sampled_dt5e-6"

plotErrorAvgVs(
    plot_type,
    base_dir,
    data_dirs,
    iter_start_list,
    iter_end_list,
    iter_skip_list,
    xvals_list,
    plot_var,
    plot_colors,
    xlabel,
    out_dir,
    out_name,
    time_type=time_type,
    cores_list=cores_list,
    num_cores_FOM=num_cores_FOM,
    fom_cpu_hours_calc=fom_cpu_hours_calc,
    fom_cpu_hours_mpi=fom_cpu_hours_mpi,
    vs_raw=vs_raw,
    mags=mags,
    xscale="log",
    yscale="log",
    xbounds=xbounds,
    ybounds=ybounds,
    plot_legend=plot_legend,
    legend_labels=legend_labels,
    legend_loc=legend_loc,
    marker_types=marker_types,
    marker_sizes=marker_sizes,
    line_styles=line_styles,
    legend_fontsize=legend_fontsize,
    plot_point_markers=plot_point_markers,
    point_marker_idxs=point_marker_idxs,
    point_marker_styles=point_marker_styles,
    point_marker_size=point_marker_size,
)

#### dt = 1e-5 #####

plot_legend = False
plot_point_markers = False
base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cavity/ROMs/primitive/100ms_to_110ms_samp1_dt1e-5/mplsvt-real/implicit/k150/solutionModes/conservative"

data_dirs = [
    [
        "random/parts2/modes" + str(deim_modes) + "_samp0.005/UnsteadyFieldResults",
        "random/parts2/modes" + str(deim_modes) + "_samp0.0075/UnsteadyFieldResults",
        "random/parts2/modes" + str(deim_modes) + "_samp0.01/UnsteadyFieldResults",
        "random/parts2/modes" + str(deim_modes) + "_samp0.0175/UnsteadyFieldResults",
        "random/parts3/modes" + str(deim_modes) + "_samp0.025/UnsteadyFieldResults",
        "random/parts5/modes" + str(deim_modes) + "_samp0.0375/UnsteadyFieldResults",
        "random/parts6/modes" + str(deim_modes) + "_samp0.05/UnsteadyFieldResults",
        "random/parts9/modes" + str(deim_modes) + "_samp0.075/UnsteadyFieldResults",
        "random/parts13/modes" + str(deim_modes) + "_samp0.1/UnsteadyFieldResults",
    ],
    [
        "eigenvec/parts2/modes" + str(deim_modes) + "_samp0.005/UnsteadyFieldResults",
        "eigenvec/parts2/modes" + str(deim_modes) + "_samp0.0075/UnsteadyFieldResults",
        "eigenvec/parts2/modes" + str(deim_modes) + "_samp0.01/UnsteadyFieldResults",
        "eigenvec/parts2/modes" + str(deim_modes) + "_samp0.0175/UnsteadyFieldResults",
        "eigenvec/parts3/modes" + str(deim_modes) + "_samp0.025/UnsteadyFieldResults",
        "eigenvec/parts5/modes" + str(deim_modes) + "_samp0.0375/UnsteadyFieldResults",
        "eigenvec/parts6/modes" + str(deim_modes) + "_samp0.05/UnsteadyFieldResults",
        "eigenvec/parts9/modes" + str(deim_modes) + "_samp0.075/UnsteadyFieldResults",
        "eigenvec/parts13/modes" + str(deim_modes) + "_samp0.1/UnsteadyFieldResults",
    ],
    [
        "greedy_carlberg/parts2/modes" + str(deim_modes) + "_samp0.005/UnsteadyFieldResults",
        "greedy_carlberg/parts2/modes" + str(deim_modes) + "_samp0.0075/UnsteadyFieldResults",
        "greedy_carlberg/parts2/modes" + str(deim_modes) + "_samp0.01/UnsteadyFieldResults",
        "greedy_carlberg/parts2/modes" + str(deim_modes) + "_samp0.0175/UnsteadyFieldResults",
        "greedy_carlberg/parts3/modes" + str(deim_modes) + "_samp0.025/UnsteadyFieldResults",
        "greedy_carlberg/parts5/modes" + str(deim_modes) + "_samp0.0375/UnsteadyFieldResults",
        "greedy_carlberg/parts6/modes" + str(deim_modes) + "_samp0.05/UnsteadyFieldResults",
        "greedy_carlberg/parts9/modes" + str(deim_modes) + "_samp0.075/UnsteadyFieldResults",
        "greedy_carlberg/parts13/modes" + str(deim_modes) + "_samp0.1/UnsteadyFieldResults",
    ],
    [
        "greedy_ben/parts2/modes" + str(deim_modes) + "_samp0.005/UnsteadyFieldResults",
        "greedy_ben/parts2/modes" + str(deim_modes) + "_samp0.0075/UnsteadyFieldResults",
        "greedy_ben/parts2/modes" + str(deim_modes) + "_samp0.01/UnsteadyFieldResults",
        "greedy_ben/parts2/modes" + str(deim_modes) + "_samp0.0175/UnsteadyFieldResults",
        "greedy_ben/parts3/modes" + str(deim_modes) + "_samp0.025/UnsteadyFieldResults",
        "greedy_ben/parts5/modes" + str(deim_modes) + "_samp0.0375/UnsteadyFieldResults",
        "greedy_ben/parts6/modes" + str(deim_modes) + "_samp0.05/UnsteadyFieldResults",
        "greedy_ben/parts9/modes" + str(deim_modes) + "_samp0.075/UnsteadyFieldResults",
        "greedy_ben/parts13/modes" + str(deim_modes) + "_samp0.1/UnsteadyFieldResults",
    ],
    [
        "../../samp100p/UnsteadyFieldResults",
    ]
]

iter_start_list = [
    [10004]*len(data_dirs[0]),
    [10004]*len(data_dirs[1]),
    [10004]*len(data_dirs[2]),
    [10004]*len(data_dirs[3]),
    [2501],
]
iter_end_list = [
    [11000]*len(data_dirs[0]),
    [11000]*len(data_dirs[1]),
    [11000]*len(data_dirs[2]),
    [11000]*len(data_dirs[3]),
    [2750]
]
iter_skip_list = [
    [4]*len(data_dirs[0]),
    [4]*len(data_dirs[1]),
    [4]*len(data_dirs[2]),
    [4]*len(data_dirs[3]),
    [1],
]

out_name = "sampled_dt1e-5"

plotErrorAvgVs(
    plot_type,
    base_dir,
    data_dirs,
    iter_start_list,
    iter_end_list,
    iter_skip_list,
    xvals_list,
    plot_var,
    plot_colors,
    xlabel,
    out_dir,
    out_name,
    time_type=time_type,
    cores_list=cores_list,
    num_cores_FOM=num_cores_FOM,
    fom_cpu_hours_calc=fom_cpu_hours_calc,
    fom_cpu_hours_mpi=fom_cpu_hours_mpi,
    vs_raw=vs_raw,
    mags=mags,
    xscale="log",
    yscale="log",
    xbounds=xbounds,
    ybounds=ybounds,
    plot_legend=plot_legend,
    legend_labels=legend_labels,
    legend_loc=legend_loc,
    marker_types=marker_types,
    marker_sizes=marker_sizes,
    line_styles=line_styles,
    legend_fontsize=legend_fontsize,
    plot_point_markers=plot_point_markers,
    point_marker_idxs=point_marker_idxs,
    point_marker_styles=point_marker_styles,
    point_marker_size=point_marker_size,
)