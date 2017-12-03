from similarity_searching_sketches.partitioning import assign_ghp_partition
from similarity_searching_sketches.persistence import load_np_array
import numpy as np


class MinkowskiSketchProducer(object):
    def __init__(self, pivots_path, p=1):
        self.p = p
        self.pivots = load_np_array(pivots_path)

    def transform_object(self, vec):
        return np.array(
            [assign_ghp_partition(vec, pivot_cpl[0], pivot_cpl[1], p=self.p, distance_to_hp=False) for pivot_cpl in
             self.pivots])

    def transform_many(self, vecs):
        return np.array([self.transform_object(vec) for vec in vecs])
