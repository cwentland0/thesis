import os

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

mpl.rc('font', family='serif', size='14')
mpl.rc('axes', labelsize='x-large')
mpl.rc('figure', facecolor='w')
mpl.rc('text', usetex=True)
mpl.rc('text.latex',preamble=r'\usepackage{amsmath}')


def plotProbes(
    base_dir,
    data_dirs,
    start_chunk,
    end_chunk,
    point_mon,
    var_name,
    var_list,
    plot_colors,
    outdir,
    press_factor=1.0,
    time_fac=1.0,
    xbounds=None,
    xticks=None,
    ybounds=None,
    yticks=None,
    legend_labels=[],
    plot_train_bound=False,
    train_bound=None,
    plot_legend=False,
    legendloc="best",
    outfile=None,
):

    assert end_chunk >= start_chunk

    var_idx = var_list.index(var_name) + 1
    file_suff = ''
    for var in var_list:
        file_suff = file_suff + "_" + var

    # press_factorSq = np.square(press_factor)
    if press_factor == 1.0:
        press_scale = "Pa"
    elif press_factor == 1e3:
        press_scale = "kPa"
    elif press_factor == 1e6:
        press_scale = "MPa"
    else:
        raise ValueError("Invalid press_factor: " + str(press_factor))

    if xbounds is not None:
        xbounds = [xbounds[i]*time_fac for i in range(2)]
    if xticks is not None:
        xticks[:] *= time_fac

    maxT = -1.0
    minT = np.inf

    fig = plt.figure()
    ax = fig.add_subplot(111)
    for sim_count, data_dir in enumerate(data_dirs):

        print("Plotting data from " + data_dir)

        data_path = os.path.join(base_dir, data_dir)
        for chunk_idx, chunk in enumerate(range(start_chunk, end_chunk + 1)):

            file_name = os.path.join(data_path, "point_mon_" + str(point_mon) + file_suff + "." + str(chunk) + ".npy")
            try:
                data_in = np.load(file_name)
            except OSError:
                print("Simulation apparently failed...")
                if chunk_idx == 0:
                    raise ValueError("Dataset missing from " + file_name)
                else:
                    break

            if chunk_idx == 0:
                data_arr = data_in.copy()
            else:
                data_arr = np.concatenate((data_arr, data_in), axis=0)

        if var_name == 'Static_Pressure':
            data_arr[:, var_idx] = data_arr[:, var_idx] / press_factor

        data_arr[:, 0] = data_arr[:, 0] * time_fac

        ax.plot(data_arr[:, 0], data_arr[:, var_idx], plot_colors[sim_count])
        if (np.amin(data_arr[:, 0]) < minT): minT = np.amin(data_arr[:, 0])
        if (np.amax(data_arr[:, 0]) > maxT): maxT = np.amax(data_arr[:, 0])

    if (time_fac == 1.0):
        time_units = "s"
    elif (time_fac == 1.0e3):
        time_units = "ms"
    elif (time_fac == 1.0e6):
        time_units = "$\mu$s"
    elif (time_fac == 1.0e9):
        time_units = "ns"
    else:
        raise ValueError("Invalid time_fac: "+str(time_fac))

    ax.set_xlabel(r't (' +time_units + ')')
    if var_name == "Static_Pressure":
        ax.set_ylabel('Pressure (' +press_scale +')')
    if var_name == "Temperature":
        ax.set_ylabel('Temperature (K)')
    if var_name == "U":
        ax.set_ylabel('Axial Velocity (m/s)')


    ax.set_xlim([minT, maxT])
    plt.minorticks_on()

    if plot_train_bound:
            assert train_bound is not None
            bottom, top = ax.get_ylim()
            ax.plot([train_bound[0], train_bound[1]],[bottom, top], 'k--')
            legend_labels.append('Training end')

    ax.xaxis.set_major_formatter(FormatStrFormatter('%g'))
    if xticks is not None:
        ax.xaxis.set_ticks(xticks)
        plt.subplots_adjust(right=0.95)

    if yticks is not None:
        ax.yaxis.set_ticks(yticks)

    if ybounds is not None:
        ax.set_ylim([ybounds[0], ybounds[1]])
    if xbounds is not None:
        ax.set_xlim([xbounds[0], xbounds[1]])

    if plot_legend:
        ax.legend(legend_labels, loc=legendloc, framealpha=1)

    plt.tight_layout()
    if outfile is None:
        outfile = 'point_' + str(point_mon) + '_' + var_name
    image_file = os.path.join(outdir, outfile + '.png')
    plt.savefig(image_file, format='png')
    print("File output to " + image_file)