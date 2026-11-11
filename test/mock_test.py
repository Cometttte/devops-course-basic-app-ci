import unittest
from unittest.mock import patch

from src.awsip import find_aws_ip


class MockTest(unittest.TestCase):
    @patch('src.awsip.download_aws_ip_set')  # Make sure this path is correct
    def test_withmock(self, mock_download):
        mock_data = {
            "ip_prefix": "3.4.12.4/32",
            "region": "eu-west-1",
            "service": "AMAZON",
            "network_border_group": "eu-west-1"
        }
        mock_download.return_value = [mock_data]

        result = find_aws_ip("3.10.120.3")

        mock_download.assert_called_once()
        self.assertEqual(len(result), 0)

