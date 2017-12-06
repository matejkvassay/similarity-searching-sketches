import pandas as pd
import numpy as np
from similarity_searching_sketches.utils import percentage


class ListStatsCounter(object):
    def __init__(self):
        self.stats = dict()

    def add(self, key, val):
        if key in self.stats:
            self.stats[key].append(val)
        else:
            self.stats[key] = [val]

    def to_df(self):
        return pd.DataFrame.from_dict(self.stats)


def stats_to_pandas(keys, stats):
    return pd.DataFrame.from_dict({key: stats[key] for key in keys}).reindex_axis(keys, axis=1)


def bucket_stats(mhis, m_list):
    keys = ['m', 'r', 'Bucket count', 'Bucket size mean', 'Bucket size st. dev.', 'Bucket size sum',
            'm x Bucket size mean']
    stats = {key: [] for key in keys}
    for i, mhi in enumerate(mhis):
        bucket_obj_cnt = []
        for index in mhi.index:
            for bucket in index:
                bucket_obj_cnt.append(len(index[bucket]))
        stats['m'].append(m_list[i])
        stats['r'].append(m_list[i] - 1)
        stats['Bucket count'].append(len(bucket_obj_cnt))
        stats['Bucket size mean'].append(np.mean(bucket_obj_cnt))
        stats['Bucket size st. dev.'].append(np.std(bucket_obj_cnt))
        stats['Bucket size sum'].append(sum(bucket_obj_cnt))
        stats['m x Bucket size mean'].append(m_list[i] * np.mean(bucket_obj_cnt))
    return keys, stats


def rq_candidate_set_size_stats(queries, mhis, m_list):
    keys = ['m', 'r', 'm x Bucket size mean', 'Mean |C_1|+...+|C_m|', 'Mean |C|', 'Mean % filtered out']
    stats = {key: [] for key in keys}
    for i, mhi in enumerate(mhis):
        m = m_list[i]
        r = m - 1
        stats_counter = ListStatsCounter()
        for query in queries:
            mhi.range_query(query, r, stats_counter=stats_counter)
        c_size = np.mean(stats_counter.stats['rq_candidates_cnt'])
        c_size_before_union = np.mean(stats_counter.stats['rq_candidates_before_union_cnt'])
        stats['m'].append(m)
        stats['r'].append(r)
        stats['Mean |C_1|+...+|C_m|'].append(c_size_before_union)
        stats['Mean |C|'].append(c_size)
        if c_size_before_union == 0:
            stats['Mean % filtered out'].append(0.0)
        else:
            stats['Mean % filtered out'].append(100.0 - percentage(c_size, c_size_before_union))
        bucket_cnts = bucket_sizes(mhi)
        stats['m x Bucket size mean'].append(np.mean(bucket_cnts) * m)
    return keys, stats


def bucket_sizes(mhi):
    bucket_obj_cnt = list()
    for index in mhi.index:
        for bucket in index:
            bucket_obj_cnt.append(len(index[bucket]))
    return bucket_obj_cnt
