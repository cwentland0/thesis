import sys
sys.path.append("/home/chris/Research/Papers/thesis/thesis_doc/scripts")
from plotError import plotErrorAvgVs


plot_type = 0
base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/9elem/ROMs/primitive/centIC_normL2_nonVelMag"

xvals_list = [
    [20, 40, 60, 80, 100],
    [20, 40, 60, 80, 100],
]
plot_colors = ['k', 'g', 'r', 'b']

# ybounds = [8e-3, 1e-1]
ybounds = None
xticks = None
xlabel = r"$N_p$"

plot_legend = True
legend_labels = [
    # r"$\Delta \text{t} = 2.5 \times \Delta \text{t}_{\text{FOM}}$",
    r"$\Delta \text{t} = 5 \times \Delta \text{t}_{\text{FOM}}$",
    r"$\Delta \text{t} = 10 \times \Delta \text{t}_{\text{FOM}}$",
]
legend_loc = "upper right"
legend_fontsize = 14

# plot_var = "Average"
# plot_var = "Static_Pressure"
# plot_var = "UVWMag"
# plot_var = "Temperature"
# plot_var = "CH4_mf"
# plot_var = "O2_mf"
# plot_var = "CO_mf"
# plot_var = "CO2_mf"
plot_var = "H2O_mf"
out_dir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/NineElement/Images/unsampled"

##### dt = 1e-6 #####

data_dirs = [
    [
        "21p5ms_to_21p89ms_samp10_dt5e-7/mplsvt-real/implicit/k20/samp100p/UnsteadyFieldResults/",
        "21p5ms_to_21p89ms_samp10_dt5e-7/mplsvt-real/implicit/k40/samp100p/UnsteadyFieldResults/",
        "21p5ms_to_21p89ms_samp10_dt5e-7/mplsvt-real/implicit/k60/samp100p/UnsteadyFieldResults/",
        "21p5ms_to_21p89ms_samp10_dt5e-7/mplsvt-real/implicit/k80/samp100p/UnsteadyFieldResults/",
        "21p5ms_to_21p89ms_samp10_dt5e-7/mplsvt-real/implicit/k100/samp100p/UnsteadyFieldResults/",
    ],
    [
        "21p5ms_to_21p89ms_samp10_dt1e-6/mplsvt-real/implicit/k20/samp100p/UnsteadyFieldResults/",
        "21p5ms_to_21p89ms_samp10_dt1e-6/mplsvt-real/implicit/k40/samp100p/UnsteadyFieldResults/",
        "21p5ms_to_21p89ms_samp10_dt1e-6/mplsvt-real/implicit/k60/samp100p/UnsteadyFieldResults/",
        "21p5ms_to_21p89ms_samp10_dt1e-6/mplsvt-real/implicit/k80/samp100p/UnsteadyFieldResults/",
        "21p5ms_to_21p89ms_samp10_dt1e-6/mplsvt-real/implicit/k100/samp100p/UnsteadyFieldResults/",
    ],
]

iter_start_list = [
    [4301]*len(data_dirs[0]),
    [4301]*len(data_dirs[1]),
]
iter_end_list = [
    [4378]*len(data_dirs[0]),
    [4378]*len(data_dirs[1]),
]
iter_skip_list = [
    [1]*len(data_dirs[0]),
    [1]*len(data_dirs[1]),
]

out_name = "unsampled_avg_mode"

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
    vs_raw=True,
    mags=True,
    xscale="linear",
    yscale="log",
    ybounds=ybounds,
    xticks=xticks,
    plot_legend=plot_legend,
    legend_labels=legend_labels,
    legend_loc=legend_loc,
    legend_fontsize=legend_fontsize,
)
