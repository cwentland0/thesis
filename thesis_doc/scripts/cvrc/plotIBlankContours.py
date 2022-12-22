import os
import sys
sys.path.append("/p/work/chriswen/thesis/thesis_doc/scripts")

from plotSlices import plotContourOrSlices

output_dir = "/p/work/chriswen/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cvrc/deim/iblank"

samp_perc = 0.005
modes = 300
parts = 13

var_name = "iBlank"
colormap = "Magma"
colormap_bounds = [0, 3]
num_colormap_levels = 4

fig_width=1024
line_coords = [[0.02,-0.025], [0.02,0.025]]

iblank_val = 3

basedir = "/p/work/chriswen/CVRC_cutoff/unforced_dt1e-7/PODBases/deimBases/solutionModes/conservative"
indir = "pinv_modes" + str(modes) + "_samp" + str(samp_perc) + "/mesh_" + str(parts)

# Random
data_dir = os.path.join(basedir, "random", indir) 

# z-slice
slice_axis = "z"
slice_origin = 0.0
frame_width = 13
frame_height = 2.75

file_header = "random_iblank_z"

plotContourOrSlices(
    data_dir,
    1,
    1,
    999,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height,
    frame_width,
    output_dir,
    slice_axis=slice_axis,
    slice_origin=slice_origin,
    file_header=file_header,
    fig_width=fig_width,
    add_line=True,
    line_coords=line_coords,
    iblank_val=iblank_val,
)

# x-slice
slice_axis = "x"
slice_origin = 0.02
frame_width = 2.75
frame_height = 2.75

file_header = "random_iblank_x"

plotContourOrSlices(
    data_dir,
    1,
    1,
    999,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height,
    frame_width,
    output_dir,
    slice_axis=slice_axis,
    slice_origin=slice_origin,
    file_header=file_header,
    fig_width=fig_width,
    iblank_val=iblank_val,
)

# Eigenvector
data_dir = os.path.join(basedir, "eigenvec", indir) 

# z-slice
slice_axis = "z"
slice_origin = 0.0
frame_width = 13
frame_height = 2.75

file_header = "eigenvec_iblank_z"

plotContourOrSlices(
    data_dir,
    1,
    1,
    999,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height,
    frame_width,
    output_dir,
    slice_axis=slice_axis,
    slice_origin=slice_origin,
    file_header=file_header,
    fig_width=fig_width,
    add_line=True,
    line_coords=line_coords,
    iblank_val=iblank_val,
)

# x-slice
slice_axis = "x"
slice_origin = 0.02
frame_width = 2.75
frame_height = 2.75

file_header = "eigenvec_iblank_x"

plotContourOrSlices(
    data_dir,
    1,
    1,
    999,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height,
    frame_width,
    output_dir,
    slice_axis=slice_axis,
    slice_origin=slice_origin,
    file_header=file_header,
    fig_width=fig_width,
    iblank_val=iblank_val,
)


# GNAT V1
data_dir = os.path.join(basedir, "greedy_carlberg", indir) 

# z-slice
slice_axis = "z"
slice_origin = 0.0
frame_width = 13
frame_height = 2.75

file_header = "greedy_carlberg_iblank_z"

plotContourOrSlices(
    data_dir,
    1,
    1,
    999,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height,
    frame_width,
    output_dir,
    slice_axis=slice_axis,
    slice_origin=slice_origin,
    file_header=file_header,
    fig_width=fig_width,
    add_line=True,
    line_coords=line_coords,
    iblank_val=iblank_val,
)

# x-slice
slice_axis = "x"
slice_origin = 0.02
frame_width = 2.75
frame_height = 2.75

file_header = "greedy_carlberg_iblank_x"

plotContourOrSlices(
    data_dir,
    1,
    1,
    999,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height,
    frame_width,
    output_dir,
    slice_axis=slice_axis,
    slice_origin=slice_origin,
    file_header=file_header,
    fig_width=fig_width,
    iblank_val=iblank_val,
)

# GNAT V2
data_dir = os.path.join(basedir, "greedy_ben", indir) 

# z-slice
slice_axis = "z"
slice_origin = 0.0
frame_width = 13
frame_height = 2.75

file_header = "greedy_ben_iblank_z"

plotContourOrSlices(
    data_dir,
    1,
    1,
    999,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height,
    frame_width,
    output_dir,
    slice_axis=slice_axis,
    slice_origin=slice_origin,
    file_header=file_header,
    fig_width=fig_width,
    add_line=True,
    line_coords=line_coords,
    iblank_val=iblank_val,
)

# x-slice
slice_axis = "x"
slice_origin = 0.02
frame_width = 2.75
frame_height = 2.75

file_header = "greedy_ben_iblank_x"

plotContourOrSlices(
    data_dir,
    1,
    1,
    999,
    var_name,
    colormap,
    colormap_bounds,
    num_colormap_levels,
    frame_height,
    frame_width,
    output_dir,
    slice_axis=slice_axis,
    slice_origin=slice_origin,
    file_header=file_header,
    fig_width=fig_width,
    iblank_val=iblank_val,
)

