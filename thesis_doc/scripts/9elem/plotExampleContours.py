import sys
sys.path.append("/home/chris/Research/Papers/thesis/thesis_doc/scripts")

from plotSlices import plotContourOrSlices

data_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/9elem/FOM/SZLFiles"
iter_start = 215000
iter_end = 219000
iter_skip = 1000
output_dir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/NineElement/Images/example_snaps"
meshfile = "/home/chris/Research/Papers/thesis/thesis_doc/data/9elem/FOM/SZLFiles/gemsma_grid.szplt"

fig_width=1024
theta = -90.0

slice_axis = "z"
slice_origin = 1e-6
frame_width = 10
frame_height = 8
legend_position = (0, 95)

##### Pressure slices #####
var_name = "Static_Pressure"
var_name_legend = "Pressure (MPa)"
colormap = "cmocean - balance"
colormap_bounds = [0.1, 2.5]
num_colormap_levels = 97
legend_spacing = 2
legend_level_skip = 16
file_header = "example_pressure_z"
scale_val = 1e-6


plotContourOrSlices(
    data_dir,
    iter_start,
    iter_start,
    iter_skip,
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
    theta=theta,
    vertical_legend=True,
)

plotContourOrSlices(
    data_dir,
    iter_start + iter_skip,
    iter_end,
    iter_skip,
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
    show_legend=False,
    legend_spacing=legend_spacing,
    legend_level_skip=legend_level_skip,
    legend_position=legend_position,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
    theta=theta,
)

##### Heat release slices #####
var_name = "Heat_Release"
var_name_legend = "Heat Release\\n(GW/m<sup>3</sup>)"
colormap = "Hot Metal"
colormap_bounds = [0.0, 100]
num_colormap_levels = 101
legend_spacing = 2
legend_level_skip = 20
file_header = "example_heat_z"
scale_val = 1e-9

plotContourOrSlices(
    data_dir,
    iter_start,
    iter_start,
    iter_skip,
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
    theta=theta,
    vertical_legend=True,
)

plotContourOrSlices(
    data_dir,
    iter_start + iter_skip,
    iter_end,
    iter_skip,
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
    show_legend=False,
    legend_spacing=legend_spacing,
    legend_level_skip=legend_level_skip,
    legend_position=legend_position,
    var_name_legend=var_name_legend,
    scale_val=scale_val,
    theta=theta,
)

print("Finished")
