import sys
sys.path.append("/home/chris/Research/Papers/thesis/thesis_doc/scripts")
from samplingTiming import plotSamplingTiming

base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cvrc/PODBases/deimBases/solutionModes/conservative"

fom_cores = 880
fom_time = 9.5282998
samp_cores = 121

samp_type_list = ["random", "eigenvec", "greedy_carlberg", "greedy_ben"]
samp_rate_list = [0.00025, 0.000375, 0.0005, 0.00075, 0.001, 0.00175, 0.0025, 0.00375, 0.005, 0.0075, 0.01]
num_modes_list = [300]

# 0: metric
# 1: unique
# 2: append
time_sum_idx_list = [
    [0],
    [0],
    [0,3],
    [0,3],
]

plot_styles = ["g", "b", "r", "m"]

legend_labels = ["Random", "Eigenvector", "GNAT V1", "GNAT V2"]
legend_loc = "upper left"
legend_fontsize = 14

out_dir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cvrc/deim"
out_name = "temp"


# w/r/t sampling rate
plot_legend = True
xlabel = "Sampling Rate, \%"
xvar = "samp_rate"
xbounds = [1e-2, 2]
ybounds = [7e-4, 1000]

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
)