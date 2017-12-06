import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def show_text(title, xlabel, ylabel):
    plt.suptitle(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)


def scatter_array(arr, title=None, xlabel=None, ylabel=None, point_size=5):
    ser = pd.Series(arr)
    plt.scatter(ser.index, ser, s=[point_size for _ in range(len(arr))])
    plt.suptitle(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def plot_array(arr, title=None, xlabel=None, ylabel=None, xticks=None, figsize=None):
    pd.Series(arr).plot(grid=True, figsize=figsize)
    plt.suptitle(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if xticks:
        plt.xticks(range(len(xticks)), xticks)
    plt.show()


def hist_array(arr, bins=50, title=None, xlabel=None, ylabel=None, figsize=None):
    pd.Series(arr).hist(bins=bins, grid=True, figsize=figsize)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.suptitle(title)
    plt.show()
