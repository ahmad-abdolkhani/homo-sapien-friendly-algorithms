import multiply
import unittest


class Test_Multiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEquals(multiply.multiply(3, 2), 6)


if __name__ == '__main__':
    unittest.main()
