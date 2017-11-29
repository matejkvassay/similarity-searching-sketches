import numpy as np
import pickle


def pickle_dump(obj, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(obj, f)


def unpickle(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)


def save_np_array(file_path, arr):
    with open(file_path, 'wb') as f:
        np.save(f, arr)


def load_np_array(file_path):
    with open(file_path, 'rb') as f:
        return np.load(f)
