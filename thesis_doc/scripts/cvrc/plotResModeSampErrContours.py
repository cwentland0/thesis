import sys
sys.path.append("/home/chris/Research/Papers/thesis/thesis_doc/scripts")
from plotErrContours import plotErrContours


zbounds = [2e-2, 2e-1]
yscale = "log"
cb_ticks = [0.02, 0.2]
cb_ticklabels = ["0.02", "0.2"]

xvals_list = [150, 200, 250, 300]
yvals_list = [0.025, 0.0375, 0.05, 0.075, 0.1, 0.175, 0.25, 0.375, 0.5, 0.75, 1]
plot_var = "Average"
xlabel = r"$N_{r}$"

out_dir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cvrc/deim"

data_dirs = [
    [
        "parts2/modes150_samp0.00025/UnsteadyFieldResults",
        "parts2/modes150_samp0.000375/UnsteadyFieldResults",
        "parts2/modes150_samp0.0005/UnsteadyFieldResults",
        "parts2/modes150_samp0.00075/UnsteadyFieldResults",
        "parts3/modes150_samp0.001/UnsteadyFieldResults",
        "parts5/modes150_samp0.00175/UnsteadyFieldResults",
        "parts7/modes150_samp0.0025/UnsteadyFieldResults",
        "parts10/modes150_samp0.00375/UnsteadyFieldResults",
        "parts13/modes150_samp0.005/UnsteadyFieldResults",
        "parts20/modes150_samp0.0075/UnsteadyFieldResults",
        "parts26/modes150_samp0.01/UnsteadyFieldResults",
    ],
    [
        "parts2/modes200_samp0.00025/UnsteadyFieldResults",
        "parts2/modes200_samp0.000375/UnsteadyFieldResults",
        "parts2/modes200_samp0.0005/UnsteadyFieldResults",
        "parts2/modes200_samp0.00075/UnsteadyFieldResults",
        "parts3/modes200_samp0.001/UnsteadyFieldResults",
        "parts5/modes200_samp0.00175/UnsteadyFieldResults",
        "parts7/modes200_samp0.0025/UnsteadyFieldResults",
        "parts10/modes200_samp0.00375/UnsteadyFieldResults",
        "parts13/modes200_samp0.005/UnsteadyFieldResults",
        "parts20/modes200_samp0.0075/UnsteadyFieldResults",
        "parts26/modes200_samp0.01/UnsteadyFieldResults",
    ],
    [
        "parts2/modes250_samp0.00025/UnsteadyFieldResults",
        "parts2/modes250_samp0.000375/UnsteadyFieldResults",
        "parts2/modes250_samp0.0005/UnsteadyFieldResults",
        "parts2/modes250_samp0.00075/UnsteadyFieldResults",
        "parts3/modes250_samp0.001/UnsteadyFieldResults",
        "parts5/modes250_samp0.00175/UnsteadyFieldResults",
        "parts7/modes250_samp0.0025/UnsteadyFieldResults",
        "parts10/modes250_samp0.00375/UnsteadyFieldResults",
        "parts13/modes250_samp0.005/UnsteadyFieldResults",
        "parts20/modes250_samp0.0075/UnsteadyFieldResults",
        "parts26/modes250_samp0.01/UnsteadyFieldResults",
    ],
    [
        "parts2/modes300_samp0.00025/UnsteadyFieldResults",
        "parts2/modes300_samp0.000375/UnsteadyFieldResults",
        "parts2/modes300_samp0.0005/UnsteadyFieldResults",
        "parts2/modes300_samp0.00075/UnsteadyFieldResults",
        "parts3/modes300_samp0.001/UnsteadyFieldResults",
        "parts5/modes300_samp0.00175/UnsteadyFieldResults",
        "parts7/modes300_samp0.0025/UnsteadyFieldResults",
        "parts10/modes300_samp0.00375/UnsteadyFieldResults",
        "parts13/modes300_samp0.005/UnsteadyFieldResults",
        "parts20/modes300_samp0.0075/UnsteadyFieldResults",
        "parts26/modes300_samp0.01/UnsteadyFieldResults",
    ],

]

# dtStr = "dt2p5e-7"
# err_file_name = "l2_rel_sum_err_vs_raw_mag_20020_22000_20.dat"

# dtStr = "dt5e-7"
# err_file_name = "l2_rel_sum_err_vs_raw_mag_10010_11000_10.dat"

dtStr = "dt1e-6"
err_file_name = "l2_rel_sum_err_vs_raw_mag_5005_5500_5.dat"

##### Random #####

base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cvrc/ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_" + dtStr + "/mplsvt-real/implicit/k100/solutionModes/conservative/random"

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
    zbounds=zbounds,
    yscale=yscale,
    xlabel=xlabel,
    ylabel=ylabel,
    draw_colorbar=draw_colorbar,
    cb_ticks=cb_ticks,
    cb_ticklabels=cb_ticklabels,
    figsize=figsize,
)

##### Eigenvec #####

base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cvrc/ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_" + dtStr + "/mplsvt-real/implicit/k100/solutionModes/conservative/eigenvec"

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
    zbounds=zbounds,
    yscale=yscale,
    xlabel=xlabel,
    ylabel=ylabel,
    draw_colorbar=draw_colorbar,
    cb_ticks=cb_ticks,
    cb_ticklabels=cb_ticklabels,
    figsize=figsize,
)

##### GNAT Carlberg #####

base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cvrc/ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_" + dtStr + "/mplsvt-real/implicit/k100/solutionModes/conservative/greedy_carlberg"

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
    zbounds=zbounds,
    yscale=yscale,
    xlabel=xlabel,
    ylabel=ylabel,
    draw_colorbar=draw_colorbar,
    cb_ticks=cb_ticks,
    cb_ticklabels=cb_ticklabels,
    figsize=figsize,
)

##### GNAT Ben #####

base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cvrc/ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_" + dtStr + "/mplsvt-real/implicit/k100/solutionModes/conservative/greedy_ben"

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
    zbounds=zbounds,
    yscale=yscale,
    xlabel=xlabel,
    ylabel=ylabel,
    draw_colorbar=draw_colorbar,
    cb_ticks=cb_ticks,
    cb_ticklabels=cb_ticklabels,
    figsize=figsize,
)