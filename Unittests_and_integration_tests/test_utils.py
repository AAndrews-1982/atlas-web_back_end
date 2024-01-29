#!/usr/bin/env python3
"""Unittests"""
import unittest
from unittest import mock
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test Suit AccessNestedMap."""
    """ to test the function for following inputs """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Method to test that the method returns what it is supposed to."""
        self.assertEqual(access_nested_map(nested_map, path),
                         expected_result)

    """We use the assertRaises context manager to test that a
    KeyError is raised for the following inputs"""

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expec_except):
        """Method that test that a KeyError is raised according inputs"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
            self.assertEqual(expec_except, error.exception)
