import sys

sys.path.append("/p/work/chriswen/thesis/thesis_doc/scripts")
from plotProbes import plotProbes

base_dir = "/p/work/chriswen/CVRC_cutoff/unforced_dt1e-7/"
start_chunk = 6
end_chunk = 6
point_mon = 8
var_name = "Static_Pressure"
var_list = ["Static_Pressure"]
plot_colors = ["k", "g--", "b--", "r--", "m--"]
outdir = "/p/work/chriswen/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cvrc/deim"
time_fac = 1000.0
xbounds = [0.005, 0.0055]
ybounds = [1.23, 1.35]
press_factor = 1e6

legend_labels = ["FOM", "Random", "Eigenvector", "GNAT V1", "GNAT V2"]
legendloc = "upper left"
legend_fontsize = 14

# dt = 1e-6
data_dirs = [
    "FOM/PointResults",
    #"ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt1e-6/mplsvt-real/implicit/k100/solutionModes/conservative/random/parts5/modes300_samp0.00175/PointResults",
    #"ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt1e-6/mplsvt-real/implicit/k100/solutionModes/conservative/eigenvec/parts5/modes300_samp0.00175/PointResults",
    #"ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt1e-6/mplsvt-real/implicit/k100/solutionModes/conservative/greedy_carlberg/parts5/modes300_samp0.00175/PointResults",
    #"ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt1e-6/mplsvt-real/implicit/k100/solutionModes/conservative/greedy_ben/parts5/modes300_samp0.00175/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt1e-6/mplsvt-real/implicit/k100/solutionModes/conservative/random/parts7/modes300_samp0.0025/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt1e-6/mplsvt-real/implicit/k100/solutionModes/conservative/eigenvec/parts7/modes300_samp0.0025/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt1e-6/mplsvt-real/implicit/k100/solutionModes/conservative/greedy_carlberg/parts7/modes300_samp0.0025/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt1e-6/mplsvt-real/implicit/k100/solutionModes/conservative/greedy_ben/parts7/modes300_samp0.0025/PointResults",
]

outfile = "pressure_probe_deim_dt1e-6"
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

# dt = 5e-7
data_dirs = [
    "FOM/PointResults",
    #"ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k100/solutionModes/conservative/random/parts5/modes300_samp0.00175/PointResults",
    #"ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k100/solutionModes/conservative/eigenvec/parts5/modes300_samp0.00175/PointResults",
    #"ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k100/solutionModes/conservative/greedy_carlberg/parts5/modes300_samp0.00175/PointResults",
    #"ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k100/solutionModes/conservative/greedy_ben/parts5/modes300_samp0.00175/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k100/solutionModes/conservative/random/parts7/modes300_samp0.0025/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k100/solutionModes/conservative/eigenvec/parts7/modes300_samp0.0025/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k100/solutionModes/conservative/greedy_carlberg/parts7/modes300_samp0.0025/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k100/solutionModes/conservative/greedy_ben/parts7/modes300_samp0.0025/PointResults",
]

outfile = "pressure_probe_deim_dt5e-7"
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


# dt = 2.5e-7
data_dirs = [
    "FOM/PointResults",
    #"ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt2p5e-7/mplsvt-real/implicit/k100/solutionModes/conservative/random/parts5/modes300_samp0.00175/PointResults",
    #"ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt2p5e-7/mplsvt-real/implicit/k100/solutionModes/conservative/eigenvec/parts5/modes300_samp0.00175/PointResults",
    #"ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt2p5e-7/mplsvt-real/implicit/k100/solutionModes/conservative/greedy_carlberg/parts5/modes300_samp0.00175/PointResults",
    #"ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt2p5e-7/mplsvt-real/implicit/k100/solutionModes/conservative/greedy_ben/parts5/modes300_samp0.00175/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt2p5e-7/mplsvt-real/implicit/k100/solutionModes/conservative/random/parts7/modes300_samp0.0025/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt2p5e-7/mplsvt-real/implicit/k100/solutionModes/conservative/eigenvec/parts7/modes300_samp0.0025/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt2p5e-7/mplsvt-real/implicit/k100/solutionModes/conservative/greedy_carlberg/parts7/modes300_samp0.0025/PointResults",
    "ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt2p5e-7/mplsvt-real/implicit/k100/solutionModes/conservative/greedy_ben/parts7/modes300_samp0.0025/PointResults",
]

outfile = "pressure_probe_deim_dt2p5e-7"
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
