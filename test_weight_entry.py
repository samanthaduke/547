# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 15:40:11 2022

@author: Samantha Eaton
"""

import pytest


@pytest.mark.parametrize("input, expected", [
    ("22 lb", 10),
    ("50 kg", 50),
    ("23.6 kg", 24),
    ("22 lbs", 10),
    # ("22lbs", 10),
    ("22 LB", 10),
    ("-22 lbs", -10),
    # ("ten kg", 10),
])
def test_parse_weight_input(input, expected):
    from weight_entry import parse_weight_input
    answer = parse_weight_input(input)
    assert answer == expected
