import sys
sys.path.append("/home/chris/Research/Papers/thesis/thesis_doc/scripts")
from plotError import plotErrorVsModesVars

# plot primitive variable error
base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/9elem/FOM/projection"
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
plot_vars = ["Static_Pressure", "U", "V", "W", "Temperature", "CO_mf", "CO2_mf", "H2O_mf"]
iter_start_list = [215050] * len(data_dirs)
iter_end_list = [218900] * len(data_dirs)
iter_skip_list = [50] * len(data_dirs)
x_vals = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250]
ybounds = [1e-3, 1]
plot_styles = ["r", "b", "c", "purple", "g", "y", "orange", "pink"]
legend_labels = ["Pressure", "X Vel.", "Y Vel.", "Z Vel.", "Temperature", "CO", "CO2", "H2O"]
legend_loc = "upper right"
num_legend_columns = 2
out_file = "projection_error_primitive"
out_dir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/NineElement/Images/"

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
    out_dir,
    ybounds=ybounds,
    legend_labels=legend_labels,
    legend_loc=legend_loc,
    num_legend_columns=num_legend_columns,
    out_file=out_file,
)

# plot conservative variable error
base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/9elem/FOM_consv/projection"
plot_vars = ["Rho", "Rho_U", "Rho_V", "Rho_W", "Rho_E", "Rho_CO_mf", "Rho_CO2_mf", "Rho_H2O_mf"]
# plot_styles = ["r", "g", "b", "c"]
legend_labels = ["Density", "X Mom.", "Y Mom.", "Z Mom.", "Energy", "CO", "CO2", "H2O"]
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
    out_dir,
    ybounds=ybounds,
    legend_labels=legend_labels,
    legend_loc=legend_loc,
    num_legend_columns=num_legend_columns,
    out_file=out_file,
)