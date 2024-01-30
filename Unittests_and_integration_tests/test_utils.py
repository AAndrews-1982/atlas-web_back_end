#!/usr/bin/env python3
"""Unittests"""
import unittest
from unittest import mock
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test Suite for AccessNestedMap function.
    Tests the function with various nested map structures and paths.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test that access_nested_map returns the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path),
                         expected_result)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expec_except):
        """
        Test that access_nested_map raises KeyError with specific inputs.
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(str(error.exception), expec_except)


class TestGetJson(unittest.TestCase):
    """
    Test Suite for the get_json function.
    Validates JSON retrieval from a remote URL.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test the get_json function with a mocked requests.get.
        """
        mock_response = mock.Mock()
        mock_response.json.return_value = test_payload
        with mock.patch('requests.get', return_value=mock_response):
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """
    Test Suite for the Memoize decorator.
    Validates the functionality of memoizing a method's return value.
    """

    def test_memoize(self):
        """
        Test for the memoize function from utils.py.
        Ensures that it correctly memoizes the return
        value of a property method.
        """
        class TestClass:
            """
            TestClass to be used in the memoize test.
            Contains a method and a memoized property.
            """

            def a_method(self):
                """
                Returns a fixed numeric value.
                """
                return 42

            @memoize
            def a_property(self):
                """
                Returns a memoized property, calling a_method internally.
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            response = test_class.a_property
            self.assertEqual(response, 42)
            patched.assert_called_once()
