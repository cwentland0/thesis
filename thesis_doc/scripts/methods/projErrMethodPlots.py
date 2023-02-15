import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import matplotlib as mpl
mpl.rc("font", family="serif", size="12")
mpl.rc("axes", labelsize="x-large")
mpl.rc("figure", facecolor="w")
mpl.rc("text", usetex=False)
mpl.rc("text.latex", preamble=r"\usepackage{amsmath}")
import matplotlib.pyplot as plt

import numpy as np

from scipy.optimize import least_squares
from tensorflow.keras.models import load_model

# ----- BEGIN USER INPUTS -----

data_file = "/home/chris/Research/Papers/thesis/thesis_doc/data/1d_flame/proj_err_method/data/sol_prim_FOM.npy"
snap_start = 200
snap_end = 1000
snap_skip = 10
snap_num = 600

cae_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/1d_flame/proj_err_method/cae"

pod_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/1d_flame/proj_err_method/pod"

scale_dir = "/home/chris/Research/Papers/thesis/thesis_doc/data/1d_flame/proj_err_method/scaling"

x_L = 0.0
x_R = 0.01

t_start = 0.0
t_end = 0.4

outdir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/ProjROMs/Images"

# ----- END USER INPUTS -----

def calcResidual(x, snap, decoder):


    pred = np.squeeze(decoder(x[None, :]).numpy(), axis=0)
    res = snap.flatten() - pred.flatten()
    return res

def calcCAEProj(encoder, decoder, snap):

    snap = snap.T  # in NHWC format

    code0 = np.squeeze(encoder(snap[None, :, :]).numpy(), axis=0)
    # code0 = encoder(snap[None, :, :]).numpy()
    res_out = least_squares(calcResidual, code0, verbose=0, args=(snap, decoder))

    code_opt = res_out["x"]
    snap_proj = np.squeeze(decoder(code_opt[None, :]).numpy(), axis=0)

    return snap_proj

def calcPODProj(basis, snap):

    snap_shape = snap.shape
    snap_flat = snap.flatten(order="C")
    snap_proj = basis @ (basis.T @ snap_flat)
    snap_proj = np.reshape(snap_proj, snap_shape, order="C")

    return snap_proj

# load data
data = np.load(data_file)
data_snap = data[:, :, snap_num]
data = data[:, :, snap_start:snap_end]
num_vars, num_cells, num_snaps = data.shape

# load scaling
cent = np.load(os.path.join(scale_dir, "cent_prof_0_1_2_3.npy"))
sub = np.load(os.path.join(scale_dir, "norm_sub_prof_0_1_2_3.npy"))
fac = np.load(os.path.join(scale_dir, "norm_fac_prof_0_1_2_3.npy"))

# load CAEs and basis
decoder = load_model(os.path.join(cae_dir, "decoder_0_1_2_3.h5"), compile=False)
encoder = load_model(os.path.join(cae_dir, "encoder_0_1_2_3.h5"), compile=False)
latent_dim = decoder.layers[0].input_shape[0][-1]

basis = np.load(os.path.join(pod_dir, "spatial_modes_0_1_2_3.npy"))[:, :, :latent_dim]
basis = np.reshape(basis, (-1, latent_dim), order="C")

# compute single snapshot projections
data_snap_scale = (data_snap - cent - sub) / fac
data_snap_proj_pod = calcPODProj(basis, data_snap_scale) * fac + sub + cent
data_snap_proj_cae = calcCAEProj(encoder, decoder, data_snap_scale).T * fac + sub + cent

# spatial coordinates
x = np.linspace(x_L, x_R, num_cells)

# plot single snapshots
fig_temp_proj, ax_temp_proj = plt.subplots(nrows=1, ncols=1)
ax_temp_proj.plot(x, data_snap[2, :], 'k')
ax_temp_proj.plot(x, data_snap_proj_pod[2, :], 'b--')
ax_temp_proj.plot(x, data_snap_proj_cae[2, :], 'r--')
ax_temp_proj.legend(["FOM", "POD", "CAE"], loc="upper left", fontsize=14)
ax_temp_proj.set_ylabel("Temperature (K)")
ax_temp_proj.set_xlabel("x (m)")
plt.tight_layout()
plt.savefig(os.path.join(outdir, "temp_proj_field.png"))

fig_mf_proj, ax_mf_proj = plt.subplots(nrows=1, ncols=1)
ax_mf_proj.plot(x, data_snap[3, :], 'k')
ax_mf_proj.plot(x, data_snap_proj_pod[3, :], 'b--')
ax_mf_proj.plot(x, data_snap_proj_cae[3, :], 'r--')
# ax_mf_proj.legend(["FOM", "POD", "CAE"], loc="upper left", fontsize=14)
ax_mf_proj.set_ylabel("Reactant Mass Frac.")
ax_mf_proj.set_xlabel("x (m)")
plt.tight_layout()
plt.savefig(os.path.join(outdir, "mf_proj_field.png"))

# loop snapshots, compute error
t_range = range(0, num_snaps, snap_skip)
num_snaps_out = len(t_range)
temp_err = np.zeros((2, num_snaps_out), dtype=np.float64)
mf_err = np.zeros((2, num_snaps_out), dtype=np.float64)
for snap_idx, snap_num in enumerate(range(0, num_snaps, snap_skip)):

    print("Processing snapshot " + str(snap_idx + 1) + "/" + str(num_snaps_out))

    data_snap = data[:, :, snap_num]
    data_snap_scale = (data_snap - cent - sub) / fac
    data_snap_proj_pod = calcPODProj(basis, data_snap_scale) * fac + sub + cent
    data_snap_proj_cae = calcCAEProj(encoder, decoder, data_snap_scale).T * fac + sub + cent

    err_pod = np.linalg.norm(data_snap - data_snap_proj_pod, axis=1, ord=2) / np.linalg.norm(data_snap, axis=1, ord=2)
    err_cae = np.linalg.norm(data_snap - data_snap_proj_cae, axis=1, ord=2) / np.linalg.norm(data_snap, axis=1, ord=2)

    temp_err[0, snap_idx] = err_pod[2]
    mf_err[0, snap_idx] = err_pod[3]
    temp_err[1, snap_idx] = err_cae[2]
    mf_err[1, snap_idx] = err_cae[3]

# time axis
t = np.linspace(t_start, t_end, num_snaps_out)

# plot temperature error
fig_temp_err, ax_temp_err = plt.subplots(nrows=1, ncols=1)
ax_temp_err.semilogy(t, temp_err[0,:], "b")
ax_temp_err.semilogy(t, temp_err[1,:], "r")
ax_temp_err.set_ylabel(r"Temperature $\ell^2$ Error")
ax_temp_err.set_xlabel("t (ms)")
ax_temp_err.set_ylim([1e-4, 3.0])
ax_temp_err.legend(["POD", "CAE"], loc="upper left", fontsize=14)
plt.tight_layout()
plt.savefig(os.path.join(outdir, "temp_error.png"))

# plot temperature error
fig_mf_err, ax_mf_err = plt.subplots(nrows=1, ncols=1)
ax_mf_err.semilogy(t, mf_err[0,:], "b")
ax_mf_err.semilogy(t, mf_err[1,:], "r")
ax_mf_err.set_ylabel(r"Reactant Mass Frac. $\ell^2$ Error")
ax_mf_err.set_xlabel("t (ms)")
ax_mf_err.set_ylim([1e-4, 10.0])
plt.tight_layout()
plt.savefig(os.path.join(outdir, "mf_error.png"))

# breakpoint()
print("Finished")
