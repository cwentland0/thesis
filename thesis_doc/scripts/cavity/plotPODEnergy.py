import sys

sys.path.append("/home/chris/Research/Papers/thesis/thesis_doc/scripts")
from plotPODResEnergy import plotPODResEnergy

base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cavity/PODBases"
pod_dirs = [
    "consvBases/centIC_normL2_nonVelMag/100ms_to_110ms_samp1/",
    "primBases/centIC_normL2_nonVelMag/100ms_to_110ms_samp1/",
]
plot_colors = ["b", "r"]
ubound = 200
outdir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cavity"
outfile = "cavity_pod_energy_10ms"
ybounds = [0.01, 100]
zoom_loc = [0.225, 0.45, 0.47, 0.47]
zoom_bounds_x = [0, 25]
zoom_bounds_y = [1, 100]
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