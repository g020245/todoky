import pytest
from source.FileChecker import FileChecker
from pathlib import Path
from source.config import config
from source.custom_logger import logme

@pytest.fixture()
def fileChecker():
    return FileChecker()

@pytest.fixture()
def config():
    return config

def test_programRootDirIsAPath():
    """
    Gets a valid directory path
    :return:
    """
    assert Path(fileChecker().getProgramDirectory()).is_dir() == True

def test_getValidMainInputPath():
    """
    Gets a valid main input path
    :return:
    """
    assert Path(fileChecker().getMainInputPath()).is_dir() == True
