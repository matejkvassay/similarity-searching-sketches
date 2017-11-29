import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def show_text(title, xlabel, ylabel):
    plt.suptitle(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)


def heatmap(x, y, bins=50, figsize=(5, 5), title=None, xlabel=None, ylabel=None):
    plt.figure(figsize=figsize)
    heatmap, xedges, yedges = np.histogram2d(x, y, bins)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    plt.clf()
    plt.imshow(heatmap.T, extent=extent, origin='lower')
    show_text(title, xlabel, ylabel)
    plt.show()


def scatter(x, y, title=None, xlabel=None, ylabel=None, point_size=5):
    plt.scatter(x, y, s=[point_size for _ in range(len(x))])
    plt.suptitle(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def scatter_array(arr, title=None, xlabel=None, ylabel=None, point_size=5):
    ser = pd.Series(arr)
    plt.scatter(ser.index, ser, s=[point_size for _ in range(len(arr))])
    plt.suptitle(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def plot_array(arr, title=None, xlabel=None, ylabel=None, xticks=None):
    pd.Series(arr).plot(grid=True)
    plt.suptitle(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if xticks:
        plt.xticks(range(len(xticks)), xticks)
    plt.show()


def hist_array(arr, bins=50, title=None, xlabel=None, ylabel=None):
    pd.Series(arr).hist(bins=bins, grid=True)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.suptitle(title)
    plt.show()


def restrict_2d_space(x, y, x_interval, y_interval):
    conditions = [x >= x_interval[0], x <= x_interval[1], y >= y_interval[0], y <= y_interval[1]]
    mask = conditions[0]
    for condition in conditions[1:]:
        mask = np.logical_and(mask, condition)
    return x[mask], y[mask]
