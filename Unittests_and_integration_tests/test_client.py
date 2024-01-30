#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient in client module.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test Suite for GithubOrgClient class.
    Tests the functionality of retrieving organization information.
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json", return_value={"organization": True})
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        Ensures that the get_json function is called with the
        correct org name.
        """
        client = GithubOrgClient(org_name)
        result = client.org
        self.assertEqual(result, mock_get_json.return_value)
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')
