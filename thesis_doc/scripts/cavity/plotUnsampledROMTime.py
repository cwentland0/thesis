import sys
sys.path.append("/home/chris/Research/Papers/thesis/thesis_doc/scripts")

import numpy as np

from plotError import plotErrorAvgVs


plot_type = 1
time_type = 2

base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cavity/ROMs"

xvals_list = [
    [25, 50, 75, 100, 125, 150, 175, 200],
    [25, 50, 75, 100, 125, 150, 175, 200],
    [25, 50, 75, 100, 125, 150, 175, 200],
    [25, 50, 75, 100, 125, 150, 175, 200],
]

cores_list = [
    [120, 120, 120, 120, 120, 120, 120, 120],
    [120, 120, 120, 120, 120, 120, 120, 120],
    [120, 120, 120, 120, 120, 120, 120, 120],
    [120, 120, 120, 120, 120, 120, 120, 120],
]
num_cores_FOM = 120
fom_cpu_hours_calc = np.array([371.776565253735*10, 395.686930656433*10, 296.471246242523*10, 22.1765227158880*10])
fom_cpu_hours_mpi = np.array([70.7120964904626*10, 146.679129362106*10, 46.9130725860596*10, 22.3457623936093*10])

plot_colors = ["g", "b", "r", "c"]
line_styles = ['-', '-', '-', '-']

ybounds = [5e-2, 50]
xticks = None
xlabel = r"$N_p$"

plot_legend = True
legend_labels = [
    r"$\Delta \text{t} = \Delta \text{t}_{\text{FOM}}$",
    r"$\Delta \text{t} = 2.5 \times \Delta \text{t}_{\text{FOM}}$",
    r"$\Delta \text{t} = 5 \times \Delta \text{t}_{\text{FOM}}$",
    r"$\Delta \text{t} = 10 \times \Delta \text{t}_{\text{FOM}}$",

]
legend_loc = "upper right"
legend_fontsize = 14

out_dir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cavity/unsampled"

data_dirs = [
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

iter_start_list = []
iter_end_list = []
iter_skip_list = []
plot_var = "time"

out_name = "unsampled_modeStudy"

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
    time_type=time_type,
    num_cores_FOM=num_cores_FOM,
    fom_cpu_hours_calc=fom_cpu_hours_calc,
    fom_cpu_hours_mpi=fom_cpu_hours_mpi,
    cores_list=cores_list,
    xscale="linear",
    yscale="log",
    ybounds=ybounds,
    xticks=xticks,
    plot_legend=plot_legend,
    legend_labels=legend_labels,
    legend_loc=legend_loc,
    legend_fontsize=legend_fontsize,
    line_styles=line_styles,
)
