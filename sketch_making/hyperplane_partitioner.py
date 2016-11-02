from util import get_cfg
from sklearn.neighbors import DistanceMetric
from data_processing.caffe_vectors_iterator import CaffeVectorsIterable


class MultiHyperplanePartitioner():
    def __init__(self, cfg):
        cfg = get_cfg(cfg)
        self.dist_metric = DistanceMetric(cfg['dist_metric'])  # for example 'euclidean'
        self.read_pivots(cfg)

    def read_pivots(self, cfg):
        self.pivots = list()
        iterator = CaffeVectorsIterable(cfg['pivots_file_path']).__iter__()

        for i in xrange(int(cfg['pivot_couples_count'])):
            try:
                pivot_A = iterator.next()
                pivot_B = iterator.next()
                self.pivots.append((pivot_A, pivot_B))
            except StopIteration:
                raise ValueError(
                    'Number of pivots in file must be equal or higher than 2x number of pivot couples (pivot_couples_count in config).')

    def get_partition(self, pivot_couple, obj):
        distance_A = self.dist_metric.pairwise(obj[1], pivot_couple[0][1])[0][0]  # pairwise returns matrix
        distance_B = self.dist_metric.pairwise(obj[1], pivot_couple[1][1])[0][0]
        if distance_A > distance_B:
            return 0
        else:
            return 1

    def get_partitions(self, obj):
        return [self.get_partition(pivot_couple, obj) for pivot_couple in self.pivots]
