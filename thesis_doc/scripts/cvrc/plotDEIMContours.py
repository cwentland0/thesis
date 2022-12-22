import os
import sys
sys.path.append("/p/work/chriswen/thesis/thesis_doc/scripts")

from plotSlices import plotContourOrSlices

#data_dir_base = "/p/work/chriswen/CVRC_cutoff/unforced_dt1e-7/ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt1e-6/mplsvt-real/implicit/k100/solutionModes/conservative"
#snap_iter = 5500

data_dir_base = "/p/work/chriswen/CVRC_cutoff/unforced_dt1e-7/ROMs/primitive/centIC_normL2_nonVelMag/5p0ms_to_5p5ms_dt5e-7/mplsvt-real/implicit/k100/solutionModes/conservative"
snap_iter = 11000

output_base = "/p/work/chriswen/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cvrc/deim/contours"

fig_width=1024
line_coords = [[0.02,-0.025], [0.02,0.025]]

modes = 300
samprate = 0.0025
parts = 7

slice_axis_z = "z"
slice_origin_z = 0.0
frame_width_z = 13
frame_height_z = 2.75

slice_axis_x = "x"
slice_origin_x = 0.02
frame_width_x = 2.75
frame_height_x = 2.75

###### Pressure slices #####
var_name = "Static_Pressure"
var_name_legend = "Pressure (MPa)"
colormap = "cmocean - balance"
colormap_bounds = [1.2, 1.35]
num_colormap_levels = 91
legend_spacing = 1.75
legend_level_skip = 18
scale_val = 1e-6
legend_position = (1.25, 100)

#---- Random----

data_dir = os.path.join(data_dir_base, "random", "parts" + str(parts), "modes" + str(modes) + "_samp"+ str(samprate), "UnsteadyFieldResults")
output_dir = os.path.join(output_base, "random")

file_header = "random_pressure_z"
plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height_z,
    frame_width_z,
    output_dir,
    slice_axis=slice_axis_z,
    slice_origin=slice_origin_z,
    file_header=file_header,
    fig_width=fig_width,
    show_legend=False,
    legend_spacing=legend_spacing,
    legend_level_skip=legend_level_skip,
    legend_position=legend_position,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
    add_line=True,
    line_coords=line_coords,
)

file_header = "random_pressure_x"
plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height_x,
    frame_width_x,
    output_dir,
    slice_axis=slice_axis_x,
    slice_origin=slice_origin_x,
    file_header=file_header,
    fig_width=fig_width,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
)

#----Eigenvec----

data_dir = os.path.join(data_dir_base, "eigenvec", "parts" + str(parts), "modes" + str(modes) + "_samp"+ str(samprate), "UnsteadyFieldResults")
output_dir = os.path.join(output_base, "eigenvec")

file_header = "eigenvec_pressure_z"
plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height_z,
    frame_width_z,
    output_dir,
    slice_axis=slice_axis_z,
    slice_origin=slice_origin_z,
    file_header=file_header,
    fig_width=fig_width,
    show_legend=False,
    legend_spacing=legend_spacing,
    legend_level_skip=legend_level_skip,
    legend_position=legend_position,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
    add_line=True,
    line_coords=line_coords,
)

file_header = "eigenvec_pressure_x"
plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height_x,
    frame_width_x,
    output_dir,
    slice_axis=slice_axis_x,
    slice_origin=slice_origin_x,
    file_header=file_header,
    fig_width=fig_width,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
)

#----Greedy Carlberg----

data_dir = os.path.join(data_dir_base, "greedy_carlberg", "parts" + str(parts), "modes" + str(modes) + "_samp"+ str(samprate), "UnsteadyFieldResults")
output_dir = os.path.join(output_base, "greedy_carlberg")

file_header = "greedy_carlberg_pressure_z"
plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height_z,
    frame_width_z,
    output_dir,
    slice_axis=slice_axis_z,
    slice_origin=slice_origin_z,
    file_header=file_header,
    fig_width=fig_width,
    show_legend=False,
    legend_spacing=legend_spacing,
    legend_level_skip=legend_level_skip,
    legend_position=legend_position,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
    add_line=True,
    line_coords=line_coords,
)

file_header = "greedy_carlberg_pressure_x"
plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height_x,
    frame_width_x,
    output_dir,
    slice_axis=slice_axis_x,
    slice_origin=slice_origin_x,
    file_header=file_header,
    fig_width=fig_width,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
)

#----Greedy Ben----

