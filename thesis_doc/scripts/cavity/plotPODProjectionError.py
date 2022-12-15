import sys
sys.path.append("/home/chris/Research/Papers/thesis/thesis_doc/scripts")
from plotError import plotErrorVsModesVars


x_vals = [25, 50, 75, 100, 125, 150, 175, 200]
ybounds = [5e-5, 1]
plot_styles = ["r", "g", "b"]
legend_loc = "upper right"
outdir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cavity"


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
iter_start_list = [100040] * len(data_dirs)
iter_end_list = [110000] * len(data_dirs)
iter_skip_list = [40] * len(data_dirs)

file_header = "l2_rel_sum_err_mag"
plot_vars = ["Static_Pressure", "UVMag", "Temperature"]
legend_labels = ["Pressure", "Velocity Mag.", "Temperature"]
out_file = "projection_error_primitive"

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
    out_file=out_file,
)

# plot conservative variable error
base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cavity/FOM_consv/projection"
plot_vars = ["Rho", "Rho_URho_VMag", "Rho_E"]
legend_labels = ["Density", "Momentum Mag.", "Energy"]
out_file = "projection_error_conservative"

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
    out_file=out_file,
)