import sys
sys.path.append("/home/chris/Research/Papers/thesis/thesis_doc/scripts")
from plotError import plotErrorVsModesVars

# plot primitive variable error
base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cvrc/FOM/projection"
data_dirs = [
    "k25",
    "k50",
    "k75",
    "k100",
    "k125",
    "k150",
    "k175",
    "k200",
    "k225",
    "k250",
]
file_header = "l2_rel_sum_err"
plot_vars = ["Static_Pressure", "U", "V", "Temperature", "Flamelet_Scalar_Mean", "Flamelet_Parameter"]
# plot_vars = ["Static_Pressure", "U", "V", "W", "Temperature"]
iter_start_list = [50050] * len(data_dirs)
iter_end_list = [60000] * len(data_dirs)
iter_skip_list = [50] * len(data_dirs)
x_vals = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250]
ybounds = [9e-4, 1]
plot_styles = ["r", "b", "c", "g", "orange", "pink"]
legend_labels = ["Pressure", "Axial Vel.", "Radial Vel.", "Temperature", "Mix. Frac.", "Prog. Var."]
legend_loc = "upper right"
num_legend_columns = 2
outfile = "projection_error_primitive"
outdir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cvrc"

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
    num_legend_columns=num_legend_columns,
    outfile=outfile,
)

# plot conservative variable error
base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cvrc/FOM_consv/projection"
plot_vars = ["Rho", "Rho_U", "Rho_V", "Rho_E", "Rho_ZMean", "Rho_CMean"]
# plot_styles = ["r", "g", "b", "c"]
legend_labels = ["Density", "Axial Mom.", "Radial Mom.", "Energy", "Mix. Fac.", "Prog. Var."]
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
    num_legend_columns=num_legend_columns,
    outfile=outfile,
)