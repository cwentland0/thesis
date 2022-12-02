import sys

sys.path.append("/home/chris/Research/Papers/thesis/thesis_doc/scripts")
from plotPODResEnergy import plotPODResEnergy

base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cvrc/PODBases"
pod_dirs = [
    "consvBases/centIC_normL2_nonVelMag/5p0ms_to_6p0ms_samp10/",
    "primBases/centIC_normL2_nonVelMag/5p0ms_to_6p0ms_samp10/",
]
plot_colors = ["b", "r"]
ubound = 300
outdir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cvrc"
outfile = "cvrc_pod_energy_10ms"
ybounds = [0.01, 100]
zoom_loc = [0.27, 0.58, 0.4, 0.4]
zoom_bounds_x = [0, 25]
zoom_bounds_y = [10, 100]
legend_labels = [
    "Conservative",
    "Primitive",
]

plotPODResEnergy(
    base_dir,
    pod_dirs,
    plot_colors,
    ubound,
    outdir,
    outfile=outfile,
    ybounds=ybounds,
    zoom_loc=zoom_loc,
    zoom_bounds_x=zoom_bounds_x,
    zoom_bounds_y=zoom_bounds_y,
    legend_labels=legend_labels,
    legend_loc="upper right",
)