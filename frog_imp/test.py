from unittest import main
from unittest import TestCase
from run import solution


class FrogImpTest(TestCase):
    def test_1(self):
        '''should return 3'''
        X = 10
        Y = 85
        D = 30
        self.assertEqual(3, solution(X, Y, D))

    def test_2(self):
        '''should return 3'''
        X = 1
        Y = 5
        D = 2
        self.assertEqual(2, solution(X, Y, D))

if __name__ == '__main__':
    main()
