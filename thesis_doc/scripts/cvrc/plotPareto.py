import sys
sys.path.append("/home/chris/Research/Papers/thesis/thesis_doc/scripts")
from plotError import plotErrorAvgVs

import numpy as np

plot_type = 3
time_type = 2
vs_raw = True
mags = True

cores_list = [
    [2, 2, 2, 2, 3, 5, 7, 10, 13, 20, 26],
    [2, 2, 2, 2, 3, 5, 7, 10, 13, 20, 26],
    [2, 2, 2, 2, 3, 5, 7, 10, 13, 20, 26],
    [2, 2, 2, 2, 3, 5, 7, 10, 13, 20, 26],
    [880],
]

num_cores_FOM = 880
fom_cpu_hours_calc = np.array([3838.32072237513*10, 4255.47780942917*10, 3553.38605523109*10, 148.268752545122*10])
fom_cpu_hours_mpi = np.array([925.829937346957*10, 1240.63679194450*10, 499.520252227783*10, 154.022252391060*10])

xvals_list = [
    [0.025, 0.0375, 0.05, 0.075, 0.1, 0.175, 0.25, 0.375, 0.5, 0.75, 1],
    [0.025, 0.0375, 0.05, 0.075, 0.1, 0.175, 0.25, 0.375, 0.5, 0.75, 1],
    [0.025, 0.0375, 0.05, 0.075, 0.1, 0.175, 0.25, 0.375, 0.5, 0.75, 1],
    [0.025, 0.0375, 0.05, 0.075, 0.1, 0.175, 0.25, 0.375, 0.5, 0.75, 1],
    [100.0],
]

plot_colors = ['g', 'b', 'r', 'm', 'k']
marker_types = ['o', 'o', 'o', 'o', 7]
line_styles = ['-', '-', '-', '-', 'none']
marker_sizes = [6, 6, 6, 6, 12]

xbounds = [1, 30000]
ybounds = [1e-2, 1.025]
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

deim_modes = 300

plot_var = "Average"
out_dir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cvrc/deim"

data_dirs = [
    [
        "random/parts2/modes" + str(deim_modes) + "_samp0.00025/UnsteadyFieldResults",
        "random/parts2/modes" + str(deim_modes) + "_samp0.000375/UnsteadyFieldResults",
        "random/parts2/modes" + str(deim_modes) + "_samp0.0005/UnsteadyFieldResults",
        "random/parts2/modes" + str(deim_modes) + "_samp0.00075/UnsteadyFieldResults",
        "random/parts3/modes" + str(deim_modes) + "_samp0.001/UnsteadyFieldResults",
        "random/parts5/modes" + str(deim_modes) + "_samp0.00175/UnsteadyFieldResults",
        "random/parts7/modes" + str(deim_modes) + "_samp0.0025/UnsteadyFieldResults",
        "random/parts10/modes" + str(deim_modes) + "_samp0.00375/UnsteadyFieldResults",
        "random/parts13/modes" + str(deim_modes) + "_samp0.005/UnsteadyFieldResults",
        "random/parts20/modes" + str(deim_modes) + "_samp0.0075/UnsteadyFieldResults",
        "random/parts26/modes" + str(deim_modes) + "_samp0.01/UnsteadyFieldResults",
    ],
    [
        "eigenvec/parts2/modes" + str(deim_modes) + "_samp0.00025/UnsteadyFieldResults",
        "eigenvec/parts2/modes" + str(deim_modes) + "_samp0.000375/UnsteadyFieldResults",
        "eigenvec/parts2/modes" + str(deim_modes) + "_samp0.0005/UnsteadyFieldResults",
        "eigenvec/parts2/modes" + str(deim_modes) + "_samp0.00075/UnsteadyFieldResults",
        "eigenvec/parts3/modes" + str(deim_modes) + "_samp0.001/UnsteadyFieldResults",
        "eigenvec/parts5/modes" + str(deim_modes) + "_samp0.00175/UnsteadyFieldResults",
        "eigenvec/parts7/modes" + str(deim_modes) + "_samp0.0025/UnsteadyFieldResults",
        "eigenvec/parts10/modes" + str(deim_modes) + "_samp0.00375/UnsteadyFieldResults",
        "eigenvec/parts13/modes" + str(deim_modes) + "_samp0.005/UnsteadyFieldResults",
        "eigenvec/parts20/modes" + str(deim_modes) + "_samp0.0075/UnsteadyFieldResults",
        "eigenvec/parts26/modes" + str(deim_modes) + "_samp0.01/UnsteadyFieldResults",
    ],
    [
        "greedy_carlberg/parts2/modes" + str(deim_modes) + "_samp0.00025/UnsteadyFieldResults",
        "greedy_carlberg/parts2/modes" + str(deim_modes) + "_samp0.000375/UnsteadyFieldResults",
        "greedy_carlberg/parts2/modes" + str(deim_modes) + "_samp0.0005/UnsteadyFieldResults",
        "greedy_carlberg/parts2/modes" + str(deim_modes) + "_samp0.00075/UnsteadyFieldResults",
        "greedy_carlberg/parts3/modes" + str(deim_modes) + "_samp0.001/UnsteadyFieldResults",
        "greedy_carlberg/parts5/modes" + str(deim_modes) + "_samp0.00175/UnsteadyFieldResults",
        "greedy_carlberg/parts7/modes" + str(deim_modes) + "_samp0.0025/UnsteadyFieldResults",
        "greedy_carlberg/parts10/modes" + str(deim_modes) + "_samp0.00375/UnsteadyFieldResults",
        "greedy_carlberg/parts13/modes" + str(deim_modes) + "_samp0.005/UnsteadyFieldResults",
        "greedy_carlberg/parts20/modes" + str(deim_modes) + "_samp0.0075/UnsteadyFieldResults",
        "greedy_carlberg/parts26/modes" + str(deim_modes) + "_samp0.01/UnsteadyFieldResults",
    ],
    [
        "greedy_ben/parts2/modes" + str(deim_modes) + "_samp0.00025/UnsteadyFieldResults",
        "greedy_ben/parts2/modes" + str(deim_modes) + "_samp0.000375/UnsteadyFieldResults",
        "greedy_ben/parts2/modes" + str(deim_modes) + "_samp0.0005/UnsteadyFieldResults",
        "greedy_ben/parts2/modes" + str(deim_modes) + "_samp0.00075/UnsteadyFieldResults",
        "greedy_ben/parts3/modes" + str(deim_modes) + "_samp0.001/UnsteadyFieldResults",
        "greedy_ben/parts5/modes" + str(deim_modes) + "_samp0.00175/UnsteadyFieldResults",
        "greedy_ben/parts7/modes" + str(deim_modes) + "_samp0.0025/UnsteadyFieldResults",
        "greedy_ben/parts10/modes" + str(deim_modes) + "_samp0.00375/UnsteadyFieldResults",
        "greedy_ben/parts13/modes" + str(deim_modes) + "_samp0.005/UnsteadyFieldResults",
        "greedy_ben/parts20/modes" + str(deim_modes) + "_samp0.0075/UnsteadyFieldResults",
        "greedy_ben/parts26/modes" + str(deim_modes) + "_samp0.01/UnsteadyFieldResults",
    ],
    [
        "../../samp100p/UnsteadyFieldResults",
    ]
]

