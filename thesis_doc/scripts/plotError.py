import os

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from dataExtractionFuncs import extractSolverWalltimeStats, extractIntError

mpl.rc('font', family='serif',size='14')
mpl.rc('axes', labelsize='x-large')
mpl.rc('figure', facecolor='w')
mpl.rc('text', usetex=True)
mpl.rc('text.latex',preamble=r'\usepackage{amsmath}')

def plotErrorAvgVs(
    plot_type,
    base_dir,
    data_dirs,
    iter_start_list,
    iter_end_list,
    iter_skip_list,
    xvals_list,
    plot_var,
    plot_colors,
    xlabel,
    out_dir,
    out_name,
    cores_list=None,
    num_cores_FOM=None,
    fom_cpu_hours_calc=None,
    fom_cpu_hours_mpi=None,
    vs_raw=True,
    time_type=2,
    plot_walltime=False,
    mags=False,
    calc_time_ratio=True,
    xscale="linear",
    yscale="linear",
    ybounds=None,
    xbounds=None,
    xbounds_wall=None,
    xticks=None,
    plot_legend=False,
    legend_labels=None,
    legend_loc="best",
    legend_fontsize=12,
    marker_types=['o']*50,
    line_styles=['-']*50,
    marker_sizes=[6]*50,
    plot_point_markers=False,
    point_marker_idxs=None,
    point_marker_styles=None,
    point_marker_size=6,
):

    if plot_point_markers:
        assert point_marker_idxs is not None
        assert point_marker_styles is not None
        assert len(point_marker_idxs) == len(point_marker_styles)

    if plot_legend:
        assert legend_labels is not None

    if plot_type > 0:
        assert cores_list is not None
        assert num_cores_FOM is not None
        assert fom_cpu_hours_calc is not None
        assert fom_cpu_hours_mpi is not None

    # some logical checks
    numLines = len(data_dirs)
    if (plot_type != 1):
        assert(len(iter_start_list) == numLines)
        assert(len(iter_end_list) == numLines)
        assert(len(iter_end_list) == numLines)
    if plot_type > 0:
        assert cores_list is not None
        assert len(cores_list) == numLines
    assert(len(xvals_list) == numLines)
    xvals_list = [np.array(xvals_entry) for xvals_entry in xvals_list]

    num_points_list = [len(x) for x in data_dirs]
    for lineIdx, line in enumerate(data_dirs):
        if (plot_type != 1):
            assert(len(iter_start_list[lineIdx]) == num_points_list[lineIdx])
            assert(len(iter_end_list[lineIdx]) == num_points_list[lineIdx])
            assert(len(iter_skip_list[lineIdx]) == num_points_list[lineIdx])
        if (plot_type > 0):
            assert(len(cores_list[lineIdx]) == num_points_list[lineIdx])
        assert(len(xvals_list[lineIdx]) == num_points_list[lineIdx])

    if vs_raw:
        err_string = "_errorRaw"
    else:
        err_string = "_errProj"

    if time_type == 0:
        time_string = "_time_calcOnly"
    elif (time_type == 1):
        time_string = "_time_MPIOnly"
    elif (time_type == 2):
        time_string = "_time_calcAndMPI"

    fig = plt.figure()
    out_file = os.path.join(out_dir, out_name)
    if (plot_type == 0):
        out_file += ("_" + plot_var + err_string)
        axErr = fig.add_subplot(111)
        axErrStyle = '-'
    elif (plot_type == 1):
        out_file += time_string
        axTime = fig.add_subplot(111)
        if plot_walltime:
            axTimeWall = axTime.twinx()
        axTimeStyle = '-'
    elif (plot_type == 2):
        out_file += ("_" + plot_var + err_string + time_string)
        axErr = fig.add_subplot(111)
        axTime = axErr.twinx()
        axErrStyle = '-'
        axTimeStyle = '--'
    elif (plot_type == 3):
        out_file += ("_" + plot_var + err_string + "_pareto")
        axTime = fig.add_subplot(111)
        axTimeStyle = '-'
    else:
        raise ValueError("Invalid choice for plot_type: "+str(plot_type))
    out_file += ".png"

    artist_list = []

    # loop over lines in plot
    for lineIdx in range(numLines):

        # average, min, max, std
        if (plot_type > 0):
            plot_time_vals = np.zeros((num_points_list[lineIdx],3,4), dtype=np.float64)
            plot_time_vals_wall = np.zeros((num_points_list[lineIdx],3,4), dtype=np.float64)

        # error values at each
        if ((plot_type == 0) or (plot_type == 2) or (plot_type)):
            plotErrVals = np.zeros(num_points_list[lineIdx], dtype=np.float64)

        # loop over data points in line
        for setIdx, setPath in enumerate(data_dirs[lineIdx]):

            setDir = os.path.join(base_dir, setPath)

            if (plot_type > 0):
                # load timing data
                timeFilePath = os.path.join(setDir, "../wall_time.dat")
                plot_time_vals_wall[setIdx, :, :] = extractSolverWalltimeStats(timeFilePath)

                # scale timings by number of cores
                plot_time_vals[setIdx, :, :] = plot_time_vals_wall[setIdx,:,:]*cores_list[lineIdx][setIdx]

            if ((plot_type == 0) or (plot_type == 2) or (plot_type == 3)):
                # load error data
                plotErrVals[setIdx] = extractIntError(setDir, iter_start_list[lineIdx][setIdx], iter_end_list[lineIdx][setIdx], iter_skip_list[lineIdx][setIdx], plot_var, vs_raw, mags)[0]


        if (plot_type > 0):

            # get the required metrics
            if (time_type == 0):
                plotTimeMetric = plot_time_vals[:,0,:]
                plotTimeMetricWall = plot_time_vals_wall[:,0,:]
                plot_time_fom_wall = fom_cpu_hours_calc[0]
            elif (time_type == 1):
                plotTimeMetric = plot_time_vals[:,1,:]
                plotTimeMetricWall = plot_time_vals_wall[:,1,:]
                plot_time_fom_wall = fom_cpu_hours_mpi[0]
            elif (time_type == 2):
                plotTimeMetric = plot_time_vals[:,0,:] + plot_time_vals[:,1,:]
                plotTimeMetricWall = plot_time_vals_wall[:,0,:] + plot_time_vals_wall[:,1,:]
                plot_time_fom_wall = fom_cpu_hours_calc[0] + fom_cpu_hours_mpi[0]
            else:
                raise ValueError("Invalid entry for time_type: "+str(time_type))

            plotTimeFOM = plot_time_fom_wall * num_cores_FOM

            avgTimeVals = plotTimeMetric[:,0]
            maxTimeVals = plotTimeMetric[:,1]
            minTimeVals = plotTimeMetric[:,2]
            stdTimeVals = plotTimeMetric[:,3]

            avgTimeValsWall = plotTimeMetricWall[:,0]

            # if simulation failed, timing values returned as zero
            # fill with NaN I guess?
            avgTimeVals[avgTimeVals == 0] = np.nan
            maxTimeVals[maxTimeVals == 0] = np.nan
            minTimeVals[minTimeVals == 0] = np.nan
            stdTimeVals[stdTimeVals == 0] = np.nan

            avgTimeValsWall[avgTimeValsWall == 0] = np.nan

            if calc_time_ratio:
                if ((plot_type == 1) or (plot_type == 3)):
                    stdTimeVals = ((plotTimeFOM*avgTimeVals) - (plotTimeFOM*(avgTimeVals+stdTimeVals)))/(avgTimeVals*(avgTimeVals+stdTimeVals))
                    avgTimeVals = plotTimeFOM/avgTimeVals
                    maxTimeVals = plotTimeFOM/maxTimeVals
                    minTimeVals = plotTimeFOM/minTimeVals

                    avgTimeValsWall = plot_time_fom_wall / avgTimeValsWall

                else:
                    avgTimeVals /= plotTimeFOM
                    maxTimeVals /= plotTimeFOM
                    minTimeVals /= plotTimeFOM
                    stdTimeVals /= plotTimeFOM

            # some generalizations for Pareto fronts
            if (plot_type == 3):
                xVals = avgTimeVals
                yVals = plotErrVals

            else:
                xVals = xvals_list[lineIdx]
                yVals = avgTimeVals

            # deal with large errors and NaN
            if (plot_type != 1):
                yVals[yVals > 1.0] = 1.0
            nan_mask = np.isfinite(yVals)

            # no bars
            artistTemp, = axTime.plot(xVals[nan_mask], yVals[nan_mask],
                color=plot_colors[lineIdx],
                marker=marker_types[lineIdx], linestyle=line_styles[lineIdx], markersize=marker_sizes[lineIdx])
            artist_list.append(artistTemp)

            if plot_point_markers:
                if (xVals.shape[0] > 1):
                    for idx, marker_idx in enumerate(point_marker_idxs):
                        axTime.plot(xVals[marker_idx], yVals[marker_idx],
                            color=plot_colors[lineIdx],
                            marker=point_marker_styles[idx],
                            markeredgecolor="k",
                            markersize=point_marker_size)

            if plot_walltime:
                if (num_points_list[lineIdx] == 1):
                    marker_types[lineIdx] = 10
                artistTemp, = axTimeWall.plot(xVals, avgTimeValsWall, color=plot_colors[lineIdx],
                    marker=marker_types[lineIdx], linestyle=line_styles[lineIdx], markersize=marker_sizes[lineIdx])
                if (num_points_list[lineIdx] == 1):
                    artist_list.append(artistTemp)

            axTime.set_xscale(xscale)
            axTime.set_yscale(yscale)
            if (plot_type == 3):
                if plot_walltime:
                    axTime.set_xlabel(r"Speedup Ratio (Core Time)")
                else:
                    axTime.set_xlabel(r"Speedup Ratio")
                if (plot_var == "Average"):
                    axTime.set_ylabel(r'Average $\ell^2$ Error')
                else:
                    axTime.set_ylabel(r'Field $\ell^2$ Error')
                if ybounds is not None:
                    axTime.set_ylim(ybounds)
            else:
                axTime.set_xlabel(xlabel)
                if (plot_type == 2):
                    axTime.set_ylabel(r"Runtime Ratio (--)")
                    if ybounds is not None:
                        axTime.set_ylim(ybounds)
                else:
                    if plot_walltime:
                        axTime.set_ylabel(r"Speedup Ratio (Core Time)")
                    else:
                        axTime.set_ylabel(r"Speedup Ratio")
                    if ybounds is not None:
                        axTime.set_ylim(ybounds)

            if xbounds is not None:
                axTime.set_xlim(xbounds)
            if xticks is not None:
                axTime.xaxis.set_ticks(xticks)

            if plot_walltime:
                axTimeWall.set_xlabel("Speedup Ratio (Wall Time)")
                axTimeWall.set_xscale(xscale)
                axTimeWall.set_xlim(xbounds_wall)


        if ((plot_type == 0) or (plot_type == 2)):
            artist, = axErr.plot(xvals_list[lineIdx], plotErrVals,color=plot_colors[lineIdx], marker='o',linestyle=axErrStyle)
            if (plot_type == 0):
                artist_list.append(artist)
                axErr.set_xscale(xscale)
                axErr.set_xlabel(xlabel)
                if xticks is not None:
                    axErr.xaxis.set_ticks(xticks)
                if (plot_var == "Average"):
                    axErr.set_ylabel(r'Average $\ell^2$ Error')
                else:
                    axErr.set_ylabel(r'Field $\ell^2$ Error')
            else:
                if (plot_var == "Average"):
                    axErr.set_ylabel(r'Average $\ell^2$ Error ($\mathbf{-}$)')
                else:
                    axErr.set_ylabel(r'Field $\ell^2$ Error ($\mathbf{-}$)')
            axErr.set_yscale('log')
            if xbounds is not None:
                axErr.set_xlim(xbounds)
            if ybounds is not None:
                axErr.set_ylim(ybounds)

    if plot_legend:
        if (plot_type > 0):
            axTime.legend(artist_list, legend_labels, loc=legend_loc, framealpha=0.8, prop={'size':legend_fontsize})
        else:
            axErr.legend(artist_list, legend_labels, loc=legend_loc, framealpha=0.8, prop={'size':legend_fontsize})


    plt.tight_layout()
    print("Saving image to " + out_file)
    plt.savefig(out_file)


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
    plot_avg=False,
    xlog=False,
    xticks=None,
    xlabel="Number of Modes",
    ybounds=None,
    legend_labels=None,
    legend_loc="best",
    legend_font_size=12,
    num_legend_columns=1,
    out_file=None,
):

    if plot_avg:
        assert len(plot_styles) == (len(plot_vars) + 1)
        if legend_labels is not None:
            legend_labels.append("Average")

    assert(len(data_dirs) == len(x_vals))

    plot_vals = np.zeros((len(data_dirs), len(plot_vars)))

    fig = plt.figure()
    ax = fig.add_subplot(111)
    for file_iter, path in enumerate(data_dirs):

        file_name = file_header + "_" + str(iter_start_list[file_iter]) + "_" + str(iter_end_list[file_iter]) + "_" + str(iter_skip_list[file_iter]) + ".dat"
        data_path = os.path.join(base_dir, data_dirs[file_iter], file_name)

        print("Processing " + data_path)

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

    if plot_avg:
        avg = np.mean(plot_vals, axis=1)
        if xlog:
            ax.loglog(x_vals, avg, plot_styles[-1], marker="o")
        else:
            ax.semilogy(x_vals, avg, plot_styles[-1], marker="o")

    if xticks is not None:
        ax.xaxis.set_ticks(xticks)
    if ybounds is not None:
        ax.set_ylim(ybounds)

    ax.set_xlabel(xlabel)
    if ((len(plot_vars) == 1) and (plot_vars[0] == "Average")):
        ax.set_ylabel(r'Average $\ell^2$ Error')
    else:
        ax.set_ylabel(r'Field $\ell^2$ Error')

    if legend_labels is not None:
        ax.legend(legend_labels,loc=legend_loc, framealpha=0.8, prop={'size':legend_font_size}, ncol=num_legend_columns)

    plt.tight_layout()

    if out_file is None:
        out_file = "error"
        for var in plot_vars:
            out_file += "_" + var

    out_file += ".png"
    out_file = os.path.join(outdir, out_file)
    print("Image saved to " + out_file)
    plt.savefig(out_file, format='png')