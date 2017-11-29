import numpy as np


class CaffeVectorsIterator(object):
    def __init__(self, file_path, limit=None, allow_duplicities=True):
        self.f = open(file_path, 'rb')
        self.limit = limit
        self.allow_dupl = allow_duplicities

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.f:
            self.f.close()

    def __iter__(self):
        if self.limit is not None:
            self.returned = 0
        if not self.allow_dupl:
            self.mem = set()
        return self

    def __next__(self):
        try:
            # (id: int, vector: np array of float32)
            if self.limit is not None:
                if self.returned == self.limit:
                    self.f.close()
                    raise StopIteration

            line_a = self.f.__next__()
            line_b = self.f.__next__()
            obj_id = int(line_a.decode().split(' ')[2])
            obj_vector = np.fromstring(line_b, dtype='f', sep=' ')
            if not self.allow_dupl:
                if str(obj_vector) in self.mem:
                    return self.__next__()
                else:
                    if self.limit is not None:
                        self.returned += 1
                    self.mem.add(str(obj_vector))
                    return obj_id, obj_vector
            else:
                if self.limit is not None:
                    self.returned += 1
                    return obj_id, obj_vector
        except StopIteration:
            self.f.close()
            raise StopIteration

    def __del__(self):
        if self.f:
            self.f.close()
