from unittest import main
from unittest import TestCase
from run import solution


class TapeEquilibriumTest(TestCase):
    def test_1(self):
        '''should return 1'''
        A = [3, 1, 2, 4, 3]
        self.assertEqual(1, solution(A))

    def test_2(self):
        '''should return 2000'''
        A = [-1000, 1000]
        self.assertEqual(2000, solution(A))

if __name__ == '__main__':
    main()
