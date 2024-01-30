#!/usr/bin/env python3
"""
This module contains unit tests for 'access_nested_map'
from 'utils'. It tests various scenarios to validate
successful and erroneous behaviors.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch, Mock


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
    """
    Class that tests the get_json function which retrieves
    JSON from a remote URL.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Mocking the requests.get method to test the get_json function.

        Ensures that the get_json function returns the correct payload and
        the json method of the mock response is called exactly once.
        """
        mock_response = mock.Mock()
        mock_response.json.return_value = test_payload

        with mock.patch('requests.get', return_value=mock_response):
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_response.json.assert_called_once()


class TestGetJson(unittest.TestCase):
    """
    Test suite for testing the 'get_json' function.

    This suite uses parameterized tests to
    ensure 'get_json' correctly fetches and
    returns data from different URLs.
    It mocks external HTTP requests to avoid
    network dependency and ensure test reliability.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url, returned_payload):
        """
        Test the 'get_json' function with mocked HTTP responses.

        Ensures that 'get_json' returns the correct data and
        the mocked 'json' method is called exactly once.
        """
        mock_response = Mock()
        mock_response.json.return_value = returned_payload
        with patch('requests.get', return_value=mock_response):
            self.assertEqual(get_json(url), returned_payload)
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """
    Test suite for testing the 'memoize' decorator.

    This suite tests the 'memoize' decorator to ensure it correctly caches
    the results of methods it is applied to, thereby avoiding redundant
    computations.
    """
    def test_memoize(self):
        """
        Test the 'memoize' decorator on a method.

        This test creates a test class with a method and a property.
        The property is decorated with 'memoize' to test if the result
        is correctly memoized.
        """
        class TestClass:
            """
            Test class with a method and a memoized property for testing
            the 'memoize' decorator.
            """
            def a_method(self):
                """
                Simple method that returns a fixed number.
                """
                return 42

            @memoize
            def a_property(self):
                """
                Property that calls 'a_method' and is decorated with 'memoize'
                to test the memoization functionality.
                """
                return self.a_method()


if __name__ == "__main__":
    unittest.main()
