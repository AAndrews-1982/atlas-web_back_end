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
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test 'access_nested_map' for various structures and paths.

        Asserts that the function's return matches the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        """
        Test error handling in 'access_nested_map' with invalid paths.
        Ensures KeyError is raised for non-existent keys in the map.

        Asserts KeyError is raised with the expected key.
        """
        with self.assertRaises(KeyError) as raised_exception:
            access_nested_map(nested_map, path)
        self.assertEqual(str(expected_key), str(raised_exception.exception))


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test the get_json function to ensure it returns the expected result.
        """
        with patch('requests.get') as mock_get:
            mock_get.return_value = Mock(json=lambda: test_payload)
            response = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(response, test_payload)


if __name__ == "__main__":
    unittest.main()
