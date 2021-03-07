from unittest import TestCase
from handlers import pulls


class TestPrime(TestCase):

    def setUp(self):
        """Init"""

    def test_exists_true(self):
        self.assertTrue(pulls.get_pulls("open")[0]["state"], "open")
        self.assertTrue(pulls.get_pulls("closed")[0]["state"], "closed")

    def test_exists_false(self):
        self.assertFalse(len(pulls.get_pulls("needs work")), len(pulls.get_pulls("accepted")))
        self.assertFalse(len(pulls.get_pulls("accepted")), len(pulls.get_pulls("needs work")))

    def test_site(self):
        self.assertEqual(pulls.get_pulls('all').status_code, 200)
        self.assertEqual(pulls.get_pulls("closed").status_code, 200)
        self.assertEqual(pulls.get_pulls("open").status_code, 200)
        self.assertEqual(pulls.get_pulls("needs work").status_code, 200)
        self.assertEqual(pulls.get_pulls("accepted").status_code, 200)

    def test_len(self):
        self.assertNotEqual(len(pulls.get_pulls("open")), 0)
        self.assertNotEqual(len(pulls.get_pulls("closed")), 0)
        self.assertNotEqual(len(pulls.get_pulls("accepted")), 0)
        self.assertNotEqual(len(pulls.get_pulls("needs work")), 0)
        self.assertNotEqual(len(pulls.get_pulls("all")), 0)

    def tearDown(self):
        """Finish"""
