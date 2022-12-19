import sys
sys.path.append("/home/chris/Research/Papers/thesis/thesis_doc/scripts")
from plotError import plotErrorAvgVs


plot_type = 0
base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cvrc/ROMs/primitive/centIC_normL2_nonVelMag"

xvals_list = [
    [25, 50, 75, 100, 125, 150, 175, 200],
    [25, 50, 75, 100, 125, 150, 175, 200],
    [25, 50, 75, 100, 125, 150, 175, 200],
    [25, 50, 75, 100, 125, 150, 175, 200],
]
plot_colors = ['k', 'g', 'r', 'b']

ybounds = [8e-3, 1e-1]
xticks = None
xlabel = "Number of Modes"

plot_legend = True
legend_labels = [
    r"$\Delta \text{t} = \Delta \text{t}_{\text{FOM}}$",
    r"$\Delta \text{t} = 2.5 \times \Delta \text{t}_{\text{FOM}}$",
    r"$\Delta \text{t} = 5 \times \Delta \text{t}_{\text{FOM}}$",
    r"$\Delta \text{t} = 10 \times \Delta \text{t}_{\text{FOM}}$",
]
legend_loc = "upper right"
legend_fontsize = 14

plot_var = "Average"
out_dir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cvrc/unsampled"

##### dt = 1e-6 #####

data_dirs = [
    [
        "5p0ms_to_5p5ms_dt1e-7/mplsvt-real/implicit/k25/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt1e-7/mplsvt-real/implicit/k50/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt1e-7/mplsvt-real/implicit/k75/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt1e-7/mplsvt-real/implicit/k100/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt1e-7/mplsvt-real/implicit/k125/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt1e-7/mplsvt-real/implicit/k150/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt1e-7/mplsvt-real/implicit/k175/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt1e-7/mplsvt-real/implicit/k200/samp100p/UnsteadyFieldResults/",
    ],
    [
        "5p0ms_to_5p5ms_dt2p5e-7/mplsvt-real/implicit/k25/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt2p5e-7/mplsvt-real/implicit/k50/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt2p5e-7/mplsvt-real/implicit/k75/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt2p5e-7/mplsvt-real/implicit/k100/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt2p5e-7/mplsvt-real/implicit/k125/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt2p5e-7/mplsvt-real/implicit/k150/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt2p5e-7/mplsvt-real/implicit/k175/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt2p5e-7/mplsvt-real/implicit/k200/samp100p/UnsteadyFieldResults/",
    ],
    [
        "5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k25/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k50/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k75/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k100/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k125/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k150/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k175/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k200/samp100p/UnsteadyFieldResults/",
    ],
    [
        "5p0ms_to_5p5ms_dt1e-6/mplsvt-real/implicit/k25/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt1e-6/mplsvt-real/implicit/k50/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt1e-6/mplsvt-real/implicit/k75/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt1e-6/mplsvt-real/implicit/k100/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt1e-6/mplsvt-real/implicit/k125/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt1e-6/mplsvt-real/implicit/k150/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt1e-6/mplsvt-real/implicit/k175/samp100p/UnsteadyFieldResults/",
        "5p0ms_to_5p5ms_dt1e-6/mplsvt-real/implicit/k200/samp100p/UnsteadyFieldResults/",
    ],
]

iter_start_list = [
    [1001]*len(data_dirs[0]),
    [1001]*len(data_dirs[1]),
    [1001]*len(data_dirs[2]),
    [1001]*len(data_dirs[3]),
]
iter_end_list = [
    [1100]*len(data_dirs[0]),
    [1100]*len(data_dirs[1]),
    [1100]*len(data_dirs[2]),
    [1100]*len(data_dirs[3]),
]
iter_skip_list = [
    [1]*len(data_dirs[0]),
    [1]*len(data_dirs[1]),
    [1]*len(data_dirs[2]),
    [1]*len(data_dirs[3]),
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
