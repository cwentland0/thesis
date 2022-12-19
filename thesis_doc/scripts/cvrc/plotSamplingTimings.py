import sys
sys.path.append("/home/chris/Research/Papers/thesis/thesis_doc/scripts")
from samplingTiming import plotSamplingTiming

base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cvrc/PODBases/deimBases/solutionModes/conservative"

fom_cores = 880
fom_time = 9.5282998
samp_cores = 121

samp_type_list = ["random", "eigenvec", "greedy_carlberg", "greedy_ben"]
samp_rate_list = [0.00025, 0.000375, 0.0005, 0.00075, 0.001, 0.00175, 0.0025, 0.00375, 0.005, 0.0075, 0.01]

# 0: metric
# 1: unique
# 2: append
time_sum_idx_list = [
    [0],
    [0],
    [0],
    [0],
]

plot_styles = ["g", "b", "r", "m"]

legend_labels = ["Random", "Eigenvector", "GNAT V1", "GNAT V2"]
legend_loc = "upper left"
legend_fontsize = 14

out_dir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cvrc/deim"


# w/r/t sampling rate
num_modes_list = [300]

plot_legend = True
xlabel = "Sampling Rate, \%"
xvar = "samp_rate"
xbounds = [1e-2, 2]
ybounds = [7e-4, 1000]

plot_slopeline = True
slopeline_x = [0.025, 1]
slopeline_y = [1, 40]
slopeline_text = r'$m=10^{N_s}$'
slopeline_angle = 15
slopeline_coords = [0.2, 3]

out_name = "samp_timing_wrt_samprate"

plotSamplingTiming(
    base_dir,
    samp_type_list,
    samp_rate_list,
    num_modes_list,
    time_sum_idx_list,
    plot_styles,
    xvar,
    xlabel,
    out_dir,
    out_name,
    fom_time,
    fom_cores,
    samp_cores,
    ybounds=ybounds,
    xbounds=xbounds,
    plot_legend=plot_legend,
    legend_labels=legend_labels,
    legend_loc=legend_loc,
    legend_fontsize=legend_fontsize,
    plot_slopeline=plot_slopeline,
    slopeline_x=slopeline_x,
    slopeline_y=slopeline_y,
    slopeline_text=slopeline_text,
    slopeline_coords=slopeline_coords,
    slopeline_angle=slopeline_angle,
)

# w/r/t sampling rate
num_modes_list = [100, 150, 200, 250, 300]

time_sum_idx_list = [
    [0],
    [0],
    [0,2],
    [0,2],
]

plot_legend = False
xlabel = r"$N_r$"
xvar = "num_modes"
ybounds = [7e-4, 100]
xbounds = None

samp_rate_plot = 0.0025

plot_slopeline = False

out_name = "samp_timing_wrt_modes"

plotSamplingTiming(
    base_dir,
    samp_type_list,
    samp_rate_list,
    num_modes_list,
    time_sum_idx_list,
    plot_styles,
    xvar,
    xlabel,
    out_dir,
    out_name,
    fom_time,
    fom_cores,
    samp_cores,
    samp_rate_plot=samp_rate_plot,
    ybounds=ybounds,
    xbounds=xbounds,
    plot_legend=plot_legend,
    legend_labels=legend_labels,
    legend_loc=legend_loc,
    legend_fontsize=legend_fontsize,
    plot_slopeline=plot_slopeline,
    slopeline_x=slopeline_x,
    slopeline_y=slopeline_y,
    slopeline_text=slopeline_text,
    slopeline_coords=slopeline_coords,
    slopeline_angle=slopeline_angle,
)