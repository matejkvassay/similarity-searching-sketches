from sketch_searching.util import get_cfg
import os

TEST_FILE_PREFIX = 'test_util_py_sqt2teaddvgzdgtt5ophujhbdsr'


def test_read_cfg():
    test_cfg = """
        category:
            value: 'val'
    """
    with open('./'+TEST_FILE_PREFIX + 'test_read_cfg_file.yml', 'wb') as f:
        f.writelines(test_cfg)

    test_cfg_dict = {'category': {'value': 'val'}}
    cfg_dict = get_cfg(test_cfg_dict)
    assert type(cfg_dict) == dict
    assert cfg_dict['category']['value'] == 'val'

    cfg_dict = get_cfg(test_cfg_dict)
    assert type(cfg_dict) == dict
    assert cfg_dict['category']['value'] == 'val'

    os.remove('./'+TEST_FILE_PREFIX + 'test_read_cfg_file.yml')