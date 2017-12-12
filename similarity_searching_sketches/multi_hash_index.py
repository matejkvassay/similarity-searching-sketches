import numpy as np
from similarity_searching_sketches.distances import hamming


class MultiHashIndex(object):
    """
    Implementation of multi hash index with fixed search radius for similarity searching on binary strings.
    """

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

    def range_query(self, obj, r, stats_counter=None):
        """
        Execute range query on objects inside the index.
        :param obj: Sketch object.
        :param r: Search adius. Used to control filtering phase however candidate set will always contain all sketches
                  up to range m-1.
        :param stats_counter: MHI stats counter.
        :return: Iterable of object ID's.
        """
        sketch = obj[1]
        if r >= self.m:
            raise ValueError('Range (r) must be lesser than number of substrings (m).')
        candidates = self.get_range_query_candidate_ids(sketch, stats_counter=stats_counter)
        result = set([obj_id for obj_id in candidates if hamming(sketch, self.sketches[obj_id]) <= r])
        return result

    def get_range_query_candidate_ids(self, sketch, stats_counter=None):
        """
        Returns candidate set for given sketch.
        :param sketch: Binary array.
        :param stats_counter: MHI stats counter.
        :return: ID's of candidates after the union.
        """
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
        """
        Returns all objects in a bucket for given sketch substring.
        :param idx: Hash index ID.
        :param sketch_substr: Substring.
        :return: Set of id's or empty set.
        """
        key = self.get_key(sketch_substr)
        if key in self.index[idx]:
            return self.index[idx][key]
        else:
            return set()

    def index_obj(self, idx, obj_id, sketch_substr):
        """
        Stores object and it's sketch in hash indices and reverse index.
        :param idx: Hash index ID.
        :param obj_id:
        :param sketch_substr:
        :return:
        """
        key = self.get_key(sketch_substr)
        if key in self.index[idx]:
            self.index[idx][key].add(obj_id)
        else:
            new_set = set()
            new_set.add(obj_id)
            self.index[idx][key] = new_set

    def insert(self, objects, stats_counter=None):
        """
        Inserts iterable of objects into MHI.
        :param objects: Iterable of objects.
        :param stats_counter: MHI stats counter.
        :return:
        """
        for obj_id, sketch in objects:
            self.sketches[obj_id] = sketch
            [self.index_obj(idx, obj_id, substr) for idx, substr in enumerate(np.array_split(sketch, self.m))]

    @staticmethod
    def get_key(sketch_substr):
        """
        Returns key of sketch substring in reverse index.
        :param sketch_substr: Sketch substring.
        :return:
        """
        return str(sketch_substr)
