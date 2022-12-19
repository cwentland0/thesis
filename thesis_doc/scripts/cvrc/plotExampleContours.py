import sys
sys.path.append("/home/chris/Research/Papers/thesis/thesis_doc/scripts")

from plotSlices import plotContourOrSlices

data_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cvrc/FOM/SZLFiles"
snap_iter = 55000
output_dir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cvrc"
meshfile = "/home/chris/Research/Papers/thesis/thesis_doc/data/cvrc/FOM/SZLFiles/gemsma_grid.szplt"

fig_width=1024
line_coords = [[0.02,-0.025], [0.02,0.025]]

##### Pressure slices #####
var_name = "Static_Pressure"
var_name_legend = "Pressure (MPa)"
colormap = "cmocean - balance"
colormap_bounds = [1.2, 1.35]
num_colormap_levels = 91
legend_spacing = 1.75
legend_level_skip = 18
file_header = "example_pressure_z"
scale_val = 1e-6
legend_position = (1.25, 100)

# z-slice
slice_axis = "z"
slice_origin = 0.0
frame_width = 13
frame_height = 2.75

plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height,
    frame_width,
    output_dir,
    slice_axis=slice_axis,
    slice_origin=slice_origin,
    meshfile=meshfile,
    file_header=file_header,
    fig_width=fig_width,
    show_legend=True,
    legend_spacing=legend_spacing,
    legend_level_skip=legend_level_skip,
    legend_position=legend_position,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
    add_line=True,
    line_coords=line_coords,
)

# x-slice
slice_axis = "x"
slice_origin = 0.02
frame_width = 2.75
frame_height = 2.75
file_header = "example_pressure_x"

plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height,
    frame_width,
    output_dir,
    slice_axis=slice_axis,
    slice_origin=slice_origin,
    meshfile=meshfile,
    file_header=file_header,
    fig_width=fig_width,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
)

##### Temperature slices #####
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

# z-slice
slice_axis = "z"
slice_origin = 0.0
frame_width = 13
frame_height = 2.75

plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height,
    frame_width,
    output_dir,
    slice_axis=slice_axis,
    slice_origin=slice_origin,
    meshfile=meshfile,
    file_header=file_header,
    fig_width=fig_width,
    show_legend=True,
    legend_spacing=legend_spacing,
    legend_level_skip=legend_level_skip,
    legend_position=legend_position,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
    add_line=True,
    line_coords=line_coords,
)

# x-slice
slice_axis = "x"
slice_origin = 0.02
frame_width = 2.75
frame_height = 2.75
file_header = "example_temperature_x"

plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height,
    frame_width,
    output_dir,
    slice_axis=slice_axis,
    slice_origin=slice_origin,
    meshfile=meshfile,
    file_header=file_header,
    fig_width=fig_width,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
)

##### Axial velocity slices #####
var_name = "U"
var_name_legend = "U (m/s)"
colormap = "cmocean - balance"
colormap_bounds = [-300, 300]
num_colormap_levels = 91
legend_spacing = 1.375
legend_level_skip = 15
file_header = "example_xVel_z"
scale_val = 1.0
legend_position = (7.75, 100)

# z-slice
slice_axis = "z"
slice_origin = 0.0
frame_width = 13
frame_height = 2.75

plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height,
    frame_width,
    output_dir,
    slice_axis=slice_axis,
    slice_origin=slice_origin,
    meshfile=meshfile,
    file_header=file_header,
    fig_width=fig_width,
    show_legend=True,
    legend_spacing=legend_spacing,
    legend_level_skip=legend_level_skip,
    legend_position=legend_position,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
    add_line=True,
    line_coords=line_coords,
)

# x-slice
slice_axis = "x"
slice_origin = 0.02
frame_width = 2.75
frame_height = 2.75
file_header = "example_xVel_x"

plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height,
    frame_width,
    output_dir,
    slice_axis=slice_axis,
    slice_origin=slice_origin,
    meshfile=meshfile,
    file_header=file_header,
    fig_width=fig_width,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
)

##### Mixture fraction slices #####
var_name = "Flamelet_Scalar_Mean"
var_name_legend = "Z"
colormap = "Sequential - Viridis"
colormap_bounds = [0, 1]
num_colormap_levels = 101
legend_spacing = 2.4
legend_level_skip = 20
file_header = "example_mixFrac_z"
scale_val = 1.0
legend_position = (12.5, 100)

# z-slice
slice_axis = "z"
slice_origin = 0.0
frame_width = 13
frame_height = 2.75

plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height,
    frame_width,
    output_dir,
    slice_axis=slice_axis,
    slice_origin=slice_origin,
    meshfile=meshfile,
    file_header=file_header,
    fig_width=fig_width,
    show_legend=True,
    legend_spacing=legend_spacing,
    legend_level_skip=legend_level_skip,
    legend_position=legend_position,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
    add_line=True,
    line_coords=line_coords,
)

# x-slice
slice_axis = "x"
slice_origin = 0.02
frame_width = 2.75
frame_height = 2.75
file_header = "example_mixFrac_x"

plotContourOrSlices(
    data_dir,
    snap_iter,
    snap_iter,
    1,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height,
    frame_width,
    output_dir,
    slice_axis=slice_axis,
    slice_origin=slice_origin,
    meshfile=meshfile,
    file_header=file_header,
    fig_width=fig_width,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
)

print("Finished")