data_dir = os.path.join(data_dir_base, "greedy_ben", "parts" + str(parts), "modes" + str(modes) + "_samp"+ str(samprate), "UnsteadyFieldResults")
output_dir = os.path.join(output_base, "greedy_ben")

file_header = "greedy_ben_pressure_z"
plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height_z,
    frame_width_z,
    output_dir,
    slice_axis=slice_axis_z,
    slice_origin=slice_origin_z,
    file_header=file_header,
    fig_width=fig_width,
    show_legend=False,
    legend_spacing=legend_spacing,
    legend_level_skip=legend_level_skip,
    legend_position=legend_position,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
    add_line=True,
    line_coords=line_coords,
)

file_header = "greedy_ben_pressure_x"
plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height_x,
    frame_width_x,
    output_dir,
    slice_axis=slice_axis_x,
    slice_origin=slice_origin_x,
    file_header=file_header,
    fig_width=fig_width,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
)

###### Temperature slices #####
var_name = "Temperature"
var_name_legend = "Temperature (K)"
colormap = "cmocean - balance"
colormap_bounds = [300, 2800]
num_colormap_levels = 101
legend_spacing = 1.505
legend_level_skip = 20
file_header = "example_temperature_z"
scale_val = 1.0
legend_position = (0, 100)

#---- Random----

data_dir = os.path.join(data_dir_base, "random", "parts" + str(parts), "modes" + str(modes) + "_samp"+ str(samprate), "UnsteadyFieldResults")
output_dir = os.path.join(output_base, "random")

file_header = "random_temperature_z"
plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height_z,
    frame_width_z,
    output_dir,
    slice_axis=slice_axis_z,
    slice_origin=slice_origin_z,
    file_header=file_header,
    fig_width=fig_width,
    show_legend=False,
    legend_spacing=legend_spacing,
    legend_level_skip=legend_level_skip,
    legend_position=legend_position,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
    add_line=True,
    line_coords=line_coords,
)

file_header = "random_temperature_x"
plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height_x,
    frame_width_x,
    output_dir,
    slice_axis=slice_axis_x,
    slice_origin=slice_origin_x,
    file_header=file_header,
    fig_width=fig_width,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
)

#----Eigenvec----

data_dir = os.path.join(data_dir_base, "eigenvec", "parts" + str(parts), "modes" + str(modes) + "_samp"+ str(samprate), "UnsteadyFieldResults")
output_dir = os.path.join(output_base, "eigenvec")

file_header = "eigenvec_temperature_z"
plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height_z,
    frame_width_z,
    output_dir,
    slice_axis=slice_axis_z,
    slice_origin=slice_origin_z,
    file_header=file_header,
    fig_width=fig_width,
    show_legend=False,
    legend_spacing=legend_spacing,
    legend_level_skip=legend_level_skip,
    legend_position=legend_position,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
    add_line=True,
    line_coords=line_coords,
)

file_header = "eigenvec_temperature_x"
plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height_x,
    frame_width_x,
    output_dir,
    slice_axis=slice_axis_x,
    slice_origin=slice_origin_x,
    file_header=file_header,
    fig_width=fig_width,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
)

#----Greedy Carlberg----

data_dir = os.path.join(data_dir_base, "greedy_carlberg", "parts" + str(parts), "modes" + str(modes) + "_samp"+ str(samprate), "UnsteadyFieldResults")
output_dir = os.path.join(output_base, "greedy_carlberg")

file_header = "greedy_carlberg_temperature_z"
plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height_z,
    frame_width_z,
    output_dir,
    slice_axis=slice_axis_z,
    slice_origin=slice_origin_z,
    file_header=file_header,
    fig_width=fig_width,
    show_legend=False,
    legend_spacing=legend_spacing,
    legend_level_skip=legend_level_skip,
    legend_position=legend_position,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
    add_line=True,
    line_coords=line_coords,
)

file_header = "greedy_carlberg_temperature_x"
plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height_x,
    frame_width_x,
    output_dir,
    slice_axis=slice_axis_x,
    slice_origin=slice_origin_x,
    file_header=file_header,
    fig_width=fig_width,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
)

#----Greedy Ben----

data_dir = os.path.join(data_dir_base, "greedy_ben", "parts" + str(parts), "modes" + str(modes) + "_samp"+ str(samprate), "UnsteadyFieldResults")
output_dir = os.path.join(output_base, "greedy_ben")

