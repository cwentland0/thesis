import sys
sys.path.append("/home/chris/Research/Papers/thesis/thesis_doc/scripts")
from plotError import plotErrorVsModesVars

file_header = "l2_rel_sum_err_mag"
outdir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cvrc"

x_vals = [25, 50, 75, 100, 125, 150, 175, 200]
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
iter_start_list = [50050] * len(data_dirs)
iter_end_list = [55000] * len(data_dirs)
iter_skip_list = [50] * len(data_dirs)

ybounds = [5e-4, 1]
# ybounds = None

plot_styles = ["r", "g", "b", "orange", "pink"]
legend_loc = "upper right"
num_legend_columns = 2

# primitive error
base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cvrc/FOM/projection"
plot_vars = ["Static_Pressure", "UVWMag", "Temperature", "Flamelet_Scalar_Mean", "Flamelet_Parameter"]
legend_labels = ["Pressure", "Velocity Mag.", "Temperature", "Mix. Frac.", "Prog. Var."]
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
    num_legend_columns=num_legend_columns,
    out_file=out_file,
)

# conservative error
base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cvrc/FOM_consv/projection"
plot_vars = ["Rho", "Rho_URho_VRho_WMag", "Rho_E", "Rho_ZMean", "Rho_CMean"]
legend_labels = ["Density", "Momentum Mag.", "Energy", "Mix. Fac.", "Prog. Var."]
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
    num_legend_columns=num_legend_columns,
    out_file=out_file,
)