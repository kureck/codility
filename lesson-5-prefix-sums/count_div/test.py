from unittest import main
from unittest import TestCase
from run import solution


class CountDivTest(TestCase):
    def test_1(self):
        '''should return 3'''
        A = 6
        B = 11
        K = 2
        self.assertEqual(3, solution(A, B, K))

    def test_2(self):
        '''should return 4'''
        A = 6
        B = 12
        K = 2
        self.assertEqual(4, solution(A, B, K))

    def test_3(self):
        '''should return 7'''
        A = 0
        B = 24
        K = 4
        self.assertEqual(7, solution(A, B, K))

if __name__ == '__main__':
    main()
