import sys
sys.path.append("/home/chris/Research/Papers/thesis/thesis_doc/scripts")
from plotError import plotErrorAvgVs


plot_type = 0
base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cavity/ROMs"

xvals_list = [
    [25, 50, 75, 100, 125, 150, 175, 200],
    [25, 50, 75, 100, 125, 150, 175, 200],
    [25, 50, 75, 100, 125, 150, 175, 200],
]
plot_colors = ['g', 'r', 'b']

ybounds = [1e-3, 1e-1]
xticks = None
xlabel = r"$N_c, N_p$"

plot_legend = True
legend_labels = [
    "Galerkin",
    "LSPG",
    "MP-LSVT",
]
legend_loc = "upper left"
legend_fontsize = 14

plot_var = "Average"
out_dir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cavity/unsampled"

##### dt = 1e-6 #####

data_dirs = [
    [
        "conservative/100ms_to_110ms_samp1_dt1e-6/galerkin/implicit/k25/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-6/galerkin/implicit/k50/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-6/galerkin/implicit/k75/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-6/galerkin/implicit/k100/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-6/galerkin/implicit/k125/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-6/galerkin/implicit/k150/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-6/galerkin/implicit/k175/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-6/galerkin/implicit/k200/samp100p/UnsteadyFieldResults",
    ],
    [
        "conservative/100ms_to_110ms_samp1_dt1e-6/lspg/implicit/k25/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-6/lspg/implicit/k50/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-6/lspg/implicit/k75/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-6/lspg/implicit/k100/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-6/lspg/implicit/k125/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-6/lspg/implicit/k150/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-6/lspg/implicit/k175/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-6/lspg/implicit/k200/samp100p/UnsteadyFieldResults",
    ],
    [
        "primitive/100ms_to_110ms_samp1_dt1e-6/mplsvt-real/implicit/k25/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt1e-6/mplsvt-real/implicit/k50/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt1e-6/mplsvt-real/implicit/k75/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt1e-6/mplsvt-real/implicit/k100/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt1e-6/mplsvt-real/implicit/k125/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt1e-6/mplsvt-real/implicit/k150/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt1e-6/mplsvt-real/implicit/k175/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt1e-6/mplsvt-real/implicit/k200/samp100p/UnsteadyFieldResults",
    ],
]

iter_start_list = [
    [2501]*len(data_dirs[0]),
    [2501]*len(data_dirs[1]),
    [2501]*len(data_dirs[2]),
]
iter_end_list = [
    [2750]*len(data_dirs[0]),
    [2750]*len(data_dirs[1]),
    [2750]*len(data_dirs[2]),
]
iter_skip_list = [
    [1]*len(data_dirs[0]),
    [1]*len(data_dirs[1]),
    [1]*len(data_dirs[2]),
]

out_name = "unsampled_dt1e-6"

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

##### dt = 2.5e-6 #####

out_name = "unsampled_dt2p5e-6"
plot_legend = False

data_dirs = [
    [
        "conservative/100ms_to_110ms_samp1_dt2p5e-6/galerkin/implicit/k25/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt2p5e-6/galerkin/implicit/k50/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt2p5e-6/galerkin/implicit/k75/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt2p5e-6/galerkin/implicit/k100/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt2p5e-6/galerkin/implicit/k125/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt2p5e-6/galerkin/implicit/k150/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt2p5e-6/galerkin/implicit/k175/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt2p5e-6/galerkin/implicit/k200/samp100p/UnsteadyFieldResults",
    ],
    [
        "conservative/100ms_to_110ms_samp1_dt2p5e-6/lspg/implicit/k25/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt2p5e-6/lspg/implicit/k50/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt2p5e-6/lspg/implicit/k75/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt2p5e-6/lspg/implicit/k100/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt2p5e-6/lspg/implicit/k125/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt2p5e-6/lspg/implicit/k150/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt2p5e-6/lspg/implicit/k175/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt2p5e-6/lspg/implicit/k200/samp100p/UnsteadyFieldResults",
    ],
    [
        "primitive/100ms_to_110ms_samp1_dt2p5e-6/mplsvt-real/implicit/k25/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt2p5e-6/mplsvt-real/implicit/k50/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt2p5e-6/mplsvt-real/implicit/k75/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt2p5e-6/mplsvt-real/implicit/k100/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt2p5e-6/mplsvt-real/implicit/k125/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt2p5e-6/mplsvt-real/implicit/k150/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt2p5e-6/mplsvt-real/implicit/k175/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt2p5e-6/mplsvt-real/implicit/k200/samp100p/UnsteadyFieldResults",
    ],
]


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

##### dt = 5e-6 #####

out_name = "unsampled_dt5e-6"
plot_legend = False

data_dirs = [
    [
        "conservative/100ms_to_110ms_samp1_dt5e-6/galerkin/implicit/k25/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt5e-6/galerkin/implicit/k50/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt5e-6/galerkin/implicit/k75/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt5e-6/galerkin/implicit/k100/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt5e-6/galerkin/implicit/k125/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt5e-6/galerkin/implicit/k150/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt5e-6/galerkin/implicit/k175/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt5e-6/galerkin/implicit/k200/samp100p/UnsteadyFieldResults",
    ],
    [
        "conservative/100ms_to_110ms_samp1_dt5e-6/lspg/implicit/k25/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt5e-6/lspg/implicit/k50/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt5e-6/lspg/implicit/k75/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt5e-6/lspg/implicit/k100/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt5e-6/lspg/implicit/k125/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt5e-6/lspg/implicit/k150/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt5e-6/lspg/implicit/k175/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt5e-6/lspg/implicit/k200/samp100p/UnsteadyFieldResults",
    ],
    [
        "primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k25/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k50/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k75/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k100/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k125/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k150/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k175/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k200/samp100p/UnsteadyFieldResults",
    ],
]

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

##### dt = 1e-5 #####

out_name = "unsampled_dt1e-5"
plot_legend = False

data_dirs = [
    [
        "conservative/100ms_to_110ms_samp1_dt1e-5/galerkin/implicit/k25/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-5/galerkin/implicit/k50/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-5/galerkin/implicit/k75/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-5/galerkin/implicit/k100/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-5/galerkin/implicit/k125/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-5/galerkin/implicit/k150/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-5/galerkin/implicit/k175/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-5/galerkin/implicit/k200/samp100p/UnsteadyFieldResults",
    ],
    [
        "conservative/100ms_to_110ms_samp1_dt1e-5/lspg/implicit/k25/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-5/lspg/implicit/k50/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-5/lspg/implicit/k75/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-5/lspg/implicit/k100/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-5/lspg/implicit/k125/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-5/lspg/implicit/k150/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-5/lspg/implicit/k175/samp100p/UnsteadyFieldResults",
        "conservative/100ms_to_110ms_samp1_dt1e-5/lspg/implicit/k200/samp100p/UnsteadyFieldResults",
    ],
    [
        "primitive/100ms_to_110ms_samp1_dt1e-5/mplsvt-real/implicit/k25/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt1e-5/mplsvt-real/implicit/k50/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt1e-5/mplsvt-real/implicit/k75/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt1e-5/mplsvt-real/implicit/k100/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt1e-5/mplsvt-real/implicit/k125/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt1e-5/mplsvt-real/implicit/k150/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt1e-5/mplsvt-real/implicit/k175/samp100p/UnsteadyFieldResults",
        "primitive/100ms_to_110ms_samp1_dt1e-5/mplsvt-real/implicit/k200/samp100p/UnsteadyFieldResults",
    ],
]

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