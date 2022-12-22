import sys
sys.path.append("/p/work/chriswen/thesis/thesis_doc/scripts")

from plotSlices import plotContourOrSlices

output_dir = "/p/work/chriswen/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cavity/deim"

fig_width=1024
var_name = "iBlank"
colormap = "Magma"
colormap_bounds = [0, 3]
num_colormap_levels = 4
frame_height = 7
frame_width = 9
zoom_lims = [[-70, 160], [-50, 55]]
iblank_val = 3

# Random
data_dir = "/p/work/chriswen/2d_cavity/PODBases/deimBases/solutionModes/conservative/random/pinv_modes250_samp0.025/mesh_3"
file_header = "iBlank_random"

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
    file_header=file_header,
    fig_width=fig_width,
    zoom=True,
    zoom_lims=zoom_lims,
    iblank_val=iblank_val,
)

# Eigenvector
data_dir = "/p/work/chriswen/2d_cavity/PODBases/deimBases/solutionModes/conservative/eigenvec/pinv_modes250_samp0.025/mesh_3"
file_header = "iBlank_eigenvec"

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
    file_header=file_header,
    fig_width=fig_width,
    zoom=True,
    zoom_lims=zoom_lims,
    iblank_val=iblank_val,
)

# Eigenvector
data_dir = "/p/work/chriswen/2d_cavity/PODBases/deimBases/solutionModes/conservative/greedy_carlberg/pinv_modes250_samp0.025/mesh_3"
file_header = "iBlank_greedy_carlberg"

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
    file_header=file_header,
    fig_width=fig_width,
    zoom=True,
    zoom_lims=zoom_lims,
    iblank_val=iblank_val,
)

# Eigenvector
data_dir = "/p/work/chriswen/2d_cavity/PODBases/deimBases/solutionModes/conservative/greedy_ben/pinv_modes250_samp0.025/mesh_3"
file_header = "iBlank_greedy_ben"

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
    file_header=file_header,
    fig_width=fig_width,
    zoom=True,
    zoom_lims=zoom_lims,
    iblank_val=iblank_val,
)

print("Finished")