#### dt = 2.5e-7 #####

plot_legend = True
base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cvrc/ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt2p5e-7/mplsvt-real/implicit/k100/solutionModes/conservative"

iter_start_list = [
    [20020]*len(data_dirs[0]),
    [20020]*len(data_dirs[1]),
    [20020]*len(data_dirs[2]),
    [20020]*len(data_dirs[3]),
    [1001],
]
iter_end_list = [
    [22000]*len(data_dirs[0]),
    [22000]*len(data_dirs[1]),
    [22000]*len(data_dirs[2]),
    [22000]*len(data_dirs[3]),
    [1100]
]
iter_skip_list = [
    [20]*len(data_dirs[0]),
    [20]*len(data_dirs[1]),
    [20]*len(data_dirs[2]),
    [20]*len(data_dirs[3]),
    [1],
]

out_name = "sampled_dt2p5e-7"

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
)

#### dt = 5e-7 #####

plot_legend = True
base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cvrc/ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k100/solutionModes/conservative"

iter_start_list = [
    [10010]*len(data_dirs[0]),
    [10010]*len(data_dirs[1]),
    [10010]*len(data_dirs[2]),
    [10010]*len(data_dirs[3]),
    [1001],
]
iter_end_list = [
    [11000]*len(data_dirs[0]),
    [11000]*len(data_dirs[1]),
    [11000]*len(data_dirs[2]),
    [11000]*len(data_dirs[3]),
    [1100]
]
iter_skip_list = [
    [10]*len(data_dirs[0]),
    [10]*len(data_dirs[1]),
    [10]*len(data_dirs[2]),
    [10]*len(data_dirs[3]),
    [1],
]

out_name = "sampled_dt5e-7"

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
)

#### dt = 1e-6 #####

plot_legend = True
base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cvrc/ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt1e-6/mplsvt-real/implicit/k100/solutionModes/conservative"

iter_start_list = [
    [5005]*len(data_dirs[0]),
    [5005]*len(data_dirs[1]),
    [5005]*len(data_dirs[2]),
    [5005]*len(data_dirs[3]),
    [1001],
]
iter_end_list = [
    [5500]*len(data_dirs[0]),
    [5500]*len(data_dirs[1]),
    [5500]*len(data_dirs[2]),
    [5500]*len(data_dirs[3]),
    [1100]
]
iter_skip_list = [
    [5]*len(data_dirs[0]),
    [5]*len(data_dirs[1]),
    [5]*len(data_dirs[2]),
    [5]*len(data_dirs[3]),
    [1],
]

out_name = "sampled_dt1e-6"

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
)