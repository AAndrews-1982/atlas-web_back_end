#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from your_module_name import access_nested_map
# Replace 'your_module_name' with the
# actual name of your module


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
