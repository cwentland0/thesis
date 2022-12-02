import sys

sys.path.append("/home/chris/Research/Papers/thesis/thesis_doc/scripts")
from plotProbes import plotProbes

base_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/cavity/FOM/"
data_dirs = [
    "PointResults",
]
start_chunk = 101
end_chunk = 110
point_mon = 8
var_name = "Static_Pressure"
var_list = ["Static_Pressure"]
plot_colors = ["k"]
outdir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cavity"
outfile = "pressure_probe_fom_10ms"
time_fac = 1000.0
xbounds = [0.1, 0.11]

plotProbes(
    base_dir,
    data_dirs,
    start_chunk,
    end_chunk,
    point_mon,
    var_name,
    var_list,
    plot_colors,
    outdir,
    time_fac=time_fac,
    outfile=outfile,
    xbounds=xbounds,
)