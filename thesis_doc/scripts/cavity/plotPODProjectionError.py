import sys
sys.path.append("/home/chris/Research/Papers/thesis/thesis_doc/scripts")
from plotError import plotErrorVsModesVars

# plot primitive variable error
base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cavity/FOM/projection"
data_dirs = [
    "k25",
    "k50",
    "k75",
    "k100",
    "k125",
    "k150",
    "k175",
    "k200",
]
file_header = "l2_rel_sum_err"
plot_vars = ["Static_Pressure", "U", "V", "Temperature"]
iter_start_list = [100040] * len(data_dirs)
iter_end_list = [110000] * len(data_dirs)
iter_skip_list = [40] * len(data_dirs)
x_vals = [25, 50, 75, 100, 125, 150, 175, 200]
ybounds = [1e-5, 1]
plot_styles = ["r", "g", "b", "c"]
legend_labels = ["Pressure", "x-Velocity", "y-Velocity", "Temperature"]
legend_loc = "upper right"
outfile = "projection_error_primitive"
outdir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cavity"

plotErrorVsModesVars(
    base_dir,
    data_dirs,
    file_header,
    plot_vars,
    iter_start_list,
    iter_end_list,
    iter_skip_list,
    x_vals,
    plot_styles,
    outdir,
    ybounds=ybounds,
    legend_labels=legend_labels,
    legend_loc=legend_loc,
    outfile=outfile,
)

# plot conservative variable error
base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cavity/FOM_consv/projection"
plot_vars = ["Rho", "Rho_U", "Rho_V", "Rho_E"]
plot_styles = ["r", "g", "b", "c"]
legend_labels = ["Density", "x-Momentum", "y-Momentum", "Energy"]
outfile = "projection_error_conservative"

plotErrorVsModesVars(
    base_dir,
    data_dirs,
    file_header,
    plot_vars,
    iter_start_list,
    iter_end_list,
    iter_skip_list,
    x_vals,
    plot_styles,
    outdir,
    ybounds=ybounds,
    legend_labels=legend_labels,
    legend_loc=legend_loc,
    outfile=outfile,
)