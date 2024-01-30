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
        # Add more test cases for successful access if needed
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test access_nested_map for successful scenarios """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "KeyError accessing ['a']"),
        ({"a": 1}, ("a", "b"), "KeyError accessing ['a']['b']"),
    ])
    def test_access_nested_map_exception(
          self, nested_map, path, expected_message):
        """ Test access_nested_map for exceptions """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_message)

# Add additional test methods if needed


if __name__ == "__main__":
    unittest.main()
