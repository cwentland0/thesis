import sys
sys.path.append("/home/chris/Research/Papers/thesis/thesis_doc/scripts")
from plotError import plotErrorVsModesVars

data_dirs = [
    "k20",
    "k40",
    "k60",
    "k80",
    "k100",
]
iter_start_list = [215050] * len(data_dirs)
iter_end_list = [218900] * len(data_dirs)
iter_skip_list = [50] * len(data_dirs)
x_vals = [20, 40, 60, 80, 100]
ybounds = [1e-2, 5e-1]

file_header = "l2_rel_sum_err_mag"

plot_styles = ["r", "g", "b", "orange", "pink", "k"]
legend_font_size = 14
legend_loc = "upper right"
num_legend_columns = 2

plot_avg = True

out_dir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/NineElement/Images/"

# plot primitive variable error
base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/9elem/FOM/projection"
plot_vars = ["Static_Pressure", "UVWMag", "Temperature", "CO2_mf", "H2O_mf"]
legend_labels = ["Pressure", "Velocity Mag.", "Temperature", "CO2", "H2O"]
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
    out_dir,
    ybounds=ybounds,
    legend_labels=legend_labels,
    legend_loc=legend_loc,
    num_legend_columns=num_legend_columns,
    out_file=out_file,
    legend_font_size=legend_font_size,
    plot_avg=plot_avg,
)

# plot conservative variable error
base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/9elem/FOM_consv/projection"
plot_vars = ["Rho", "Rho_URho_VRho_WMag", "Rho_E", "Rho_CO2_mf", "Rho_H2O_mf"]
legend_labels = ["Density", "Momentum Mag.", "Energy", "CO2", "H2O"]
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
    legend_font_size=legend_font_size,
    plot_avg=plot_avg,
)