file_header = "greedy_ben_temperature_z"
plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height_z,
    frame_width_z,
    output_dir,
    slice_axis=slice_axis_z,
    slice_origin=slice_origin_z,
    file_header=file_header,
    fig_width=fig_width,
    show_legend=False,
    legend_spacing=legend_spacing,
    legend_level_skip=legend_level_skip,
    legend_position=legend_position,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
    add_line=True,
    line_coords=line_coords,
)

file_header = "greedy_ben_temperature_x"
plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height_x,
    frame_width_x,
    output_dir,
    slice_axis=slice_axis_x,
    slice_origin=slice_origin_x,
    file_header=file_header,
    fig_width=fig_width,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
)


###### Axial velocity slices #####
#var_name = "U"
#var_name_legend = "U (m/s)"
#colormap = "cmocean - balance"
#colormap_bounds = [-300, 300]
#num_colormap_levels = 91
#legend_spacing = 1.375
#legend_level_skip = 15
#file_header = "example_xVel_z"
#scale_val = 1.0
#legend_position = (7.75, 100)
#
## z-slice
#slice_axis = "z"
#slice_origin = 0.0
#frame_width = 13
#frame_height = 2.75
#
#plotContourOrSlices(
#    data_dir,
#    snap_iter,
#    snap_iter,
#    1,
#    var_name,
#    colormap,
#    colormap_bounds,
#    num_colormap_levels,
#    frame_height,
#    frame_width,
#    output_dir,
#    slice_axis=slice_axis,
#    slice_origin=slice_origin,
#    meshfile=meshfile,
#    file_header=file_header,
#    fig_width=fig_width,
#    show_legend=True,
#    legend_spacing=legend_spacing,
#    legend_level_skip=legend_level_skip,
#    legend_position=legend_position,
#    var_name_legend=var_name_legend,
#    scale_val=scale_val,
#    add_line=True,
#    line_coords=line_coords,
#)
#
## x-slice
#slice_axis = "x"
#slice_origin = 0.02
#frame_width = 2.75
#frame_height = 2.75
#file_header = "example_xVel_x"
#
#plotContourOrSlices(
#    data_dir,
#    snap_iter,
#    snap_iter,
#    1,
#    var_name,
#    colormap,
#    colormap_bounds,
#    num_colormap_levels,
#    frame_height,
#    frame_width,
#    output_dir,
#    slice_axis=slice_axis,
#    slice_origin=slice_origin,
#    meshfile=meshfile,
#    file_header=file_header,
#    fig_width=fig_width,
#    var_name_legend=var_name_legend,
#    scale_val=scale_val,
#)
#
###### Mixture fraction slices #####
#var_name = "Flamelet_Scalar_Mean"
#var_name_legend = "Z"
#colormap = "Sequential - Viridis"
#colormap_bounds = [0, 1]
#num_colormap_levels = 101
#legend_spacing = 2.4
#legend_level_skip = 20
#file_header = "example_mixFrac_z"
#scale_val = 1.0
#legend_position = (12.5, 100)
#
## z-slice
#slice_axis = "z"
#slice_origin = 0.0
#frame_width = 13
#frame_height = 2.75
#
#plotContourOrSlices(
#    data_dir,
#    snap_iter,
#    snap_iter,
#    1,
#    var_name,
#    colormap,
#    colormap_bounds,
#    num_colormap_levels,
#    frame_height,
#    frame_width,
#    output_dir,
#    slice_axis=slice_axis,
#    slice_origin=slice_origin,
#    meshfile=meshfile,
#    file_header=file_header,
#    fig_width=fig_width,
#    show_legend=True,
#    legend_spacing=legend_spacing,
#    legend_level_skip=legend_level_skip,
#    legend_position=legend_position,
#    var_name_legend=var_name_legend,
#    scale_val=scale_val,
#    add_line=True,
#    line_coords=line_coords,
#)
#
## x-slice
#slice_axis = "x"
#slice_origin = 0.02
#frame_width = 2.75
#frame_height = 2.75
#file_header = "example_mixFrac_x"
#
#plotContourOrSlices(
#    data_dir,
#    snap_iter,
#    snap_iter,
#    1,
#    var_name,
#    colormap,
#    colormap_bounds,
#    num_colormap_levels,
#    frame_height,
#    frame_width,
#    output_dir,
#    slice_axis=slice_axis,
#    slice_origin=slice_origin,
#    meshfile=meshfile,
#    file_header=file_header,
#    fig_width=fig_width,
#    var_name_legend=var_name_legend,
#    scale_val=scale_val,
#)

print("Finished")
