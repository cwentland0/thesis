import os

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedFormatter

mpl.rc('font', family='serif',size='10')
mpl.rc('axes', labelsize='x-large')
mpl.rc('figure', facecolor='w')
mpl.rc('text', usetex=False)
mpl.rc('text.latex',preamble=r'\usepackage{amsmath}')

def plotPODResEnergy(
    base_dir,
    pod_dirs,
    plot_colors,
    ubound,
    outdir,
    outfile=None,
    ybounds=None,
    zoom_loc=None,
    zoom_bounds_x=None,
    zoom_bounds_y=None,
    legend_labels=None,
    legend_loc="best",
):

    fig = plt.figure()
    ax = fig.add_subplot(111)
    if zoom_loc is not None:
        assert zoom_bounds_x is not None
        assert zoom_bounds_y is not None
        axins = ax.inset_axes(zoom_loc)

    for basisIdx, basisDir in enumerate(pod_dirs):

        print("Processing basis: "+basisDir)
        inFile = os.path.join(base_dir, basisDir, "S.txt")

        sVals = np.loadtxt(inFile)
        nVals = sVals.shape[0]
        sVals = sVals[1:]

        sumSq = np.sum(np.square(sVals))
        energy = np.zeros(nVals,dtype=np.float64)

        for i in range(nVals):
            energy[i] = 100.0 - 100.0*np.sum(np.square(sVals[:(i+1)]))/sumSq

        print("99%: "+str(np.where(energy < 1.0)[0][0]+1))
        print("99.9%: "+str(np.where(energy < 0.1)[0][0]+1))
        print("99.99%: "+str(np.where(energy < 0.01)[0][0]+1))

        ax.semilogy(range(1, ubound+1), energy[:ubound], plot_colors[basisIdx], linewidth=2)

        # inset zoom axes
        if zoom_loc is not None:
            axins.semilogy(range(1, ubound + 1), energy[:ubound], plot_colors[basisIdx], linewidth=2)

    ax.set_ylabel('POD Residual Energy, %')
    ax.set_xlabel('Number of Modes')
    if ybounds is not None:
        ax.set_ylim(ybounds)
    else:
        ax.set_ylim([None, 100.0])

    ax.set_xlim([0, ubound])

    if legend_labels is not None:
        ax.legend(legend_labels, loc=legend_loc, framealpha=1)

    plt.grid(visible=True, which='major', color='k')
    ax.yaxis.set_major_formatter(FixedFormatter(["0.001%","0.01%","0.1%","1%","10%","100%","1000%"]))
    plt.draw()
    hundredIdx = 1000
    for tickIdx, tickLabel in enumerate(reversed(ax.get_yticklabels())):
        if (tickLabel.get_text() == "$\\mathdefault{10^{2}}$"):
            hundredIdx = tickIdx
            tickLabel.set_text("100%")
        if (tickIdx == (hundredIdx+1)):
            tickLabel.set_text("10%")
        elif (tickIdx == (hundredIdx+2)):
            tickLabel.set_text("1%")
        elif (tickIdx == (hundredIdx+3)):
            tickLabel.set_text("0.1%")
        elif (tickIdx == (hundredIdx+4)):
            tickLabel.set_text("0.01%")
        elif (tickIdx == (hundredIdx+5)):
            tickLabel.set_text("0.001%")

    plt.tight_layout()

    if zoom_loc is not None:
        axins.set_xlim(zoom_bounds_x)
        axins.set_ylim(zoom_bounds_y)
        axins.set_xticklabels('')
        axins.set_yticklabels('')
        plt.setp(axins.get_yminorticklabels(), visible=False)
        ax.indicate_inset_zoom(axins, edgecolor='r', linewidth=2)

    if outfile is None:
        outfile = "S.png"
    else:
        outfile += ".png"
    plt.savefig(os.path.join(outdir, outfile))