import numpy as np
from scipy.spatial.distance import minkowski


def get_dist_from_dividing_hp(dist_a, dist_b):
    """
    Get distance from dividing hyperplane.
    :param dist_a: Distance to first pivot.
    :param dist_b: Distance to second pivot.
    :return:
    """
    if dist_a < dist_b:
        return (float(dist_a + dist_b) / 2) - dist_a
    else:
        return (float(dist_a + dist_b) / 2) - dist_b


def assign_ghp_partition(obj, pivot_a, pivot_b, p=1, distance_to_hp=False):
    """
    Get GHP partition.
    :param obj: Object vector
    :param pivot_a: First pivot
    :param pivot_b: Second pivot
    :param p: p-paramter of Minkowski distance
    :param distance_to_hp: Whether to return distance of object to dividing hyperplane
    :return Assigned partition either 0 or 1.
    """
    dist_a = minkowski(obj, pivot_a, p=p)
    dist_b = minkowski(obj, pivot_b, p=p)
    if dist_a < dist_b:
        partition = 1
    elif dist_a > dist_b:
        partition = 0
    else:
        partition = np.random.choice([0, 1])
    if distance_to_hp:
        dist = get_dist_from_dividing_hp(dist_a, dist_b)
        return partition, dist
    else:
        return partition


def balance_score(cnt_partition, cnt_all):
    """
    Compute balance score.
    :param cnt_partition: Count objects in one partition.
    :param cnt_all: Count all objects.
    """
    return 1.0 - (2 * abs(0.5 - (cnt_partition / cnt_all)))
