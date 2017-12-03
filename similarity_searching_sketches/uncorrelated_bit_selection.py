import numpy as np
from similarity_searching_sketches.correlation_matrix import get_upper_triangle_values


def select_random_subset(corr_mtx, p, k):
    """
    Selects k random p-subsets of bits of Sketch Matrix and selects the one resulting in lowest mean correlation
    of upper triangle in given Sketch Correlation Matrix.
    :param corr_mtx: Sketch Correlation Matrix
    :param p: Desired Sketch length
    :param k: Number of subsets to evaluate
    :return: Tuple (array of selected column indices, mean correlation, correlation st.dev)
    """
    if p < 2:
        return None, None, None
    rang = np.arange(corr_mtx.shape[0])
    subsets = np.array([np.random.choice(rang, size=p, replace=False) for _ in range(k)])
    best_subset = None
    best_corr_mean = 1.0
    best_corr_std = 0.0
    for indices in subsets:
        upper_tria = get_upper_triangle_values(corr_mtx, include=indices)
        corr_mean = np.mean(upper_tria)
        if corr_mean <= best_corr_mean:
            best_corr_mean = corr_mean
            best_corr_std = np.std(upper_tria)
            best_subset = indices
    return np.array(best_subset), best_corr_mean, best_corr_std


def fast_minimal_correlation_columns(corr_mtx, p):
    """
    Implementation of FMCC algorithm. Selects low correlated subset of bits.
    :param corr_mtx: Sketch Correlation Matrix
    :param p: Desired Sketch length
    :return: Tuple (array of selected column indices, mean correlation, correlation st.dev)
    """
    if p < 2:
        return None, None, None
    else:
        selected_cols = np.sum(corr_mtx, axis=1).argsort()[:p]
        upper_tria = get_upper_triangle_values(corr_mtx, include=selected_cols)
        return selected_cols, np.mean(upper_tria), np.std(upper_tria)


def greedy_minimal_correlation_columns(corr_mtx, p):
    """
    Implementation of GMCC algorithm. Selects low correlated subset of bits.z
    :param corr_mtx: Sketch Correlation Matrix
    :param p: Desired Sketch length
    :return: Tuple (array of selected column indices, mean correlation, correlation st.dev)
    """
    if p < 2:
        return None, None, None
    least_correlated = np.argmin(np.sum(corr_mtx, axis=1))
    indices = []  # to keep them sorted
    indices_lookup = set()  # to speed up search for membership
    indices.append(least_correlated)
    indices_lookup.add(least_correlated)
    while len(indices) < p:
        best_i = None
        best_mean_corr = 1.0
        best_corr_std = 1.0
        for i in range(corr_mtx.shape[0]):
            if i not in indices_lookup:
                upper_tria = get_upper_triangle_values(corr_mtx, include=list(indices) + [i])
                corr_mean = np.mean(upper_tria)
                if corr_mean < best_mean_corr:
                    best_i = i
                    best_mean_corr = corr_mean
                    best_corr_std = np.std(upper_tria)
        indices_lookup.add(best_i)
        indices.append(best_i)
    return np.array(indices), best_mean_corr, best_corr_std
