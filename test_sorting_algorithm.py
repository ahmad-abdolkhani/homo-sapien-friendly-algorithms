import sorting_algorithm    # The code to test
import unittest   # The test framework


class Test_TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(sorting_algorithm.bubble_sort(
            [4, 3, 2, 1]), [1, 2, 3, 4])

    def test_selection_sort(self):
        self.assertEquals(sorting_algorithm.selection_sort(
            [4, 3, 2, 1]), [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
