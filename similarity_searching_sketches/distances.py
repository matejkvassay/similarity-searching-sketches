from similarity_searching_sketches.log_utils import IterationLogger
from similarity_searching_sketches.log_utils import log
import numpy as np
from scipy.spatial.distance import minkowski


def hamming(a, b):
    """
    Computers hamming distance between two binary strings.
    :param a: First object.
    :param b: Second object.
    :return: Hamming distance.
    """
    return np.count_nonzero(a != b)


def l1(a, b):
    """
    Computes Manhattan distance between two vectors.
    :param a: Vector A.
    :param b: Vector B.
    :return: Minkowski L1 distance.
    """
    return minkowski(a, b, p=1)


def get_sample_distances(vec_matrix, sample_size, p, log_by=5000):
    """
    Selects given number of reference objects from given vector matrix and computes distances from them to all other rows.
    :param vec_matrix: Vectors numpy matrix - one row one object
    :param sample_size: How many objects to randomly choose as reference objects
    :param p: p-param of Minkowski distance, can be either 1 value or iterable of multiple values
    :param log_by: How many iterations to log by
    :return: Tuple of lists of distances for each given p.
    """
    distances = [[] for _ in range(len(p))]
    chosen_indices = np.random.choice(vec_matrix.shape[0], size=sample_size, replace=False)
    reference_objects = vec_matrix[chosen_indices]
    matrix = np.delete(vec_matrix, chosen_indices, axis=0)
    iter_log = IterationLogger(log_by=log_by)
    log(
        'Going to compute distances from selected {} reference objects to all {} other objects in given matrix for p={}.'.format(
            reference_objects.shape[0], matrix.shape[0], p))
    for vec in matrix:
        iter_log.next_iter()
        for ref_obj in reference_objects:
            for i, val_p in enumerate(p):
                dist = minkowski(ref_obj, vec, p=val_p)
                distances[i].append(dist)
    return tuple(distances)
