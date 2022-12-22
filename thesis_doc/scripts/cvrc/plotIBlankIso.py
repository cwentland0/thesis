import os
import sys
sys.path.append("/p/work/chriswen/thesis/thesis_doc/scripts")
from plotLayout import plotLayout

layout = "/p/work/chriswen/thesis/thesis_doc/scripts/cvrc/iBlank.lay"
fileline = 2
samp_perc = 0.0025
modes = 300
parts = 7

basedir = "/p/work/chriswen/CVRC_cutoff/unforced_dt1e-7/PODBases/deimBases/solutionModes/conservative"
indir = "pinv_modes" + str(modes) + "_samp" + str(samp_perc) + "/mesh_" + str(parts)
outdir = "/p/work/chriswen/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cvrc/deim/iblank"

# Random
filename = os.path.join(basedir, "random", indir, "dfd_cell.plt")
outname = os.path.join(outdir, "random_iblank_iso.png")
plotLayout(filename, layout, fileline, outname)

# Eigenvec
filename = os.path.join(basedir, "eigenvec", indir, "dfd_cell.plt")
outname = os.path.join(outdir, "eigenvec_iblank_iso.png")
plotLayout(filename, layout, fileline, outname)

# GNAT V1
filename = os.path.join(basedir, "greedy_carlberg", indir, "dfd_cell.plt")
outname = os.path.join(outdir, "greedy_carlberg_iblank_iso.png")
plotLayout(filename, layout, fileline, outname)

# GNAT V2
filename = os.path.join(basedir, "greedy_ben", indir, "dfd_cell.plt")
outname = os.path.join(outdir, "greedy_ben_iblank_iso.png")
plotLayout(filename, layout, fileline, outname)
