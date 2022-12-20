import os

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from dataExtractionFuncs import extractValues

mpl.rc('font', family='serif',size='14')
mpl.rc('axes', labelsize='x-large')
mpl.rc('figure', facecolor='w')
mpl.rc('text', usetex=True)
mpl.rc('text.latex',preamble=r'\usepackage{amsmath}')

def plotErrContours(
    base_dir,
    data_dirs,
    err_file_name,
    xvals_list,
    yvals_list,
    plot_var,
    out_dir,
    out_name,
    draw_colorbar=False,
    cb_ticks=None,
    cb_ticklabels=None,
    zbounds=[None,None],
    xlabel=None,
    ylabel=None,
    xscale="linear",
    yscale="lienar",
    figsize=(6.4, 4.8),
    plot_point_markers=False,
    point_marker_coords=None,
    point_marker_colors=None,
    point_marker_styles=None,
):

    if plot_point_markers:
        assert point_marker_coords is not None
        assert point_marker_colors is not None
        assert point_marker_styles is not None
        assert len(point_marker_coords) == len(point_marker_colors)
        assert len(point_marker_coords) == len(point_marker_styles)


    if draw_colorbar is not None:
        if (cb_ticks is not None) and (cb_ticklabels is not None):
            assert len(cb_ticklabels) == len(cb_ticks)

    # check data_dirs dimension
    num_xvals = len(data_dirs)
    num_yvals = len(data_dirs[0])
    for dir_list in data_dirs:
        assert len(dir_list) == num_yvals
    assert len(xvals_list) == num_xvals
    assert len(yvals_list) == num_yvals

    plot_vals = np.zeros((num_xvals, num_yvals), dtype=np.float64)

    for xidx, xlist in enumerate(data_dirs):
        for yidx, ydir in enumerate(xlist):

            err_file = os.path.join(base_dir, ydir, err_file_name)
            plot_vals[xidx, yidx] = extractValues(err_file, plot_var)[0]

    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    cm = ax.pcolormesh(xvals_list, yvals_list, plot_vals.T,
        shading='nearest',
        norm=mpl.colors.LogNorm(vmin=zbounds[0], vmax=zbounds[1]),
        edgecolors="k", linewidth=0.5)

    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)
    ax.set_xscale(xscale)
    ax.set_yscale(yscale)
    ax.set_xticks(xvals_list)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y,pos: ('{{:.{:1d}f}}'.format(int(np.maximum(-np.log10(y),0)))).format(y)))

    if draw_colorbar:

        cb = fig.colorbar(cm, ax=ax, label=r"Average $\ell^2$ Error", extend="neither")
        if cb_ticks is not None:
            if cb_ticklabels is not None:
                cb.set_ticks(cb_ticks, minor=False, labels=cb_ticklabels)
                cb.set_ticks([], minor=True, labels=[])
            else:
                cb.set_ticks(cb_ticks, minor=False)
            cb.minorticks_on()

    if plot_point_markers:
        for point_idx, point_coords in enumerate(point_marker_coords):
            ax.plot(point_coords[0], point_coords[1],
                color=point_marker_colors[point_idx],
                marker=point_marker_styles[point_idx],
                markersize=8)

    plt.tight_layout()
    outfile = os.path.join(out_dir, out_name + ".png")
    print("Saving image to " + outfile)
    plt.savefig(outfile)
