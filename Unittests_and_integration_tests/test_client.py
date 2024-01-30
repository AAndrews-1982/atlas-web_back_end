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
    Test Suite for the GithubOrgClient class.
    Validates the functionality of the org() method for different org names.
    """

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Tests that org() method correctly calls get_json with the right URL.
        """
        # Setup the mock response object
        mock_response = Mock()
        mock_response.json.return_value = {}

        # Set the return value for the mocked get_json
        mock_get_json.return_value = mock_response

        # Create a GithubOrgClient instance and call the org method
        github_client = GithubOrgClient(org_name)
        github_client.org()

        # Check that get_json was called correctly
        expected_url = github_client.ORG_URL.format(org=org_name)
        mock_get_json.assert_called_once_with(expected_url)
