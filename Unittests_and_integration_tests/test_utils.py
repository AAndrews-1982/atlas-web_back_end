#!/usr/bin/env python3
"""
This module contains unit tests for 'access_nested_map'
from 'utils'. It tests various scenarios to validate
successful and erroneous behaviors.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test suite for 'access_nested_map' in 'utils'.

    This suite tests different nested map structures and path sequences.
    It checks successful accesses and error handling for invalid paths.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
