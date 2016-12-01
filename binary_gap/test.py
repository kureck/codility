from unittest import main
from unittest import TestCase
from main import solution


class BinaryGapTest(TestCase):

    def test_15(self):
        """should return 0 for binary 15 (1111)"""
        self.assertEqual(solution(15), 0)

    def test_1041(self):
        """should return 5 for binary 1041 (10000010001)"""
        self.assertEqual(solution(1041), 5)

    def test_529(self):
        """should return 4 for binary 529 (1000010001)"""
        self.assertEqual(solution(529), 4)

    def test_20(self):
        """should return 1 for binary 20 (10100)"""
        self.assertEqual(solution(20), 1)

if __name__ == '__main__':
    main()
