import pytest
from source.categories import *

def test_getCategoriesSectionGetsADictWithValues():
    assert type(cat.getCategoriesSection()) == list
    assert type(cat.getCategoriesSection()[0]) == dict
    for k,v  in cat.getCategoriesSection()[0].items():
        assert k != None
        assert v != None
