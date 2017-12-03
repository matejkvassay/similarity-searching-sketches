import numpy as np
from similarity_searching_sketches.log_utils import IterationLogger


def sort_ids_by_distance(ids, database, queries, dist_f, log_by=5000):
    """
    Sorts objects from database by distances to query objects for all given queries.
    :param ids: Object ID's
    :param database: Objects
    :param queries: Query objects
    :param dist_f: Distance function
    :param log_by:
    :return:
    """
    iter_log = IterationLogger(log_by=log_by)
    distances = np.zeros(shape=(queries.shape[0], database.shape[0]))
    for i, obj in enumerate(database):
        iter_log.next_iter()
        for j, query in enumerate(queries):
            distances[j][i] = dist_f(obj, query)
    return np.array([ids[np.argsort(dist_list)] for dist_list in distances])


def compute_knn_results(ids, database, queries, k, dist_f, log_by=5000):
    """
    Iterates over given vectors and looks for nearest neighbors for given query objects.
    :param ids: ID's of objects in the database.
    :param database: Vectors or Sketches from the database.
    :param queries: Array of query objects.
    :param k: Number of nearest neighbors to find.
    :param dist_f: Distance function.
    :param log_by: Log iterations by.
    :return: Array containing lists of nearest neighbor ID's for each query object.
    """
    knn_res = [list() for _ in range(queries.shape[0])]
    iter_log = IterationLogger(log_by=log_by)
    for i in range(len(database)):
        iter_log.next_iter()
        for j in range(len(queries)):
            dist = dist_f(database[i], queries[j])
            if len(knn_res[j]) > 0:
                if dist < knn_res[j][-1][1]:  # if object is not member of result set
                    knn_res[j].append((ids[i], dist))
                    knn_res[j].sort(key=lambda x: x[1], reverse=False)
                    if len(knn_res[j]) > k:  # if > k objects remove last one
                        del knn_res[j][-1]
            else:
                knn_res[j].append((ids[i], dist))
    return np.array(knn_res)
