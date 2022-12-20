import sys
sys.path.append("/home/chris/Research/Papers/thesis/thesis_doc/scripts")
from plotErrContours import plotErrContours


zbounds = [3e-3, 3e-2]
yscale = "log"
cb_ticks = [0.003, 0.03]
cb_ticklabels = ["0.003", "0.03"]

xvals_list = [150, 200, 250, 300]
yvals_list = [0.5, 0.75, 1, 1.75, 2.5, 3.75, 5, 7.5, 10]
plot_var = "Average"
xlabel = r"$N_{r}$"
out_dir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cavity/deim"

data_dirs = [
    [
        "parts2/modes150_samp0.005/UnsteadyFieldResults",
        "parts2/modes150_samp0.0075/UnsteadyFieldResults",
        "parts2/modes150_samp0.01/UnsteadyFieldResults",
        "parts2/modes150_samp0.0175/UnsteadyFieldResults",
        "parts3/modes150_samp0.025/UnsteadyFieldResults",
        "parts5/modes150_samp0.0375/UnsteadyFieldResults",
        "parts6/modes150_samp0.05/UnsteadyFieldResults",
        "parts9/modes150_samp0.075/UnsteadyFieldResults",
        "parts13/modes150_samp0.1/UnsteadyFieldResults",
    ],
    [
        "parts2/modes200_samp0.005/UnsteadyFieldResults",
        "parts2/modes200_samp0.0075/UnsteadyFieldResults",
        "parts2/modes200_samp0.01/UnsteadyFieldResults",
        "parts2/modes200_samp0.0175/UnsteadyFieldResults",
        "parts3/modes200_samp0.025/UnsteadyFieldResults",
        "parts5/modes200_samp0.0375/UnsteadyFieldResults",
        "parts6/modes200_samp0.05/UnsteadyFieldResults",
        "parts9/modes200_samp0.075/UnsteadyFieldResults",
        "parts13/modes200_samp0.1/UnsteadyFieldResults",
    ],
    [
        "parts2/modes250_samp0.005/UnsteadyFieldResults",
        "parts2/modes250_samp0.0075/UnsteadyFieldResults",
        "parts2/modes250_samp0.01/UnsteadyFieldResults",
        "parts2/modes250_samp0.0175/UnsteadyFieldResults",
        "parts3/modes250_samp0.025/UnsteadyFieldResults",
        "parts5/modes250_samp0.0375/UnsteadyFieldResults",
        "parts6/modes250_samp0.05/UnsteadyFieldResults",
        "parts9/modes250_samp0.075/UnsteadyFieldResults",
        "parts13/modes250_samp0.1/UnsteadyFieldResults",
    ],
    [
        "parts2/modes300_samp0.005/UnsteadyFieldResults",
        "parts2/modes300_samp0.0075/UnsteadyFieldResults",
        "parts2/modes300_samp0.01/UnsteadyFieldResults",
        "parts2/modes300_samp0.0175/UnsteadyFieldResults",
        "parts3/modes300_samp0.025/UnsteadyFieldResults",
        "parts5/modes300_samp0.0375/UnsteadyFieldResults",
        "parts6/modes300_samp0.05/UnsteadyFieldResults",
        "parts9/modes300_samp0.075/UnsteadyFieldResults",
        "parts13/modes300_samp0.1/UnsteadyFieldResults",
    ],

]

# dtStr = "dt2p5e-6"
# err_file_name = "l2_rel_sum_err_vs_raw_mag_40016_44000_16.dat"

dtStr = "dt5e-6"
err_file_name = "l2_rel_sum_err_vs_raw_mag_20008_22000_8.dat"

# dtStr = "dt1e-5"
# err_file_name = "l2_rel_sum_err_vs_raw_mag_10004_11000_4.dat"

plot_point_markers = True
point_marker_coords = [
    [250, 1],
    [250, 2.5],
]
point_marker_colors = ["k", "k"]
point_marker_styles = ["D", "X"]

