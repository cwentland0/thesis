import sys

sys.path.append("/p/work/chriswen/thesis/thesis_doc/scripts")
from plotProbes import plotProbes

base_dir = "/p/work/chriswen/2d_cavity"
start_chunk = 101
end_chunk = 110
point_mon = 8
var_name = "Static_Pressure"
var_list = ["Static_Pressure"]
outdir = "/p/work/chriswen/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cavity/deim"
time_fac = 1000.0
xbounds = [0.1, 0.11]
ybounds = [22, 28]
press_factor = 1

legendloc = "upper left"
legend_fontsize = 12

plot_colors = ["k", "g--", "b--", "r--", "m--"]
legend_labels = ["FOM", "Random", "Eigenvector", "GNAT V1", "GNAT V2"]

# 2.5%
data_dirs = [
    "FOM/PointResults",
    "ROMs/primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k150/solutionModes/conservative/random/parts3/modes250_samp0.025/PointResults",
    "ROMs/primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k150/solutionModes/conservative/eigenvec/parts3/modes250_samp0.025/PointResults",
    "ROMs/primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k150/solutionModes/conservative/greedy_carlberg/parts3/modes250_samp0.025/PointResults",
    "ROMs/primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k150/solutionModes/conservative/greedy_ben/parts3/modes250_samp0.025/PointResults",
]

outfile = "pressure_probe_deim_2p5"
plot_legend = True

plotProbes(
    base_dir,
    data_dirs,
    start_chunk,
    end_chunk,
    point_mon,
    var_name,
    var_list,
    plot_colors,
    outdir,
    time_fac=time_fac,
    press_factor=press_factor,
    legend_labels=legend_labels,
    plot_legend=plot_legend,
    legendloc=legendloc,
    legend_fontsize=legend_fontsize,
    outfile=outfile,
    xbounds=xbounds,
    ybounds=ybounds,
)

# 1%
data_dirs = [
    "FOM/PointResults",
    "ROMs/primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k150/solutionModes/conservative/random/parts2/modes250_samp0.01/PointResults",
    "ROMs/primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k150/solutionModes/conservative/eigenvec/parts2/modes250_samp0.01/PointResults",
    "ROMs/primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k150/solutionModes/conservative/greedy_carlberg/parts2/modes250_samp0.01/PointResults",
    "ROMs/primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k150/solutionModes/conservative/greedy_ben/parts2/modes250_samp0.01/PointResults",
]

outfile = "pressure_probe_deim_1"
plot_legend = False

plotProbes(
    base_dir,
    data_dirs,
    start_chunk,
    end_chunk,
    point_mon,
    var_name,
    var_list,
    plot_colors,
    outdir,
    time_fac=time_fac,
    press_factor=press_factor,
    legend_labels=legend_labels,
    plot_legend=plot_legend,
    legendloc=legendloc,
    legend_fontsize=legend_fontsize,
    outfile=outfile,
    xbounds=xbounds,
    ybounds=ybounds,
)
