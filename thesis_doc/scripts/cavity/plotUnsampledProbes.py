import sys

sys.path.append("/p/work/chriswen/thesis/thesis_doc/scripts")
from plotProbes import plotProbes

base_dir = "/p/work/chriswen/2d_cavity"
start_chunk = 101
end_chunk = 110
point_mon = 8
var_name = "Static_Pressure"
var_list = ["Static_Pressure"]
outdir = "/p/work/chriswen/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cavity/unsampled"
time_fac = 1000.0
xbounds = [0.1, 0.11]
ybounds = [22, 28]
press_factor = 1

legendloc = "upper left"
legend_fontsize = 14

# Method study
data_dirs = [
    "FOM/PointResults",
    "ROMs/conservative/100ms_to_110ms_samp1_dt5e-6/galerkin/implicit/k150/samp100p/PointResults",
    "ROMs/conservative/100ms_to_110ms_samp1_dt5e-6/lspg/implicit/k150/samp100p/PointResults",
    "ROMs/primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k150/samp100p/PointResults",
]

plot_colors = ["k", "g--", "r--", "b--"]
legend_labels = ["FOM", "Galerkin", "LSPG", "MP-LSVT"]
outfile = "pressure_probe_unsampled_methods"
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

# Mode study
data_dirs = [
    "FOM/PointResults",
    "ROMs/primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k25/samp100p/PointResults",
    "ROMs/primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k50/samp100p/PointResults",
    "ROMs/primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k75/samp100p/PointResults",
    #"ROMs/primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k100/samp100p/PointResults",
    #"ROMs/primitive/100ms_to_110ms_samp1_dt5e-6/mplsvt-real/implicit/k150/samp100p/PointResults",
]

plot_colors = ["k", "g--", "r--", "b--"]
legend_labels = [
    "FOM",
    r"$N_p = 25$",
    r"$N_p = 50$",
    r"$N_p = 75$",
]
outfile = "pressure_probe_unsampled_modes"
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
