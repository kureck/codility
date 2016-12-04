from unittest import main
from unittest import TestCase
from run import solution


class FrogRiverOneTest(TestCase):
    def test_1(self):
        '''should return 6'''
        X = 5
        A = [1, 3, 1, 4, 2, 3, 5, 4]
        self.assertEqual(6, solution(X, A))

    def test_2(self):
        '''should return -1'''
        X = 5
        A = [3]
        self.assertEqual(-1, solution(X, A))

if __name__ == '__main__':
    main()
