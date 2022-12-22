import sys
sys.path.append("/p/work/chriswen/thesis/thesis_doc/scripts")
from plotPartitionStats import plotPartitionStats

base_dir = "/p/work/chriswen/CVRC_cutoff/unforced_dt1e-7/PODBases/deimBases/solutionModes/conservative"
data_dirs = [
    [
        "random/pinv_modes300_samp0.00025",
        "random/pinv_modes300_samp0.000375",
        "random/pinv_modes300_samp0.0005",
        "random/pinv_modes300_samp0.00075",
        "random/pinv_modes300_samp0.001",
        "random/pinv_modes300_samp0.00175",
        "random/pinv_modes300_samp0.0025",
        "random/pinv_modes300_samp0.00375",
        "random/pinv_modes300_samp0.005",
        "random/pinv_modes300_samp0.0075",
        "random/pinv_modes300_samp0.01",
    ],
    [
        "eigenvec/pinv_modes300_samp0.00025",
        "eigenvec/pinv_modes300_samp0.000375",
        "eigenvec/pinv_modes300_samp0.0005",
        "eigenvec/pinv_modes300_samp0.00075",
        "eigenvec/pinv_modes300_samp0.001",
        "eigenvec/pinv_modes300_samp0.00175",
        "eigenvec/pinv_modes300_samp0.0025",
        "eigenvec/pinv_modes300_samp0.00375",
        "eigenvec/pinv_modes300_samp0.005",
        "eigenvec/pinv_modes300_samp0.0075",
        "eigenvec/pinv_modes300_samp0.01",
    ],
    [
        "greedy_carlberg/pinv_modes300_samp0.00025",
        "greedy_carlberg/pinv_modes300_samp0.000375",
        "greedy_carlberg/pinv_modes300_samp0.0005",
        "greedy_carlberg/pinv_modes300_samp0.00075",
        "greedy_carlberg/pinv_modes300_samp0.001",
        "greedy_carlberg/pinv_modes300_samp0.00175",
        "greedy_carlberg/pinv_modes300_samp0.0025",
        "greedy_carlberg/pinv_modes300_samp0.00375",
        "greedy_carlberg/pinv_modes300_samp0.005",
        "greedy_carlberg/pinv_modes300_samp0.0075",
        "greedy_carlberg/pinv_modes300_samp0.01",
    ],
    [
        "greedy_ben/pinv_modes300_samp0.00025",
        "greedy_ben/pinv_modes300_samp0.000375",
        "greedy_ben/pinv_modes300_samp0.0005",
        "greedy_ben/pinv_modes300_samp0.00075",
        "greedy_ben/pinv_modes300_samp0.001",
        "greedy_ben/pinv_modes300_samp0.00175",
        "greedy_ben/pinv_modes300_samp0.0025",
        "greedy_ben/pinv_modes300_samp0.00375",
        "greedy_ben/pinv_modes300_samp0.005",
        "greedy_ben/pinv_modes300_samp0.0075",
        "greedy_ben/pinv_modes300_samp0.01",
    ],
]
xvals_list = [
    [0.025, 0.0375, 0.05, 0.075, 0.1, 0.175, 0.25, 0.375, 0.5, 0.75, 1.0],
    [0.025, 0.0375, 0.05, 0.075, 0.1, 0.175, 0.25, 0.375, 0.5, 0.75, 1.0],
    [0.025, 0.0375, 0.05, 0.075, 0.1, 0.175, 0.25, 0.375, 0.5, 0.75, 1.0],
    [0.025, 0.0375, 0.05, 0.075, 0.1, 0.175, 0.25, 0.375, 0.5, 0.75, 1.0],
]
mesh_name = "cutoff_14cm_noChoke.msh"
xlabel = "Sampling Rate, \%"
out_dir = "/p/work/chriswen/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cvrc/deim/stats"
out_name = "temp"
num_parts_spec = 10

plot_colors = ["g", "b" , "r", "m"]

xbounds = None
xticks = None
ybounds_stats = None
ybounds_iblank = None
ybounds_comm = None
scale_cells = True
num_cells = 2637771
legend_labels = ["Random", "Eigenvector", "GNAT V1", "GNAT_V2"]

plotPartitionStats(
    base_dir,
    data_dirs,
    xvals_list,
    mesh_name,
    num_parts_spec,
    plot_colors,
    xlabel,
    out_dir,
    out_name,
    xbounds=xbounds,
    xticks=xticks,
    ybounds_stats=ybounds_stats,
    ybounds_iblank=ybounds_iblank,
    ybounds_comm=ybounds_comm,
    scale_cells=scale_cells,
    num_cells=num_cells,
    legend_labels=legend_labels,
    legend_loc="best",
    legend_fontsize=12,
    yscale="log",
    xscale="log",
)
