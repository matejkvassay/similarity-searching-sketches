import pandas as pd
import numpy as np
from similarity_searching_sketches.utils import percentage


class ListStatsCounter(object):
    """
    Collector of statistics for evaluation of MHI.
    """

    def __init__(self):
        self.stats = dict()

    def add(self, key, val):
        """
        Adds new value to list under the key.
        :param key:
        :param val:
        :return:
        """
        if key in self.stats:
            self.stats[key].append(val)
        else:
            self.stats[key] = [val]

    def to_df(self):
        """
        Transforms stats counter to pandas dataframe.
        :return: Pandas dataframe of stats.
        """
        return pd.DataFrame.from_dict(self.stats)


def stats_to_pandas(keys, stats):
    """
    Transforms dictionary of statistics with known keys to pandas dataframe.
    :param keys: Keys of columns for dataframe/
    :param stats: Dictionary of stats.
    :return:
    """
    return pd.DataFrame.from_dict({key: stats[key] for key in keys}).reindex_axis(keys, axis=1)


def bucket_stats(mhis, m_list):
    """
    Computes bucket statistics for given iterable of Multi-hash indexes.
    :param mhis: Iterable of MHI's.
    :param m_list: List of split sizes.
    :return: Tuple keys, stats, where stats is a dictionary of computed statistics.
    """
    keys = ['m', 'r', 'Bucket count', 'Bucket size mean', 'Bucket size sum',
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
        stats['Bucket size sum'].append(sum(bucket_obj_cnt))
        stats['m x Bucket size mean'].append(m_list[i] * np.mean(bucket_obj_cnt))
    return keys, stats


def rq_candidate_set_size_stats(queries, mhis, m_list, obj_cnt):
    """
    Evaluates multiple range queries on iterable of MHI's and computes mean statistics of candidate sets.
    :param queries: Iterable of query sketches.
    :param mhis: Iterable of MHI's.
    :param m_list: Iterable of numbers of splits of MHI's.
    :param obj_cnt: Count of objects in dataset to compute % from.
    :return: Tuple keys, stats, where stats is a dictionary of computed statistics.
    """
    keys = ['m', 'r', 'Mean TP count', 'm x Bucket size mean', 'Mean |C_1|+...+|C_m|', 'Mean |C|',
            'Mean % bucket overlap',
            'Mean % db filtered']
    stats = {key: [] for key in keys}
    for i, mhi in enumerate(mhis):
        m = m_list[i]
        r = m - 1
        stats_counter = ListStatsCounter()
        for query in queries:
            res = mhi.range_query(query, r, stats_counter=stats_counter)
            stats_counter.add('res_len', len(res))
        c_size = np.mean(stats_counter.stats['rq_candidates_cnt'])
        c_size_before_union = np.mean(stats_counter.stats['rq_candidates_before_union_cnt'])
        tp_cnt = np.mean(stats_counter.stats['res_len'])
        stats['m'].append(m)
        stats['r'].append(r)
        stats['Mean |C_1|+...+|C_m|'].append(c_size_before_union)
        stats['Mean |C|'].append(c_size)
        if c_size_before_union == 0:
            stats['Mean % bucket overlap'].append(0.0)
        else:
            stats['Mean % bucket overlap'].append(100.0 - percentage(c_size, c_size_before_union))
        bucket_cnts = bucket_sizes(mhi)
        stats['m x Bucket size mean'].append(np.mean(bucket_cnts) * m)
        stats['Mean % db filtered'].append(percentage(obj_cnt - c_size, obj_cnt))
        stats['Mean TP count'].append(tp_cnt)

    return keys, stats


def bucket_sizes(mhi):
    """
    Returns iterable of bucket sizes for given MHI.
    :param mhi: MHI.
    :return: Iterable of bucket sizes.
    """
    bucket_obj_cnt = list()
    for index in mhi.index:
        for bucket in index:
            bucket_obj_cnt.append(len(index[bucket]))
    return bucket_obj_cnt
