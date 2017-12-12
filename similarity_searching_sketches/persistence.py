import numpy as np


def save_np_array(file_path, arr):
    """
    Saves NumPy array into a file.
    :param file_path: File path.
    :param arr: Numpy array.
    :return:
    """
    with open(file_path, 'wb') as f:
        np.save(f, arr)


def load_np_array(file_path):
    """
    Loads numpy array from a file.
    :param file_path: File path.
    :return: Numpy array.
    """
    with open(file_path, 'rb') as f:
        return np.load(f)
