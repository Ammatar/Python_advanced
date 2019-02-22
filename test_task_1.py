import unittest
from task_1 import subs

class TestSubs(unittest.TestCase):
    def test_subs_count(self):
        self.assertEqual(subs("asa"), 3)
        print()
    def test_subs_type(self):
        self.addTypeEqualityFunc(int, subs("asa"))

if __name__ == "__main__":
    unittest.main()