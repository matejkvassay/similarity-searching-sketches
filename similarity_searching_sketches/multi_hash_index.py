import numpy as np


class MultiHashIndex(object):
    def __init__(self, sketch_db, m):
        """
        :param sketch_db: Database of (obj_id, sketch)
        :param sketch_producer: SketchProducer instance
        :param m: Number of splits.
        """
        self.m = m
        self.sketches = dict()
        self.index = [dict() for _ in range(self.m)]
        self.insert(sketch_db)

    @staticmethod
    def hamming_dist(sketch_a, sketch_b, stats_counter=None):
        assert len(sketch_a) == len(sketch_b)
        dist = sum([abs(sketch_a[i] - sketch_b[i]) for i in range(len(sketch_a))])
        if stats_counter is not None:
            stats_counter.add('hamming_dist', dist)
        return dist

    def range_query(self, obj, r, stats_counter=None):
        sketch = obj[1]
        if r >= self.m:
            raise ValueError('Range (r) must be lesser than number of substrings (m).')
        candidates = self.get_range_query_candidate_ids(sketch, stats_counter=stats_counter)
        result = set([obj_id for obj_id in candidates if \
                      MultiHashIndex.hamming_dist(sketch, self.sketches[obj_id], stats_counter=stats_counter) <= r])
        return result

    def get_range_query_candidate_ids(self, sketch, stats_counter=None):
        candidates = set()
        count_before_union = 0
        for idx, split in enumerate(np.array_split(sketch, self.m)):
            candidates_to_add = self.get_bucket_obj_ids(idx, split)
            count_before_union += len(candidates_to_add)
            candidates = candidates.union(candidates_to_add)
        if stats_counter is not None:
            stats_counter.add('rq_candidates_cnt', len(candidates))
            stats_counter.add('rq_candidates_before_union_cnt', count_before_union)
        return candidates

    def get_bucket_obj_ids(self, idx, sketch_substr):
        key = self.get_key(sketch_substr)
        if key in self.index[idx]:
            return self.index[idx][key]
        else:
            return set()

    def index_obj(self, idx, obj_id, sketch_substr):
        key = self.get_key(sketch_substr)
        if key in self.index[idx]:
            self.index[idx][key].add(obj_id)
        else:
            new_set = set()
            new_set.add(obj_id)
            self.index[idx][key] = new_set

    def insert(self, objects, stats_counter=None):
        for obj_id, sketch in objects:
            self.sketches[obj_id] = sketch
            [self.index_obj(idx, obj_id, substr) for idx, substr in enumerate(np.array_split(sketch, self.m))]

    def get_key(self, sketch_substr):
        return str(sketch_substr)
