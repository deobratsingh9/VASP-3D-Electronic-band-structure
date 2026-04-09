#!/usr/bin/python
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib as mpl
mpl.use('Agg')  # silent mode (no display)
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import Axes3D

# ================= Font Settings =================
mpl.rcParams.update({
    "font.family": "DejaVu Sans",  # safe default on HPC
    "font.size": 13,               # main font size (labels, titles)
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

# ================= Helper Function =================
def format_ticks(ax, dx=0.5, dy=0.5, tick_fontsize=9):
    """Set tick spacing and format for kx, ky axes, with smaller tick labels."""
    ax.xaxis.set_major_locator(MultipleLocator(dx))
    ax.yaxis.set_major_locator(MultipleLocator(dy))
    ax.xaxis.set_major_formatter(FormatStrFormatter("%.1f"))
    ax.yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
    ax.tick_params(axis="x", labelsize=tick_fontsize)
    ax.tick_params(axis="y", labelsize=tick_fontsize)
    ax.zaxis.set_tick_params(colors="black", labelsize=11)  # z ticks slightly bigger

# ================= Plot =================
fig = plt.figure(figsize=(12, 12))
cmap = plt.colormaps["turbo"]  # attractive colormap

# --- First subplot ---
ax0 = fig.add_subplot(131, projection="3d")
ax0.plot_surface(kx_mesh, ky_mesh, VBM_mesh, alpha=0.7, rstride=1, cstride=1, cmap=cmap, lw=0)
ax0.plot_surface(kx_mesh, ky_mesh, CBM_mesh, alpha=0.7, rstride=1, cstride=1, cmap=cmap, lw=0)
ax0.contourf(kx_mesh, ky_mesh, CBM_mesh, zdir="z", offset=0, cmap=cmap)
ax0.set_ylabel(r"$\mathbf{k}_{y}$")
ax0.set_zlabel(r"Energy (eV)")
ax0.set_zlim((-2, 2))
ax0.set_xticks([])
ax0.view_init(elev=0, azim=0)
format_ticks(ax0)

# --- Second subplot ---
ax = fig.add_subplot(132, projection="3d")
ax.plot_surface(kx_mesh, ky_mesh, VBM_mesh, alpha=0.7, rstride=1, cstride=1, cmap=cmap, lw=0)
ax.plot_surface(kx_mesh, ky_mesh, CBM_mesh, alpha=0.7, rstride=1, cstride=1, cmap=cmap, lw=0)
ax.contourf(kx_mesh, ky_mesh, CBM_mesh, zdir="z", offset=0, cmap=cmap)
ax.set_xlabel(r"$\mathbf{k}_{x}$")
ax.set_ylabel(r"$\mathbf{k}_{y}$")
ax.set_zlabel(r"Energy (eV)")
ax.set_zlim((-2, 2))
ax.view_init(elev=0, azim=45)
format_ticks(ax)

# --- Third subplot ---
ax1 = fig.add_subplot(133, projection="3d")
ax1.plot_surface(kx_mesh, ky_mesh, VBM_mesh, alpha=0.7, rstride=1, cstride=1, cmap=cmap, lw=0)
ax1.plot_surface(kx_mesh, ky_mesh, CBM_mesh, alpha=0.7, rstride=1, cstride=1, cmap=cmap, lw=0)
ax1.contourf(kx_mesh, ky_mesh, CBM_mesh, zdir="z", offset=0, cmap=cmap)
ax1.set_xlabel(r"$\mathbf{k}_{x}$")
ax1.set_ylabel(r"$\mathbf{k}_{y}$")
ax1.set_zlabel(r"Energy (eV)")
ax1.set_zlim((-2, 2))
ax1.view_init(elev=5, azim=45)
format_ticks(ax1)

# ================= Save =================
plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0.1, wspace=0.1)
plt.savefig("new-3D.png", dpi=600, bbox_inches="tight")
print("Saved figure as new-3D.png")

