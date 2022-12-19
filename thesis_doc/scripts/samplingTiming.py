import os
from math import log10, exp

import numpy as np
import matplotlib as mpl
from matplotlib import ticker
import matplotlib.pyplot as plt

from dataExtractionFuncs import extractSamplingTimeData

mpl.rc('font', family='serif',size='14')
mpl.rc('axes', labelsize='x-large')
mpl.rc('figure', facecolor='w')
mpl.rc('text', usetex=True)
mpl.rc('text.latex',preamble=r'\usepackage{amsmath}')

def plotSamplingTiming(
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
    samp_rate_plot=None,
    ybounds=None,
    xbounds=None,
    xticks=None,
    plot_legend=False,
    legend_labels=None,
    legend_loc="best",
    legend_fontsize=12,
    plot_slopeline=False,
    slopeline_x=None,
    slopeline_y=None,
    slopeline_text="",
    slopeline_angle=0,
    slopeline_coords=None,
):

    assert xvar in ["samp_rate", "num_modes"]
    if xvar == "samp_rate":
        assert len(num_modes_list) == 1
        xvals = samp_rate_list
    else:
        xvals = num_modes_list
        assert samp_rate_plot is not None
        plot_idx = samp_rate_list.index(samp_rate_plot)

    time_data = np.zeros((len(samp_rate_list), len(num_modes_list)), dtype=np.float64)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    for samp_type_idx, samp_type in enumerate(samp_type_list):

        time_sum_idxs = time_sum_idx_list[samp_type_idx]

        for samp_rate_idx, samp_rate in enumerate(samp_rate_list):

            for num_modes_idx, num_modes in enumerate(num_modes_list):

                time_file = os.path.join(base_dir, samp_type, "pinv_modes" + str(num_modes) + "_samp" + str(samp_rate), "timings.dat")

                metric_time, unique_time, append_time = extractSamplingTimeData(time_file, samp_type)

                if 0 in time_sum_idxs:
                    time_data[samp_rate_idx, num_modes_idx] += metric_time[0]
                if 1 in time_sum_idxs:
                    time_data[samp_rate_idx, num_modes_idx] += unique_time[0]
                if 2 in time_sum_idxs:
                    time_data[samp_rate_idx, num_modes_idx] += append_time[0]

        # eigenvec and GNAT V2 are cumulative
        if samp_type in ["eigenvec", "greedy_ben"]:
            time_data[:, :] = np.cumsum(time_data, axis=0)

        # scale by FOM time
        time_data = time_data * samp_cores / (fom_time * fom_cores)

        if xvar == "samp_rate":
            ax.loglog([xval * 100.0 for xval in xvals], time_data[:, 0], plot_styles[samp_type_idx], marker='o')
        else:
            ax.semilogy(xvals, time_data[plot_idx, :], plot_styles[samp_type_idx], marker='o')


    if plot_slopeline:
        if xvar == "samp_rate":
            ax.loglog(slopeline_x, slopeline_y, 'k')
        else:
            ax.semilogy(slopeline_x, slopeline_y, 'k')

        plt.annotate(
            slopeline_text,
            slopeline_coords, xycoords='data',
            ha='center', va='bottom',
            rotation=15,
            rotation_mode='anchor',
        )

    if xvar == "samp_rate":
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda y,pos: ('{{:.{:1d}f}}'.format(int(np.maximum(-np.log10(y),0)))).format(y)))

    if xlabel is not None:
        ax.set_xlabel(xlabel)
    ax.set_ylabel("Sampling Cost (FOM iters)")

    if xbounds is not None:
        ax.set_xlim(xbounds)
    if ybounds is not None:
        ax.set_ylim(ybounds)

    if plot_legend:
        ax.legend(legend_labels, loc=legend_loc, framealpha=0.8, prop={'size':legend_fontsize})

    plt.tight_layout()
    out_file = os.path.join(out_dir, out_name + ".png")
    print("Image saved to " + out_file)
    plt.savefig(out_file, format='png')

    print("Finished")