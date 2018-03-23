import pytest
from source.categories import configCategories

@pytest.fixture()
def getcat():
    """
    This initiates category class
    :return:
    """
    return configCategories


def test_getCategoriesSectionGetsADictWithValues():
    typeOfGetCats = type(getcat().getCategoriesSection())
    assert typeOfGetCats == list

    for k,v  in getcat().getCategoriesSection()[0].items():
        assert k != None
        assert v != None
