import unittest

import src


class FindTest(unittest.TestCase):
    def test_find_ip(self):
        awsipset = src.download_aws_ip_set()
        self.assertEqual(len(src.find_ip(awsipset, "3.10.120.3")), 2)
        self.assertEqual(src.find_ip(awsipset, "3.10.120.3")[0]['ip_prefix'], "3.8.0.0/14")
        self.assertEqual(len(src.find_ip(awsipset, "1.1.1.1")), 0)
    def test_find_aws_ip(self):
        self.assertEqual(len(src.find_aws_ip("3.10.120.3")), 2)