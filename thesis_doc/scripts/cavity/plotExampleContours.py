import os
import sys
sys.path.append("/home/chris/Research/Papers/Thesis_CW/thesis/thesis_doc/scripts")

from plotSlices import plotContourOrSlices

data_dir = "/home/chris/Research/GEMS_runs/2d_cavity/FOM/SZLFiles"
snap_iter = 104000
output_dir = "/home/chris/Research/Papers/Thesis_CW/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cavity"

fig_width=1024

# Pressure full
var_name = "Static_Pressure"
var_name_legend = "Pressure (Pa)"
colormap = "cmocean - balance"
colormap_bounds = [21.0, 29.0]
num_colormap_levels = 121
frame_height = 5.25
frame_width = 10.5
legend_spacing = 2.5
legend_level_skip = 30
file_header = "pressure_example_full"

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
    file_header=file_header,
    fig_width=fig_width,
    show_legend=True,
    legend_spacing=legend_spacing,
    legend_level_skip=legend_level_skip,
    legend_position=(0, 15),
    var_name_legend=var_name_legend,
)

# Pressure zoom
zoom_lims = [[-0.07, 0.16], [-0.05, 0.055]]
legend_spacing = 3
legend_level_skip = 60
file_header = "pressure_example"

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
    file_header=file_header,
    fig_width=fig_width,
    zoom=True,
    zoom_lims=zoom_lims,
    show_legend=True,
    vertical_legend=True,
    legend_spacing=legend_spacing,
    legend_level_skip=legend_level_skip,
    legend_position=(10, 43),
    var_name_legend=var_name_legend,
)

# V zoom
var_name = "V"
var_name_legend = "V (m/s)"
colormap = "cmocean - balance"
colormap_bounds = [-125, 125]
num_colormap_levels = 101
legend_spacing = 1.2
legend_level_skip = 10
file_header = "y_vel_example"

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
    file_header=file_header,
    fig_width=fig_width,
    zoom=True,
    zoom_lims=zoom_lims,
)

print("Finished")