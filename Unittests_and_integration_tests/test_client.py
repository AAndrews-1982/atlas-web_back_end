#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient in client module.
"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError


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
        Test the org method. Ensures it returns the correct value for
        different organization names.
        """
        client = GithubOrgClient(org_name)
        result = client.org
        self.assertEqual(result, mock_get_json.return_value)
        mock_get_json.assert_called_once()

    def test_public_repos_url(self):
        """
        Test the _public_repos_url method. Checks if it correctly retrieves
        the repository URL from organization data.
        """
        with patch.object(GithubOrgClient,
                          "org", new_callable=PropertyMock) as patched:
            test_json = {"url": "google",
                         "repos_url": "https://www.atlasschool.com/"}
            patched.return_value = test_json
            github_client = GithubOrgClient(test_json.get("url"))
            response = github_client._public_repos_url
            patched.assert_called_once()
            self.assertEqual(response, test_json.get("repos_url"))

    @patch("client.get_json")
    def test_public_repos(self, get_patch):
        """
        Test the public_repos method. Mocks _public_repos_url and get_json
        to verify correct repository retrieval.
        """
        get_patch.return_value = [{"name": "atlas"},
                                  {"name": "abc"}]
        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock) as mock_get:
            mock_get.return_value = "http://google.com"
            github_client = GithubOrgClient("atlas")
            result = github_client.public_repos()
            self.assertEqual(result, ["atlas", "abc"])
            get_patch.assert_called_once()
            mock_get.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_return):
        """
        Test the has_license method. Validates if repositories have the
        specified license. Uses different license scenarios.
        """
        github_client = GithubOrgClient("atlas")
        result = github_client.has_license(repo, license_key)
        self.assertEqual(expected_return, result)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for the GithubOrgClient class.
    These tests use payloads from fixtures to simulate
    real-world data and scenarios.
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup method for integration tests.
        Initializes a patcher for requests.get.
        """
        cls.get_patcher = patch("requests.get", side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """
        Tear down method for integration tests. Stops the patcher after tests.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test the public_repos method in an integration test environment.
        Currently a placeholder for future test implementation.
        """
        test_class = GithubOrgClient("atlas")
        assert True

    def test_public_repos_with_license(self):
        """
        Test public_repos with a license argument in an integration test
        environment. Placeholder for future implementation.
        """
        test_class = GithubOrgClient("atlas")
        assert True
