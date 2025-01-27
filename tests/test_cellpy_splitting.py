import logging

import pandas as pd
import pytest

from cellpy import log
from cellpy.exceptions import NullData
from cellpy.utils import helpers

log.setup_logging(default_level=logging.DEBUG, testing=True)


# TODO: manually renaming cellpy fixture to cell; remove this when all instances of dataset is renamed to cell
@pytest.fixture
def cell(dataset):
    return dataset


def test_split(cell):
    list_of_all_cycles = cell.get_cycle_numbers()
    c1, c2 = cell.split(10)
    list_of_first_cycles = c1.get_cycle_numbers()
    list_of_last_cycles = c2.get_cycle_numbers()
    assert list_of_first_cycles[0] == 1
    assert list_of_first_cycles[-1] == 9
    assert list_of_all_cycles[-1] == list_of_last_cycles[-1]


def test_drop_to(cell):
    c1 = cell.drop_to(10)
    list_of_new_cycles = c1.get_cycle_numbers()
    print(list_of_new_cycles)
    assert list_of_new_cycles[0] == 10
    assert list_of_new_cycles[-1] == cell.get_cycle_numbers()[-1]


def test_drop_from(cell):
    c1 = cell.drop_from(10)
    list_of_new_cycles = c1.get_cycle_numbers()
    assert list_of_new_cycles[0] == 1
    assert list_of_new_cycles[-1] == 9
