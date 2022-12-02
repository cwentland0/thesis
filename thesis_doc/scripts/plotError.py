import os

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc('font', family='serif',size='10')
mpl.rc('axes', labelsize='x-large')
mpl.rc('figure', facecolor='w')
mpl.rc('text', usetex=False)
mpl.rc('text.latex',preamble=r'\usepackage{amsmath}')

def plotErrorVsModesVars(
    base_dir,
    data_dirs,
    file_header,
    plot_vars,
    iter_start_list,
    iter_end_list,
    iter_skip_list,
    x_vals,
    plot_styles,
    outdir,
    xlog=False,
    xticks=None,
    ybounds=None,
    legend_labels=None,
    legend_loc="best",
    legend_font_size=12,
    num_legend_columns=1,
    outfile=None,
):

    assert(len(data_dirs) == len(x_vals))

    plot_vals = np.zeros((len(data_dirs), len(plot_vars)))

    fig = plt.figure()
    ax = fig.add_subplot(111)
    for file_iter, path in enumerate(data_dirs):

        file_name = file_header + "_" + str(iter_start_list[file_iter]) + "_" + str(iter_end_list[file_iter]) + "_" + str(iter_skip_list[file_iter]) + ".dat"
        data_path = os.path.join(base_dir, data_dirs[file_iter], file_name)

        print("Processing "+data_path)

        data_mat = np.loadtxt(data_path, dtype={'names':('labels', 'values'), 'formats':('|S30', float)})

        for idx in range(data_mat.shape[0]):
            var_name = data_mat[idx][0].decode('UTF-8')[:-1]
            if any([var_name == plot_var for plot_var in plot_vars]):
                insertIdx = plot_vars.index(var_name)
                plot_vals[file_iter,insertIdx] = data_mat[idx][1]

    for plot_idx in range(len(plot_vars)):
        if xlog:
            ax.loglog(x_vals, plot_vals[:,plot_idx], plot_styles[plot_idx], marker="o")
        else:
            ax.semilogy(x_vals, plot_vals[:,plot_idx], plot_styles[plot_idx], marker="o")


    if xticks is not None:
        ax.xaxis.set_ticks(xticks)
    if ybounds is not None:
        ax.set_ylim(ybounds)

    ax.set_xlabel("Number of Modes")
    if ((len(plot_vars) == 1) and (plot_vars[0] == "Average")):
        ax.set_ylabel(r'Average $\ell^2$ Error')
    else:
        ax.set_ylabel(r'Field $\ell^2$ Error')

    if legend_labels is not None:
        ax.legend(legend_labels,loc=legend_loc, framealpha=0.8, prop={'size':legend_font_size}, ncol=num_legend_columns)

    plt.tight_layout()

    if outfile is None:
        outfile = "error"
        for var in plot_vars:
            outfile += "_" + var

    outfile += ".png"
    outfile = os.path.join(outdir, outfile)
    print("Image saved to " + outfile)
    plt.savefig(outfile, format='png')