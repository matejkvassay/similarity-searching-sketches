from data_processing.decaf_vectors_iterator import CaffeVectorsIterable
import numpy as np

TEST_FILE_PATH = 'tests/data/caffe_vectors_iterator_test.data'


def test_caffe_vectors_iterator():
    iterator = CaffeVectorsIterable(TEST_FILE_PATH)
    data=[item for item in iterator]
    assert len(data) == 4
    num=1
    for item in data:
        assert type(item)==tuple
        assert type(item[0])==int
        assert item[0]==num
        assert type(item[1])==np.ndarray
        assert item[1].all()==np.array([float(num)*0.001]*5).all()
        num+=1

