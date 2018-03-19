import pytest
from source.FileChecker import FileChecker
from pathlib import Path
from source.config import cfg
from source.custom_logger import logme

@pytest.fixture()
def fileChecker():
    return FileChecker()

@pytest.fixture()
def config():
    return cfg

def test_programRootDirIsAPath():
    assert Path(fileChecker().getProgramDirectory()).is_dir() == True

