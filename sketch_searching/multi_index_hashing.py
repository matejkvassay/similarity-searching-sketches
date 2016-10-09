#TO DO: Classes SOS, RHMI, RHMIA

# class RestrictedHashMultiIndex():
#     def __init__(self, database_iterator, substr_cnt, sketch_len):
#         """
#         Restricted means that radius in queries must be < substr_cnt
#
#         :param database_iterator: iterator for objects (Bits: sketch, int: obj_id)
#         """
#         self.substr_cnt = substr_cnt  # m
#         self.sketch_len = sketch_len  # p
#         self.buckets = dict()  # this dict will contain search buckets {sketch: set(object id's), ...}
#         for sketch, obj_id in database_iterator:
#             if self.buckets.get(sketch) is None:
#                 self.buckets[sketch] = set()
#             self.buckets[sketch].add(obj_id)
#
#     def range_query(self, query_sketch, radius):
#         if not radius<self.substr_cnt:
#             raise ValueError('Radius for range query must be < count of substrings.')
#         max_different_bits = radius / self.substr_cnt
#         if max_different_bits == 0:
#             # great
#             pass
#         else:
#             # oh my...
#             pass
#
#     def k_nn_query(self, query_sketch, k):
#         pass
