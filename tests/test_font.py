import unittest
import fontawesome47


class TestFonts(unittest.TestCase):

    def test(self):
        self.assertTrue(fontawesome47.get_path().exists())
        self.assertTrue(fontawesome47.get_data())


if __name__ == '__main__':
    unittest.main()
