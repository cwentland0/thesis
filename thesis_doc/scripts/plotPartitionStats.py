import os

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

from dataExtractionFuncs import extractPartitionData, extractCommsFromASCIIMesh

mpl.rc('font', family='serif',size='14')
mpl.rc('axes', labelsize='x-large')
mpl.rc('figure', facecolor='w')
mpl.rc('text', usetex=True)
mpl.rc('text.latex',preamble=r'\usepackage{amsmath}')


def plotPartitionStats(
    base_dir,
    data_dirs,
    xvals_list,
    mesh_name,
    num_parts_spec,
    plot_colors,
    xlabel,
    out_dir,
    out_name,
    xbounds=None,
    xticks=None,
    ybounds_stats=None,
    ybounds_iblank=None,
    ybounds_comm=None,
    scale_cells=False,
    num_cells=None,
    legend_labels=None,
    legend_loc="best",
    legend_fontsize=12,
    yscale="log",
    xscale="log",
    
):
    # some logical checks
    num_lines = len(data_dirs)
    assert(len(xvals_list) == num_lines)
    if scale_cells:
        assert num_cells is not None

    num_points_list = [len(x) for x in data_dirs]
    for line_idx, line in enumerate(data_dirs):
        assert(len(xvals_list[line_idx]) == num_points_list[line_idx])

    outStatsFile = os.path.join(out_dir, out_name + "_partition_stats.png")
    outIBlankFile = os.path.join(out_dir, out_name + "_partition_iblank.png")
    outCommFile = os.path.join(out_dir, out_name + "_partition_comms.png")

    # set up figures/axes
    figStats = plt.figure()
    axStats = figStats.add_subplot(111)
    figIBlank = plt.figure()
    axIBlank = figIBlank.add_subplot(111)
    figComm = plt.figure()
    axComm = figComm.add_subplot(111)

    artistsStats = [None]*num_lines
    artistsIBlank = [None]*num_lines
    artistsComm = [None]*num_lines

    # loop over lines in plot
    for line_idx in range(num_lines):

        # average, min, max, std
        plotStatsVals = np.zeros((num_points_list[line_idx],4), dtype=np.float64)
        # iBlank type counts
        plotIBlankVals = np.zeros((num_points_list[line_idx],3), dtype=np.float64)
        # number of face communications
        plotCommVals = np.zeros((num_points_list[line_idx]), dtype=np.float64)

        # loop over data points in line
        for set_idx, set_path in enumerate(data_dirs[line_idx]):

            set_dir = os.path.join(base_dir, set_path)
            print(set_dir)

            # load partition data
            partitionFilePath = os.path.join(set_dir, "mesh_" + str(num_parts_spec), "partitionOutput.out")
            partitionDataIn = extractPartitionData(partitionFilePath)
            plotIBlankVals[set_idx,:] = partitionDataIn[0] 
            plotStatsVals[set_idx,:] = partitionDataIn[1]
            
            meshDir = os.path.join(set_dir, "mesh_" + str(num_parts_spec))
            plotCommVals[set_idx] = extractCommsFromASCIIMesh(meshDir, mesh_name, num_parts_spec)

        # scale cell counts by total mesh cell numbers			
        if scale_cells:
            plotIBlankVals /= num_cells
            plotStatsVals /= num_cells

        xVals = xvals_list[line_idx]

    ######### PLOT STATISTICS ##########

        plt.figure(figStats.number)

        # set up error bars for statistics
        yVals = plotStatsVals[:,2]

        # no bars
        artistsStats[line_idx], = axStats.plot(
            xVals,
            yVals,
            color=plot_colors[line_idx], 
            marker="o",
            linestyle='-'
        )

        # set axes
        axStats.set_yscale(yscale)
        axStats.set_xscale(xscale)
        axStats.xaxis.set_major_formatter(PercentFormatter(xmax=100.0,decimals=2))
        if scale_cells:
            axStats.set_ylabel("Cells per Partition, \% of Full Mesh")
            axStats.yaxis.set_major_formatter(PercentFormatter(xmax=1.0,decimals=2))
        else:
            axStats.set_ylabel("Cells per Partition")
        axStats.set_xlabel(xlabel)
        if xbounds is not None:
            axStats.set_xlim(xbounds)
        if ybounds_stats is not None:
            axStats.set_ylim(ybounds_stats)
        if xticks is not None:
            axStats.xaxis.set_ticks(xticks)
        

    ######### END STATISTICS ##########

        # plot iBlank
        plt.figure(figIBlank.number)
        artistsIBlank[line_idx], = axIBlank.plot(xVals,plotIBlankVals[:,0],color=plot_colors[line_idx],marker="o",linestyle='-')
        axIBlank.plot(xVals,plotIBlankVals[:,1],color=plot_colors[line_idx],marker="o",linestyle='--')
        axIBlank.plot(xVals,plotIBlankVals[:,2],color=plot_colors[line_idx],marker="o",linestyle='-.')
        axIBlank.set_yscale(yscale)
        axIBlank.set_xscale(xscale)
        axIBlank.xaxis.set_major_formatter(PercentFormatter(xmax=100.0,decimals=2))
        if scale_cells:
            axIBlank.set_ylabel("Number of Cells, % of Full Mesh")
            axIBlank.yaxis.set_major_formatter(PercentFormatter(xmax=1.0,decimals=2))
        else:
            axIBlank.set_ylabel("Number of Cells")
        axIBlank.set_xlabel(xlabel)	
        if xbounds is not None:
            axIBlank.set_xlim(xbounds)
        if ybounds_iblank is not None:
            axIBlank.set_ylim(ybounds_iblank)
        if xticks is not None:
            axStats.xaxis.set_ticks(xticks)

        # plot comms
        plt.figure(figComm.number)
        artistsComm[line_idx], = axComm.plot(
            xVals, 
            plotCommVals,
            color=plot_colors[line_idx],
            marker="o",
            linestyle='-'
        )
        axComm.set_ylabel("Number of MPI Communications")
        axComm.set_xlabel(xlabel)
        if yscale == "log":
            axComm.set_yscale("symlog")
        else:
            axComm.set_yscale("linear")
        axComm.set_xscale(xscale)
        axComm.xaxis.set_major_formatter(PercentFormatter(xmax=100.0,decimals=2))
        if xbounds is not None:
            axComm.set_xlim(xbounds)
        if ybounds_comm is not None:
            axComm.set_ylim(ybounds_comm)
        if xticks is not None:
            axComm.xaxis.set_ticks(xticks)
            
    # plot legends
    if legend_labels is not None: 
        axStats.legend(artistsStats, legend_labels, loc=legend_loc, framealpha=0.8, prop={'size':legend_fontsize})
        axIBlank.legend(artistsIBlank, legend_labels, loc=legend_loc, framealpha=0.8, prop={'size':legend_fontsize})
        axComm.legend(artistsComm, legend_labels, loc=legend_loc, framealpha=0.8, prop={'size':legend_fontsize})
            
    # tighten and save figures
    print("Saving images in " + out_dir)
    
    plt.figure(figStats.number)
    plt.tight_layout()
    plt.savefig(outStatsFile)

    plt.figure(figIBlank.number)
    plt.tight_layout()
    plt.savefig(outIBlankFile)

    plt.figure(figComm.number)
    plt.tight_layout()
    plt.savefig(outCommFile)


    print("Finished!")