##### Random #####

base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cavity/ROMs/primitive/100ms_to_110ms_samp1_" + dtStr + "/mplsvt-real/implicit/k150/solutionModes/conservative/random"

ylabel = "Sampling Rate, \%"
draw_colorbar = False
figsize=(6.4, 4.8)

out_name = "err_contour_random_" + dtStr

plotErrContours(
    base_dir,
    data_dirs,
    err_file_name,
    xvals_list,
    yvals_list,
    plot_var,
    out_dir,
    out_name,
    draw_colorbar=draw_colorbar,
    cb_ticks=cb_ticks,
    cb_ticklabels=cb_ticklabels,
    figsize=figsize,
    zbounds=zbounds,
    yscale=yscale,
    xlabel=xlabel,
    ylabel=ylabel,
    plot_point_markers=plot_point_markers,
    point_marker_coords=point_marker_coords,
    point_marker_colors=point_marker_colors,
    point_marker_styles=point_marker_styles,
)

##### Eigenvec #####

base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cavity/ROMs/primitive/100ms_to_110ms_samp1_" + dtStr + "/mplsvt-real/implicit/k150/solutionModes/conservative/eigenvec"

ylabel = None
draw_colorbar = True
figsize=(7.2, 4.8)

out_name = "err_contour_eigenvec_" + dtStr

plotErrContours(
    base_dir,
    data_dirs,
    err_file_name,
    xvals_list,
    yvals_list,
    plot_var,
    out_dir,
    out_name,
    draw_colorbar=draw_colorbar,
    cb_ticks=cb_ticks,
    cb_ticklabels=cb_ticklabels,
    figsize=figsize,
    zbounds=zbounds,
    yscale=yscale,
    xlabel=xlabel,
    ylabel=ylabel,
    plot_point_markers=plot_point_markers,
    point_marker_coords=point_marker_coords,
    point_marker_colors=point_marker_colors,
    point_marker_styles=point_marker_styles,
)

##### GNAT Carlberg #####

base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cavity/ROMs/primitive/100ms_to_110ms_samp1_" + dtStr + "/mplsvt-real/implicit/k150/solutionModes/conservative/greedy_carlberg"

ylabel = "Sampling Rate, \%"
draw_colorbar = False
figsize=(6.4, 4.8)

out_name = "err_contour_gnat1_" + dtStr

plotErrContours(
    base_dir,
    data_dirs,
    err_file_name,
    xvals_list,
    yvals_list,
    plot_var,
    out_dir,
    out_name,
    draw_colorbar=draw_colorbar,
    cb_ticks=cb_ticks,
    cb_ticklabels=cb_ticklabels,
    figsize=figsize,
    zbounds=zbounds,
    yscale=yscale,
    xlabel=xlabel,
    ylabel=ylabel,
    plot_point_markers=plot_point_markers,
    point_marker_coords=point_marker_coords,
    point_marker_colors=point_marker_colors,
    point_marker_styles=point_marker_styles,
)

##### GNAT Ben #####

base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cavity/ROMs/primitive/100ms_to_110ms_samp1_" + dtStr + "/mplsvt-real/implicit/k150/solutionModes/conservative/greedy_ben"

ylabel = None
draw_colorbar = True
figsize=(7.2, 4.8)

out_name = "err_contour_gnat2_" + dtStr

plotErrContours(
    base_dir,
    data_dirs,
    err_file_name,
    xvals_list,
    yvals_list,
    plot_var,
    out_dir,
    out_name,
    draw_colorbar=draw_colorbar,
    cb_ticks=cb_ticks,
    cb_ticklabels=cb_ticklabels,
    figsize=figsize,
    zbounds=zbounds,
    yscale=yscale,
    xlabel=xlabel,
    ylabel=ylabel,
    plot_point_markers=plot_point_markers,
    point_marker_coords=point_marker_coords,
    point_marker_colors=point_marker_colors,
    point_marker_styles=point_marker_styles,
)