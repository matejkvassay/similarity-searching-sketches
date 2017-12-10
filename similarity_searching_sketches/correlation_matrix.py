import numpy as np


def compute_corr_mtx(sketch_matrix):
    """
    Computes Correlation Matrix from given Sketch matrix.
    :param sketch_matrix: Numpy matrix, 1 row - 1 sketch
    :return: Pearson correlation matrix
    """
    corr_mtx = np.absolute(np.corrcoef(sketch_matrix.T))
    np.fill_diagonal(corr_mtx, 0.0)
    return corr_mtx


def get_upper_triangle_values(mtx, include=None, exclude=None):
    """
    Get values from upper triangle of Matrix.
    :param mtx: Numpy matrix
    :param include: If not None only columns and rows with these indices will be included.
    :param exclude: If not None all columns and rows with these indices will be excluded.
    :return: Array of values from upper triangle of given matrix.
    """
    if include is None and exclude is None:
        u = np.triu_indices(n=mtx.shape[0], m=mtx.shape[1], k=1)
        return mtx[u]
    if include is not None:
        selection = mtx[include].T[include]
        u = np.triu_indices(n=selection.shape[0], m=selection.shape[1], k=1)
        return selection[u]
    if exclude is not None:
        mask = np.ones(mtx.shape[0], dtype=bool)
        mask[exclude] = 0
        selection = mtx[mask].T[mask]
        u = np.triu_indices(n=selection.shape[0], m=selection.shape[1], k=1)
        return selection[u]
    raise ValueError('Choose only indices to either include or exclude, not both.')


def get_one_vs_all_corrs(corr_mtx, col_idx):
    """
    Returns list of 1 vs All correlations for given bit index.
    :param corr_mtx: Sketch correlation matrix.
    :param col_idx: Index of bit to compute correlations from
    :return: Array of correlations except for indentity correlation.
    """
    return np.delete(corr_mtx[:, col_idx], col_idx)
