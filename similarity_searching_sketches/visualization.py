import matplotlib.pyplot as plt
import pandas as pd


def scatter_array(arr, title=None, xlabel=None, ylabel=None, point_size=5):
    """
    Plots scatter of an array.
    :param arr: Array with data.
    :param title: Title to write.
    :param xlabel: X label.
    :param ylabel: Y label.
    :param point_size: Size of scatter point.
    :return:
    """
    ser = pd.Series(arr)
    plt.scatter(ser.index, ser, s=[point_size for _ in range(len(arr))])
    plt.suptitle(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def plot_array(arr, title=None, xlabel=None, ylabel=None, xticks=None, figsize=None):
    """
    Plots array.
    :param arr: Array with data.
    :param title: Title to write.
    :param xlabel: X label.
    :param ylabel: Y label.
    :param xticks: X ticks.
    :param figsize: Figure size in cm.
    :return:
    """
    pd.Series(arr).plot(grid=True, figsize=figsize)
    plt.suptitle(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if xticks:
        plt.xticks(range(len(xticks)), xticks)
    plt.show()


def hist_array(arr, bins=50, title=None, xlabel=None, ylabel=None, figsize=None):
    """
    Plot histogram of an array.
    :param arr: Array with data
    :param bins: Number of bins.
    :param title: Title to write.
    :param xlabel: X label.
    :param ylabel: Y label.
    :param figsize: Figure size in cm.
    :return:
    """
    pd.Series(arr).hist(bins=bins, grid=True, figsize=figsize)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.suptitle(title)
    plt.show()
