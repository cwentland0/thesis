import sys

sys.path.append("/p/work/chriswen/thesis/thesis_doc/scripts")
from plotProbes import plotProbes

base_dir = "/p/work/chriswen/CVRC_cutoff/unforced_dt1e-7/"
outdir = "/p/work/chriswen/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cvrc/unsampled"

start_chunk = 6
end_chunk = 6
xbounds = [0.005, 0.0055]

legendloc = "upper left"
legend_fontsize = 14

time_fac = 1000.0


##### PRESSURE #####

point_mon = 8
var_name = "Static_Pressure"
var_list = ["Static_Pressure"]
ybounds = [1.23, 1.35]
press_factor = 1e6

# Time step study
data_dirs = [
    "FOM/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt1e-7/mplsvt-real/implicit/k100/samp100p/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt2p5e-7/mplsvt-real/implicit/k100/samp100p/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k100/samp100p/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt1e-6/mplsvt-real/implicit/k100/samp100p/PointResults",
]
legend_labels = [
    "FOM",
    r"$\Delta \text{t} = \Delta \text{t}_{\text{FOM}}$",
    r"$\Delta \text{t} = 2.5 \times \Delta \text{t}_{\text{FOM}}$",
    r"$\Delta \text{t} = 5 \times \Delta \text{t}_{\text{FOM}}$",
    r"$\Delta \text{t} = 10 \times \Delta \text{t}_{\text{FOM}}$",
]
plot_colors = ["k", "g--", "b--", "r--", "c--"]

outfile = "pressure_probe_unsampled_time"
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
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k25/samp100p/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k50/samp100p/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k100/samp100p/PointResults",
]
legend_labels = [
    "FOM",
    r"$N_p = 25$",
    r"$N_p = 50$",
    r"$N_p = 100$",
]
plot_colors = ["k", "g--", "b--", "r--"]

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

# LSPG
data_dirs = [
    "FOM/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt1e-7/mplsvt-real/implicit/k100/samp100p/PointResults",
    "ROMs/conservative/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt1e-7/lspg/implicit/k100/samp100p/PointResults",
    "ROMs/conservative/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt1e-7/lspg/implicit/k200/samp100p/PointResults",
]
legend_labels = [
    "FOM",
    r"MP-LSVT, $N_p = 100$",
    r"LSPG, $N_c = 100$",
    r"LSPG, $N_c = 200$",
]
plot_colors = ["k", "b--", "r--", "m--"]

outfile = "pressure_probe_unsampled_lspg"
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
    legendloc="upper right",
    legend_fontsize=legend_fontsize,
    outfile=outfile,
    xbounds=[0.005, 0.0051],
    ybounds=[1.24, 1.32],
)

##### HEAT RELEASE #####

var_name = "Heat_Release"
var_list = ["Heat_Release"]
hr_factor = 1e9
ybounds = [-200, 2500]
point_mon = 10

# Time step study
data_dirs = [
    "FOM/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt1e-7/mplsvt-real/implicit/k100/samp100p/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt2p5e-7/mplsvt-real/implicit/k100/samp100p/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k100/samp100p/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt1e-6/mplsvt-real/implicit/k100/samp100p/PointResults",
]
legend_labels = [
    "FOM",
    r"$\Delta \text{t} = \Delta \text{t}_{\text{FOM}}$",
    r"$\Delta \text{t} = 2.5 \times \Delta \text{t}_{\text{FOM}}$",
    r"$\Delta \text{t} = 5 \times \Delta \text{t}_{\text{FOM}}$",
    r"$\Delta \text{t} = 10 \times \Delta \text{t}_{\text{FOM}}$",
]
plot_colors = ["k", "g--", "b--", "r--", "c--"]

outfile = "heat_probe_unsampled_time"
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
    hr_factor=hr_factor,
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
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k25/samp100p/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k50/samp100p/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k100/samp100p/PointResults",
]
legend_labels = [
    "FOM",
    r"$N_p = 25$",
    r"$N_p = 50$",
    r"$N_p = 100$",
]
plot_colors = ["k", "g--", "b--", "r--"]


outfile = "heat_probe_unsampled_modes"
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
    hr_factor=hr_factor,
    legend_labels=legend_labels,
    plot_legend=plot_legend,
    legendloc=legendloc,
    legend_fontsize=legend_fontsize,
    outfile=outfile,
    xbounds=xbounds,
    ybounds=ybounds,
)
