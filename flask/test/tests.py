from unittest import TestCase
from handlers import pulls


class TestPrime(TestCase):

    def setUp(self):
        """Init"""

    def test_exists_open(self):
        self.assertTrue(pulls.get_inform("open", [{"state": "open"}])[0]["state"] == "open")
        self.assertTrue(pulls.get_inform("all", [{"state": "open"}])[0]["state"] == "open")
        self.assertTrue(pulls.get_inform("accepted", {"items": "work"}) == "work")

    def test_len(self):
        self.assertNotEqual(len(pulls.get_inform("open", [{"state": "open"}])), 0)
        self.assertNotEqual(len(pulls.get_inform("accepted", {"items": "work"})), 0)
        self.assertNotEqual(len(pulls.get_inform("all", [{"state": "all"}])), 0)

    def test_code(self):
        self.assertTrue(pulls.get_pulls_get("open")[0] == 200)

    def tearDown(self):
        """Finish"""