def plotPartComparison(
    base_dir,
    mode_types,
    samp_percs,
    num_modes,
    num_parts,
    mesh_name,
    plot_colors,
    num_parts_list,
    xlabel,
    out_dir,
    out_name,
    line_styles=['-']*50,
    xscale="linear",
    yscale="log",
    xbounds=None,
    ybounds=None,
    xticks=None,
    legend_labels=None,
    legend_loc="best",
    legend_fontsize=12,
):

    # some logical checks
    num_mode_types = len(mode_types)
    numSampPercs = len(samp_percs)
    numLines = num_mode_types * numSampPercs
    assert(len(num_parts_list) == numLines)

    numPointsList = [len(x) for x in num_parts_list]

    out_file = os.path.join(out_dir, out_name+".png")

    # set up figures/axes
    fig = plt.figure()
    ax = fig.add_subplot(111)

    artists = []

    # loop over lines in plot
    lineIdx = 0
    for modeTypeIdx, modeType in enumerate(mode_types):

        for sampPercIdx, samp_perc in enumerate(samp_percs):

            # number of communications
            plotCommVals = np.zeros((numPointsList[lineIdx]), dtype=np.float64)
        
            # loop over data points in line
            for partsIdx, numParts in enumerate(num_parts_list[lineIdx]):
        
                meshDir = os.path.join(
                    base_dir,
                    modeType, 
                    "modes" + str(num_modes) + "_samp" + str(samp_perc),
                    "mesh_" + str(num_parts))
        
                print(meshDir)
        
                # load partition data
                plotCommVals[partsIdx] = extractCommsFromASCIIMesh(meshDir, mesh_name, numParts)
        
            # plot comms
            artistTemp, = ax.plot(
                num_parts_list[lineIdx],
                plotCommVals,
                color=plot_colors[modeTypeIdx],
                marker="o",
                linestyle=line_styles[sampPercIdx])

            if (sampPercIdx == 0): artists.append(artistTemp)
            
            lineIdx += 1


    ax.set_ylabel("Number of MPI Communications")
    ax.set_xlabel(xlabel)
    if (yscale == "log"):
        ax.set_yscale("symlog")
    else:
        ax.set_yscale("linear")
    ax.set_xscale(xscale)
    if xbounds is not None:
        ax.set_xlim(xbounds)
    if ybounds is not None:
        ax.set_ylim(ybounds)
    if xticks is not None:
        ax.xaxis.set_ticks(xticks)
        
    # plot legends
    if legend_labels is not None: 
        ax.legend(artists, legend_labels, loc=legend_loc, framealpha=0.8, prop={'size':legend_fontsize})
            

    plt.figure(fig.number)
    plt.tight_layout()
    print("Saving image to " + out_file)
    plt.savefig(out_file)