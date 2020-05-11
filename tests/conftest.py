import pytest
import os
import yaml


def get_path_info():
    with open(os.getcwd() + '/resources/config.yaml', 'r') as f:
        return yaml.load(f, Loader=yaml.FullLoader)


@pytest.fixture(scope='session', autouse=True)
def host():
    return get_path_info()['api']['host']
