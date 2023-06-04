import unittest


class TestBuiltins(unittest.TestCase):
    """Test some python built-in methods"""
    def test_str_lwr(self):
        self.assertTrue("ABC".islower())

    def test_equal(self):
        self.assertEqual(0,4)



    def test_len(self):
        self.assertEqual(5, len("hello"))
        self.assertEqual(3, len(['a', 'b', 'c']))
        # edge case
        self.assertEqual(0, len(""))

    def test_str_upper(self):
        self.assertTrue("ABC".isupper())
        self.assertFalse("ABc".isupper())
        s = ""  # edge case
        self.assertFalse(s.isupper())
    # def test_sum(self):
    # self.assertEqual(2, len(['a','b','c']))


if __name__ == "__main__":
    unittest.main()

