#!/usr/bin/python
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import Axes3D
from scipy.interpolate import griddata

# ================= Font Settings =================
mpl.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 13,
    "axes.labelcolor": "black",
    "xtick.color": "black",
    "ytick.color": "black",
})

# ================= Load Data =================
try:
    kx_mesh = np.loadtxt("KX.grd")
    ky_mesh = np.loadtxt("KY.grd")
    CBM_mesh = np.loadtxt("BAND_LUMO.grd")
    VBM_mesh = np.loadtxt("BAND_HOMO.grd")
except Exception as e:
    print("Failed to open grds!", e)
    exit(1)

# ================= Interpolation (SMOOTHING) =================
# finer grid
kx_fine = np.linspace(kx_mesh.min(), kx_mesh.max(), 200)
ky_fine = np.linspace(ky_mesh.min(), ky_mesh.max(), 200)
kx_fine, ky_fine = np.meshgrid(kx_fine, ky_fine)

# interpolate bands
VBM_smooth = griddata(
    (kx_mesh.flatten(), ky_mesh.flatten()),
    VBM_mesh.flatten(),
    (kx_fine, ky_fine),
    method='cubic'
)

CBM_smooth = griddata(
    (kx_mesh.flatten(), ky_mesh.flatten()),
    CBM_mesh.flatten(),
    (kx_fine, ky_fine),
    method='cubic'
)

# replace with smooth data
kx_mesh, ky_mesh = kx_fine, ky_fine
VBM_mesh, CBM_mesh = VBM_smooth, CBM_smooth

# ================= Helper Function =================
def format_ticks(ax, dx=0.5, dy=0.5, tick_fontsize=9):
    ax.xaxis.set_major_locator(MultipleLocator(dx))
    ax.yaxis.set_major_locator(MultipleLocator(dy))
    ax.xaxis.set_major_formatter(FormatStrFormatter("%.1f"))
    ax.yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
    ax.tick_params(axis="x", labelsize=tick_fontsize)
    ax.tick_params(axis="y", labelsize=tick_fontsize)
    ax.zaxis.set_tick_params(labelsize=11)

# ================= Plot =================
fig = plt.figure(figsize=(12, 12))

# smoother colormap
#cmap = plt.colormaps["viridis"]
#cmap = plt.colormaps["plasma"]
cmap = plt.colormaps["turbo"]
#cmap = plt.colormaps["inferno"]
#cmap = plt.colormaps["magma"]
#cmap = plt.colormaps["cividis"]
#cmap = plt.colormaps["coolwarm"]



axes = []
z0 = 0

# lines domain
kx_line = np.linspace(kx_mesh.min(), kx_mesh.max(), 300)
ky_line = np.linspace(ky_mesh.min(), ky_mesh.max(), 300)

# --- First subplot ---
ax0 = fig.add_subplot(131, projection="3d")
axes.append(ax0)

ax0.plot_surface(kx_mesh, ky_mesh, VBM_mesh,
                 cmap=cmap, linewidth=0,
                 antialiased=True, shade=True)

ax0.plot_surface(kx_mesh, ky_mesh, CBM_mesh,
                 cmap=cmap, linewidth=0,
                 antialiased=True, shade=True)

# zero-energy dotted lines
ax0.plot(kx_line, np.zeros_like(kx_line), np.full_like(kx_line, z0),
         linestyle=":", linewidth=1)

ax0.plot(np.zeros_like(ky_line), ky_line, np.full_like(ky_line, z0),
         linestyle=":", linewidth=1)

ax0.set_ylabel(r"$\mathbf{k}_{y}$")
ax0.set_zlabel(r"Energy (eV)")
ax0.set_zlim((-2, 2))
ax0.set_xticks([])
ax0.view_init(elev=0, azim=0)
format_ticks(ax0)

# --- Second subplot ---
ax = fig.add_subplot(132, projection="3d")
axes.append(ax)

ax.plot_surface(kx_mesh, ky_mesh, VBM_mesh,
                cmap=cmap, linewidth=0,
                antialiased=True, shade=True)

ax.plot_surface(kx_mesh, ky_mesh, CBM_mesh,
                cmap=cmap, linewidth=0,
                antialiased=True, shade=True)

ax.plot(kx_line, np.zeros_like(kx_line), np.full_like(kx_line, z0),
        linestyle=":", linewidth=1)

ax.plot(np.zeros_like(ky_line), ky_line, np.full_like(ky_line, z0),
        linestyle=":", linewidth=1)

ax.set_xlabel(r"$\mathbf{k}_{x}$")
ax.set_ylabel(r"$\mathbf{k}_{y}$")
ax.set_zlabel(r"Energy (eV)")
ax.set_zlim((-2, 2))
ax.view_init(elev=0, azim=45)
format_ticks(ax)

# --- Third subplot ---
ax1 = fig.add_subplot(133, projection="3d")
axes.append(ax1)

ax1.plot_surface(kx_mesh, ky_mesh, VBM_mesh,
                 cmap=cmap, linewidth=0,
                 antialiased=True, shade=True)

ax1.plot_surface(kx_mesh, ky_mesh, CBM_mesh,
                 cmap=cmap, linewidth=0,
                 antialiased=True, shade=True)

ax1.plot(kx_line, np.zeros_like(kx_line), np.full_like(kx_line, z0),
         linestyle=":", linewidth=1)

ax1.plot(np.zeros_like(ky_line), ky_line, np.full_like(ky_line, z0),
         linestyle=":", linewidth=1)

ax1.set_xlabel(r"$\mathbf{k}_{x}$")
ax1.set_ylabel(r"$\mathbf{k}_{y}$")
ax1.set_zlabel(r"Energy (eV)")
ax1.set_zlim((-2, 2))
ax1.view_init(elev=5, azim=45)
format_ticks(ax1)

# ================= Clean Look =================
for a in axes:
    a.grid(False)
    a.xaxis.pane.fill = False
    a.yaxis.pane.fill = False
    a.zaxis.pane.fill = False

# ================= Save =================
plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                    hspace=0.1, wspace=0.1)

plt.savefig("new-3D-smooth.png", dpi=600, bbox_inches="tight")

print("Saved figure as new-3D-smooth.png")
